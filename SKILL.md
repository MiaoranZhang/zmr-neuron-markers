---
name: zmr-neuron-markers
description: "Annotate and audit adult human brain neurons from scRNA-seq or snRNA-seq using source-traceable marker panels, brain-region constraints, donor evidence and matched reference atlases. Use for neuronal identity, transmitter classes, regional subtypes, ambiguous or mixed clusters, or curation of neuron marker resources; not for diagnosing disease effects from cluster markers."
---

# ZMR Neuron Markers

为成年人人脑神经元建立可追溯、分层且允许拒绝赋名的鉴定证据。适用于成人 PD 单细胞/单核数据；其他物种、发育阶段必须重新核验。v1.3.0包含39个面板、77个基因；这是未经过独立队列准确率评估的审阅体系，不是经过验证的分类器。

## 文献与新增程序（v1.3.0）

NRGN仅增加神经元辅助证据，不改变既有神经元核心路径。RIT2富集和GALNTL6相关表达分别按两个program审阅：文献展示的富集群不等于固定名称、排他细胞类型或必须共表达的双基因组合。程序与身份保持分开，是否重叠由当前数据核验；TH未检出不证明生物学TH阴性。评估这些程序时读取[文献与用途](references/marker-literature.md)及[新增规则](references/rules-study-programs.md)。

逐基因来源见`assets/marker_literature.tsv`：论文题名、作者、年份、DOI、原文/规则位置、来源版本、核心/辅助/冲突用途及evidence_family齐全。数据库方法论文与原始marker实验来源分别标记；不臆造数据库条目的原始发现文献。GSE184950与Wang 2024共享输入时只能算来源支持，不算独立验证。

## cluster 整体鉴定（v1.3.0）

最终身份以正式 cluster（或经重新降维、聚类后审阅的 subcluster）为单位，不再逐细胞独立定名。综合未整合表达的核心组合、表达比例与效应量、群内一致性、供者/数据集复现、竞争谱系及匹配参考，先形成 cluster 注释表，再按 cluster_id 将统一标签关联到成员细胞。写回的标签须注明 `annotation_basis=cluster_inherited`、鉴定单位和规则版本；簇级置信度不表示每个成员都实测满足核心或具有相同的个体置信度。

逐细胞 marker 检出、参考预测、质量及冲突只作辅助证据和审计字段，不覆盖 cluster 身份，不凭单个细胞未检出核心就改为 Unknown，也不把按 marker/参考筛出的表达小组当成正式 subcluster。若簇内存在不能解释的竞争身份或明显异质性，在相应层级保留未定；需要细分时先正式子聚类并核验稳定性、marker 和供者构成。主注释 UMAP、DotPlot、组成统计使用 cluster 注释；逐细胞诊断图明确标为辅助证据。原作者逐细胞标签仍可用于来源核验及初始提取。

## 先选任务模式

- **查基因集／整理资源**：读取 [资源说明](references/resource-guide.md)、`assets/source_registry.json` 和 `assets/curated_panels.json`。根据物种、阶段、脑区、层级选面板，不将来源直接取并集。
- **鉴定细胞或核验不确定簇**：先读 [规则总则](references/rulebook.md)、[鉴定流程](references/annotation-workflow.md) 与 [数据约定](references/data-contract.md)。谱系/递质读取 [对应规则](references/rules-identity.md)，区域亚型/程序读取 [对应规则](references/rules-contextual.md)；不要只看 UMAP 相邻关系、单个 marker 或细胞级 P 值。
- **引入完整上游库**：读取资源说明中的导入和许可部分；`scripts/import_resources.py` 只下载并解析数据，不执行上游代码。未声明许可的完整规则仅在本地缓存，不能自动公开再分发。
- **用脑图谱作参考映射**：优先匹配成人、人类及实际脑区；核验参考输入、标签层级、模型版本和拒绝策略。映射是辅助假设，不替代表达核验。

## 必须保持的科学边界

1. 原作者标签、cluster 鉴定、成员继承标签、逐细胞辅助参考预测分别保存。不要将作者初筛标签或参考预测改称真实测量；最终身份遵循上述 cluster 整体鉴定规则。
2. 身份证据使用未整合 RNA 表达；counts、标准化表达及 Harmony/CCA 表示保持分离。marker 基因未被某数据集测量不等于零表达。
3. 先确认多基因神经元程序及排除性谱系，再判递质，再判区域亚型。程序单独记录；神经肽/受体在匹配解剖和完整证据下可支持身份，但单基因程序不自动升格为类型。
4. 使用原始稳定 ID 到 symbol 的可追溯映射；歧义 symbol 不任意合并。不得仅把大小写转换当作鼠到人同源映射。
5. 作者规则的阳性组合、替代规则和阴性条件不可改写成一张无结构基因清单。单核 dropout、低深度及测量缺失不能证明阴性。
6. 排除性 marker 应用于**可测且有足够深度的群体/供者证据**；同一细胞表达冲突才支持混合程序假设。一个簇同时含两类细胞不证明共递质，也不证明双细胞。
7. 保留 `Neuron: transmitter unresolved`、`Neuron: mixed/unresolved transmitter`、`Unknown/Uncertain`。按逐类型规则降级；补充证据不是补表达值。本版没有已验证的 rescue 路径，辅助集合不得任意替代缺失核心。
8. High 必须满足规则总则的适用性、表达质量、区分能力和冲突审阅四门槛及具体规则条件。分别报告大类/递质/亚型/程序置信度，供者复现和独立验证另列；High 不是校准概率。不要将 cluster marker 检验当作供者层面的 PD 疾病证据。

## 资源使用顺序

Siletti 作者规则用于大类/递质/区域程序的来源核验；Siletti 全脑和 Allen HMBA 人类参考用于匹配脑区的标签比较；Kamath 仅在已有可靠 DA 身份后用于 SNpc DA 亚型假设；ScType、CellMarker、PanglaoDB 是补充先验，不算相互独立的重复验证。来源可能共享同一论文，按 `evidence_family` 去重。

特别核验 [冲突清单](assets/source_conflicts.tsv)：ScType 的 Brain DA 条目含 DBH/SLC6A2/PPP1R1B，5-HT 条目含 TPH1，OPC 条目含 LHFPL3。不要据此直接给成人中脑细胞定名。详见资源说明，不能机械删除上游条目，也不能机械采用。

## 小型工具与交付

- `python scripts/audit_coverage.py --genes genes.txt --region midbrain --species human --output marker_coverage.tsv`：只审计精选面板的基因可测性与区域适用性，不执行细胞分类。输入 gene symbol 每行一个，可用 `--gene-column` 读取 TSV。
- `python scripts/review_rules.py --template da-core` / `--evidence YOUR_REVIEW.json`：生成审阅模板或检查已填写的表达证据记录。不会读取矩阵、自动生成阳性或核实附件真实性；输出等级仅反映所填证据是否满足规则。
- `python scripts/import_resources.py --source siletti_rules --out LOCAL_CACHE`：导入固定版本作者规则，保留路径、SHA256、正负极性和替代面板；完整输出不要提交到公开仓库。
- `python scripts/import_resources.py --source sctype --out LOCAL_CACHE`：导入固定版本 Brain 面板，保留原大小写、未明确的物种和缺失阴性条件。查看许可后才决定再分发。

输出至少包含逐细胞来源及身份表、cluster 注释证据表、基因可测性表、marker 展示、供者核验、参考映射结果及冲突表；字段见数据约定。所有输入只读，新注释使用新字段/新版本，不覆盖历史结果。下载大型参考、执行昂贵映射或修改既有鉴定前，确认它确属当前用户请求；创建本 SKILL 不等于获准重分析。
