# 资源索引与选择

## v1.3研究相关补充

[Wang等，Science Advances 2024](https://doi.org/10.1126/sciadv.adi8287)支持NRGN辅助背景，以及分别审阅RIT2富集和GALNTL6相关程序。RIT2、GALNTL6在原图与补表中的分布不同，不作为固定双阳性类别。原文方法、Fig1/2/4与TableS2的具体定位见[逐基因文献](marker-literature.md)及[研究程序规则](rules-study-programs.md)。数据库方法论文与原始研究的证据层级不同；查询含GSE184950时，与该论文共享数据，不能算独立验证。

版本、许可及 acquisition_status 的机器可读事实见 `assets/source_registry.json`，不要将 indexed_only 或 mapping payload not frozen 改称完整导入。

## Siletti 作者规则

- 仓库：https://github.com/linnarsson-lab/auto-annotation-ah
- 固定 commit：`02e092b4a3f0d294d4bcd8ab574dfc98f51d7981`
- 实际文件是带 YAML 风格头部的 `.md`，不一定是 `.yaml`，也不一定有开头 `---`。
- `Human_adult/Class`：谱系；`Neurotransmission`：递质；`Subtype/Neuronal`：区域亚型；`State`：状态；`Neuropeptides`：程序。
- 保留文件路径作为 panel_id。GABA1/2 共享简称，不能覆盖；文件上下文、正负规则、上游物种证据和源字段冲突一起保留。
- 原作者使用群体表达的 trinarization 判断 presence/absence；不得把它替换成“任一细胞 UMI>0/等于0”而声称复现作者算法。
- 完整规则没有发现明确仓库 LICENSE。导入本地以便审阅，不把完整衍生表公开上传。本包精选面板是独立编辑的小型事实索引，与字面规则分离。

## Siletti 全脑参考

- 仓库：https://github.com/linnarsson-lab/adult-human-brain
- DOI：https://doi.org/10.1126/science.add7046
- 对应作者表：`tables/cluster_annotation.xlsx`、`tables/subcluster_annotation.xlsx`、`tables/dissections.xlsx`。
- 官方访问教程：https://alleninstitute.github.io/abc_atlas_access/notebooks/WHB_cluster_annotation_tutorial.html
- 可先查脑区和分层标签，再下载适用参考子集。代码仓库、规则、表及由它训练的模型同属 Siletti evidence family，不能计作多次独立验证。
- 官方 Gene lists 页面列的是可用测量基因，不等同于每个细胞类型的 marker 清单。本次没有下载完整表达参考或建立映射模型。

## Allen HMBA 基底节/黑质

- 当前官方入口：https://brain-map.org/consortia/hmba/hmba-release-basal-ganglia
- 本地映射工具：https://github.com/AllenInstitute/cell_type_mapper
- 旧 GitHub 入口已标 deprecated，应采用当前官方页面。
- 关注**人类** precomputed_stats 和 query_markers，记录真实文件 release、URL、SHA256、标签层级。当前本包只有入口索引，不冒称已冻结完整参考。
- query_markers 是分类算法使用的特征，不是每个类别都具备特异性的诊断基因集。
- 使用实际解剖来源。Human/macaque/marmoset 与跨物种共识标签不能无条件互换。官方页面仍标 pre-print release，参考标签亦需表达核验。

## Kamath：只在 DA 父层级之后

- 代码：https://github.com/tkamath1/Kamathetal2022
- 原文：https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/
- DOI：https://doi.org/10.1038/s41593-022-01061-1
- Results/Extended Data Fig1：TH/SLC6A3/SLC18A2 组合；Fig1e 及 Results：SOX6/CALB1 相关分类；Fig3：SOX6_AGTR1 与 CALB1_TMEM200A 等程序。
- 这些少量精选事实不是十个 DA 亚型的完整 marker 库。要复现精细亚型，读取对应补充表和匹配 SNpc 参考，不只看一个标签基因。
- 论文中 PD 易损性结论不能转移为当前 query 的疾病证据；原始人类测序存在 dbGaP 访问限制，不绕过。

## ScType Brain

- 文件：https://github.com/IanevskiAleksandr/sc-type/blob/master/ScTypeDB_full.xlsx
- 已核验固定版本中 `tissueType=Brain` 为24个面板，逐条物种/年龄未明确；所有 inspected Brain 行的 negative 字段为空。
- 工具支持阳性/阴性 marker，不等于 Brain 数据已经提供完整阴性规则。
- 保留 DBH/SLC6A2、TPH1、LHFPL3 等原条目，但将冲突放入审阅清单。不要自动改字或丢弃原始证据来让结果符合预期。
- GPL-3.0 来源数据库未随本 MIT 技能再分发；导入器下载本地副本和原 LICENSE，不执行 ScType 上游 R 脚本。

## CellMarker 2.0 与 PanglaoDB

- CellMarker：https://bio-bigdata.hrbmu.edu.cn/CellMarker2.0/index.html
- 数据库论文：https://pmc.ncbi.nlm.nih.gov/articles/PMC9825416/
- PanglaoDB：https://panglaodb.se/markers.html
- 优先回到原始 PMID、物种、组织、疾病状态、发育期和测序技术；广义 Brain 条目不能代表成人黑质特异性。
- CellMarker/PanglaoDB/ScType 可能共享上游研究，不能“两个数据库都列出”就称两个独立实验支持。
- 完整下载未纳入本包。若用户提供下载表，应保留逐行出处、版本和许可，再按人类与实际脑区筛选，不直接混合库内所有 neuron 行。

## 导入与维护

```text
python scripts/import_resources.py --source siletti_rules --out local_imports
python scripts/import_resources.py --source sctype --out local_imports
```

导入器拒绝覆盖同名来源目录，固定 commit，写入原数据 SHA256、URL、检索日期、原规则和事实性 marker 行。输出默认语义是 LOCAL_REVIEW_ONLY。只有实际核验条款允许的衍生文件才可另行发布；本次 GitHub 发布排除整个 local_imports/source_cache。

更新时另建日期/版本目录，比较上游差异、许可和语义，不静默替换旧规则。采用新增 marker 前，把对应 source_locator、来源物种和 evidence_family 记到自己的证据表。程序类别不得因为更新来源而自动升格为身份。

## v1.1 判定规则的来源层级

逐类型规则见[规则总则](rulebook.md)。v1.1在原74个基因上增加核心/辅助/冲突审阅逻辑；v1.3新增NRGN、RIT2、GALNTL6，合计77个基因。`source_panel_ids`关联逐基因来源，`core_routes.basis`区分作者组合与本项目编辑的证据分组。来源支持某个组合，不等于在独立数据上验证了该规则，也不允许任意缺失补救。

关于 HCRT/PMCH、TPH1/TPH2、PPP1R1B 等解释上的修订及原始论文，集中列于规则总则末节；这些文献没有被冒充为完整下载的新参考图谱。
