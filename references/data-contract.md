# 数据与输出约定

## 目录和表

| 文件 | 必需信息 |
| --- | --- |
| source_registry | source_id, url, version/commit, retrieval_date, evidence_family, species, stage, brain_region, role, license_status, acquisition_status |
| marker assertions | panel_id, source_id, gene_symbol_raw, polarity, source_locator；映射后的 symbol/stable_id 另存，不能覆盖原值 |
| gene measurability | dataset_id, stable_gene_id, gene_symbol, assayed, mapping_status, reference_version |
| cell annotation | cell_id, original_barcode, dataset_id, sample_id, donor_id, author_label, cluster_id, celltype_major, transmitter_class, celltype_subtype, confidence_major, confidence_transmitter, confidence_subtype, annotation_basis, annotation_conflict |
| cluster evidence | cluster_id, gene, n_assayed, n_comparator_assayed, pct_in, pct_out, log2FC, n_evaluable_donors, donor_consistency, expression_layer |
| reference predictions | cell_id, reference_id/version, label_level, predicted_label, score_type, score, rejection_reason, mapping_conflict |
| rule review | rule_id, rulebook_version, unit_type, unit_id, claim_kind, level, core_route, gate evidence, review_grade, decision_status, candidate_only, parent_review, reviewer, review_date, fallback reason |
| external support | donor_replication, independent_validation, evidence_family, overlap with annotation evidence |

所有缺失值标为 NA/unknown，不臆造年龄、性别、脑区或供者ID。source_id 是资源，evidence_family 是共同上游研究；同库不同版本不能自动变成独立研究。

## curated_panels.json

这是本项目选择的**review panel**，不是上游字面规则。每个面板含唯一 id、label、category、species、stage、regions、positive、negative、sources、notes。`positive` 是需检查的 marker 集合，不隐含全部必须同细胞阳性；`negative` 是上下文冲突审阅线索，不是零 counts 即满足的条件。未列出阴性不代表不存在冲突。

category 分为 lineage、transmitter、regional_subtype、da_program、neuropeptide_program、non_neuronal_guard、maturation_program。`regions=["all"]` 表示用于宽泛谱系/程序筛查，不保证每个基因在所有脑区都有相同特异性。支持程序不等于身份。

## v1.2.0 鉴定单位

最终 `celltype_major`、`transmitter_class`、`celltype_subtype` 从正式 cluster/subcluster 的审阅表按 `annotation_unit_id` 关联，`annotation_basis=cluster_inherited`。保存 `annotation_unit_type=cluster`、`annotation_rulebook_version=1.2.0`、各层级 `cluster_confidence_*`；成员细胞不另行获得独立身份置信度，若保留通用 confidence 字段，须明确 `confidence_scope=cluster`。同一正式鉴定单位在同一身份层级只能有一个最终标签。

逐细胞来源、实测 marker、参考预测和冲突标志独立保留，仅用于辅助核验，不覆盖最终身份。正式子聚类须保留父 cluster_id、subcluster_id、方法参数和稳定性/marker/供者审阅记录；按 marker/参考挑出的表达分组不算正式 subcluster。

## 逐类型规则结构

`assets/rulebook_manifest.json` 登记版本、规则文件、公共门槛及验证状态；`assets/rules/*.json` 每条对应一个既有 panel_id。

| 字段 | 解释 |
| --- | --- |
| id / target_label / level / claim_kind | 对应面板、可评估标签、层级；identity 与 program 分开。 |
| scope / parent | 物种、阶段、脑区；需先满足的父级规则及等级。 |
| core_routes | 多条 route 为 OR；route 的 all_of 各组为 AND；每个基因数组组内为 OR。每条有来源或原创编辑依据，不能误称上游字面规则。 |
| supporting | 辅助基因、相关面板和适用说明；可为空，不为凑数量添加未溯源 marker。 |
| conflicts | 竞争程序及情境性冲突线索，不是任一基因阳性自动否决或零表达自动通过。 |
| high_requires / confidence_cap | 该类型在四门槛之外的审阅条件及最高允许等级；cap 是审阅规则的保守上限，不代表生物学上不可能。 |
| fallback | 缺失、强冲突时如何回退，以及适合保留的父级或未定标签。 |
| rescue_routes / validation_status | 本版 rescue 为空，所有规则标 curated_unbenchmarked；不宣称已验证的表达补救或准确率。 |
| source_panel_ids | 关联现有逐基因来源表；core 的组合逻辑另有 basis 和 note。 |

上述逻辑作用于已经审阅的表达证据，而非 counts 是否大于零。`supported` 必须说明检测层、比较对象、表达富集/比例和归属依据；缺失本身不能改写为 supported。High 的定义及复现/验证分离规则见[规则总则](rulebook.md)。

逐细胞和簇级证据分别保存。成员继承统一簇标签不等于获得逐细胞实测核心支持，不能仅更改 unit_id 就把簇级判断复制为单细胞证据。参考预测另存候选、映射质量和推断来源，用于簇级核验；它不是逐细胞最终身份或人工填写核心 marker 阳性的理由。

审阅输入由 `python scripts/review_rules.py --template RULE_ID` 生成，以当前模板为准。每个门槛和附加检查包含 pass/fail/unknown 与证据引用；每条基因证据包含状态和实际归属对象。操作者审阅内容的真实性不由检查器验证。结果不直接写回细胞元数据；实际应用需保存原始标签、新标签、review_grade、来源及冲突，再决定报告粒度。

输入必须声明 `rulebook_version="1.2.0"`；缺失或不同版本会被拒绝，避免旧审阅记录静默套用新规则。identity 审阅要求 `unit_type="cluster"`，包含已正式聚类的 subcluster；cell 单位仅允许 program 诊断。规则升级后需重新核对证据，不能只替换版本号。

`reviewer` 和 `review_date` 用于记录审核人及 `YYYY-MM-DD` 日期；空模板可以检查缺口，但这两项不完整时不能得到 High。Low 的建议标签固定为 `Unknown/Uncertain`，NotApplicable 的建议标签为空；父级记录只保存证据状态，不会在质量失败或谱系冲突后自动继承。核心满足和技术审阅完成的记录也不等同于真实性已被独立验证。

部分核心记录的 Moderate 只描述审阅材料完整性，不能写成 `annotation_confidence=Moderate`。完整核心路径未满足时，输出 `decision_status=partial_core_review_required`、`partial_core_not_type_specific=true`、`type_specific_candidate=false`，只显示层级未定，不建议具体目标类型。`target_label` 始终表示被评估的规则目标，绝不是实际赋给细胞的标签。

## 导入作者规则

上游字段 definition 中的 `+`/`-` 保留为 source_positive/source_negative，不转成通用定名规则。用文件路径形成唯一 panel_id：NT-GABA1 和 NT-GABA2 即使共享 abbreviation，也不能覆盖或把两条替代规则强制相交。导入后先比较原规则和归档、核验 applicability，再决定是否用于分析。

ScType Brain 原表不标注逐条物种/年龄；species、stage 留为 unspecified。混合大小写原值不自动改为人类正式符号。空的负 marker 字段是 not_provided，不是“所有其他 marker 都阴性”。

## audit_coverage 输入

genes.txt 每行一个**已核验的 gene symbol**；也可提供 TSV 和 `--gene-column SYMBOL_COLUMN`。建议逐数据集单独审计而非只审计 union genes。脚本做精确、区分大小写匹配，不读表达矩阵，不产生细胞标签。

输出 positive_assayed/missing、negative_assayed/missing、coverage、region_status、species_status。coverage 只是可测覆盖度，不是检出率或注释置信度。缺失负 marker 输出 unknown；测得但表达为零也不能由此脚本认定真正阴性。
