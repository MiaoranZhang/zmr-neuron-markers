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

所有缺失值标为 NA/unknown，不臆造年龄、性别、脑区或供者ID。source_id 是资源，evidence_family 是共同上游研究；同库不同版本不能自动变成独立研究。

## curated_panels.json

这是本项目选择的**review panel**，不是上游字面规则。每个面板含唯一 id、label、category、species、stage、regions、positive、negative、sources、notes。`positive` 是需检查的 marker 集合，不隐含全部必须同细胞阳性；`negative` 是上下文冲突审阅线索，不是零 counts 即满足的条件。未列出阴性不代表不存在冲突。

category 分为 lineage、transmitter、regional_subtype、da_program、neuropeptide_program、non_neuronal_guard、maturation_program。`regions=["all"]` 表示用于宽泛谱系/程序筛查，不保证每个基因在所有脑区都有相同特异性。支持程序不等于身份。

## 导入作者规则

上游字段 definition 中的 `+`/`-` 保留为 source_positive/source_negative，不转成通用定名规则。用文件路径形成唯一 panel_id：NT-GABA1 和 NT-GABA2 即使共享 abbreviation，也不能覆盖或把两条替代规则强制相交。导入后先比较原规则和归档、核验 applicability，再决定是否用于分析。

ScType Brain 原表不标注逐条物种/年龄；species、stage 留为 unspecified。混合大小写原值不自动改为人类正式符号。空的负 marker 字段是 not_provided，不是“所有其他 marker 都阴性”。

## audit_coverage 输入

genes.txt 每行一个**已核验的 gene symbol**；也可提供 TSV 和 `--gene-column SYMBOL_COLUMN`。建议逐数据集单独审计而非只审计 union genes。脚本做精确、区分大小写匹配，不读表达矩阵，不产生细胞标签。

输出 positive_assayed/missing、negative_assayed/missing、coverage、region_status、species_status。coverage 只是可测覆盖度，不是检出率或注释置信度。缺失负 marker 输出 unknown；测得但表达为零也不能由此脚本认定真正阴性。
