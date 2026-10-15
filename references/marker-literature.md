# 神经元marker的文献与逐基因溯源

v1.3.0全部77个基因均在[`marker_literature.tsv`](../assets/marker_literature.tsv)登记；共131条逐来源记录。同一基因在不同面板、极性或来源中分别保留。记录论文作者、题名、期刊、年份、DOI、原文/规则定位、固定版本、evidence_family及核心/辅助/冲突用途。论文源表见[`literature_registry.json`](../assets/literature_registry.json)。

## 文献用途

| 来源 | 参考文献 | 本SKILL的实际用途 |
|---|---|---|
| Siletti规则及图谱 | Siletti K et al. *Transcriptomic diversity of cell types across the adult human brain*. Science. 2023. [10.1126/science.add7046](https://doi.org/10.1126/science.add7046) | 成人脑谱系、递质和区域规则；逐基因定位到固定commit的具体规则文件。图谱和衍生规则共享来源，不算独立重复验证。 |
| Kamath | Kamath T et al. *Single-cell genomic profiling of human dopamine neurons identifies a population that selectively degenerates in Parkinson’s disease*. Nature Neuroscience. 2022. [10.1038/s41593-022-01061-1](https://doi.org/10.1038/s41593-022-01061-1) | 成人黑质DA三联、SOX6/CALB1及相关程序。来源中的易损性不转移给查询数据。 |
| Wang/GSE184950 | Wang Q, Wang M, Choi I, et al. *Molecular profiling of human substantia nigra identifies diverse neuron types associated with vulnerability in Parkinson’s disease*. Science Advances. 2024;10:eadi8287. [10.1126/sciadv.adi8287](https://doi.org/10.1126/sciadv.adi8287) | NRGN辅助；RIT2和GALNTL6分别作为神经元表达程序。Methods、Fig1、Fig2、Fig4及TableS2定位分别登记。 |
| ScType | Ianevski A et al. *Fully-automated and ultra-fast cell-type identification using specific marker combinations from single-cell transcriptomic data*. Nature Communications. 2022. [10.1038/s41467-022-28803-w](https://doi.org/10.1038/s41467-022-28803-w) | 聚合数据库/方法文献；仅采用经核查的Brain条目，保留原定位与物种、年龄未明确的限制。 |
| PanglaoDB | Franzen O et al. *PanglaoDB: a web server for exploration of mouse and human single-cell RNA sequencing data*. Database. 2019;baz046. [10.1093/database/baz046](https://doi.org/10.1093/database/baz046) | SNAP25/STMN2等精选关联的聚合来源；不能用数据库论文替代该marker在目标脑区的原始验证。 |
| CellMarker 2.0 | Hu C et al. *CellMarker 2.0: an updated database of manually curated cell markers in human/mouse and web tools based on scRNA-seq data*. Nucleic Acids Research. 2023. [10.1093/nar/gkac947](https://doi.org/10.1093/nar/gkac947) | 目前为资源索引，没有把完整库的逐行marker导入本SKILL。 |

Allen HMBA是参考图谱入口；本SKILL没有内置完整mapping marker或表达模型。实际用于项目时另行记录下载文件的release、引用和SHA256，不能给尚未下载的payload编造固定论文出处。

## 来源的含义

`evidence_kind`区分原始人脑研究、图谱配套规则和聚合数据库论文。`original_marker_discovery_paper`没有确切依据时为NA：这里追溯的是本规则采用该事实的实际来源，并不声称所有77个基因都已追溯到最早发现实验。ScType/PanglaoDB有共同上游来源时不能当作两项独立实验。部分Siletti规则的理由引用小鼠资料，原来源物种保留，不升级为人类验证。

RIT2与GALNTL6在Wang原图及TableS2的分布不同：RIT2在作者C9显著富集；GALNTL6在C6和部分子群富集。两者分别登记，不建立凭空推导的双阳性固定类别。查询含GSE184950时，与该论文的重合不能作独立验证。

NRGN仅辅助神经元背景，不是新增必需核心，也不能单基因决定兴奋性/递质或替代SNAP25/SYP组。新增规则详见[研究相关程序](rules-study-programs.md)。
