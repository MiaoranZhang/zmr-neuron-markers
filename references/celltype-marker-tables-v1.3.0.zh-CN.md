# ZMR神经元细胞鉴定marker及来源汇总

整理日期：2026-10-18。规则版本：**v1.3.0**。本文件是现有规则的可读汇编，不修改鉴定逻辑、基因集合或现有PD细胞注释。

规则基线：[zmr-neuron-markers / 38c5c25](https://github.com/MiaoranZhang/zmr-neuron-markers/tree/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1)。完整覆盖39项规则；来源附录覆盖77个基因、131条逐来源记录。附录包括冲突/情境阴性项，不能把全部77基因解释为阳性鉴定marker。

## 阅读与使用约定

- **核心鉴定marker**：具体规则要求的表达证据入口，不等于单基因阳性即可确定身份。
- **辅助验证marker**：加强谱系、背景或一致性证据，不等于证据较低；当前无已验证的缺失核心补救路线，不能任意替代核心。
- **文献相关表达特征**：可描述已确认身份内的亚群相关表达或富集，不自动成为固定、排他的新细胞类型。单基因特征不称为已证明的协调多基因表达程序。
- **High/Moderate**是实际cluster审阅等级，不是基因固有等级或校准概率。适用范围、表达质量、竞争身份区分及冲突解释均需核验，供者复现与独立验证另列。
- 最终身份按正式cluster/subcluster整体鉴定，成员继承标签；本表的“+”表示组合要求，“或”表示替代路径，不要求每个低深度细胞全部检出，也不能用不同细胞的零散阳性拼成同细胞组合。
- 身份证据使用未整合RNA表达；未测量不等于零表达，未检出不等于可靠阴性。非神经元面板用于竞争谱系排查，不构成完整胶质/免疫细胞分类库。
- 文献支持、来源规则及本库编辑组合分开：有文献不等于已验证该组合在成人黑质的特异性；共享来源的数据库/图谱不能重复计作独立证据。当前体系未做独立留出队列分类性能校准。
- 表格“核心/辅助”的文献链接汇总对应基因的实际来源，不表示每篇论文均验证了整条组合；具体组合采用哪条作者路径或本库编辑依据，见附录A。例如去甲肾上腺素能核心组合来自Siletti，Kamath只涉及其中共享基因的来源，不是该类型的独立组合验证。

## 目录

- [表1：神经元大类与递质类型](#table-1)
- [表2：脑区限制的神经元亚型](#table-2)
- [表3：文献相关亚群与附加表达特征](#table-3)
- [表4：非神经元竞争谱系排查](#table-4)
- [参考文献与来源版本](#references)
- [附录A：每条规则的来源依据及竞争marker](#rule-evidence)
- [附录B：逐基因、逐面板、逐来源溯源](#gene-evidence)

<a id="table-1"></a>

## 表1．神经元大类与递质类型

| 细胞类型／表达特征 | 核心鉴定／命名marker组合 | 辅助验证marker | 参考文献与来源 | 适用范围及限制 |
|---|---|---|---|---|
| 神经元 Neuron | （SNAP25 或 SYP） + （MAP2 或 RBFOX3 或 STMN2 或 TUBB3） | NRGN | 核心：[S1](#ref-s1)、[S4](#ref-s4)、[S5](#ref-s5)；辅助：[S3](#ref-s3)；[来源定位](#rule-neuronal-background) | 本库编辑的两组组合；NRGN仅辅助；排查非神经元谱系。 |
| 多巴胺能神经元 DA | TH + SLC6A3 + SLC18A2；或 TH + DDC + SLC6A3 | DDC、SLC18A2 | 核心：[S1](#ref-s1)、[S2](#ref-s2)；辅助：[S1](#ref-s1)、[S2](#ref-s2)；[来源定位](#rule-da-core) | 两条核心路径为或关系；TH单独不足；审阅DBH/PNMT竞争背景。 |
| GABA能神经元 | GAD1 + SLC32A1；或 GAD2 + SLC32A1 | GAD1、GAD2 | 核心：[S1](#ref-s1)；辅助：[S1](#ref-s1)；[来源定位](#rule-gaba-core) | 另一种GAD加强一致性，但不自动替代SLC32A1；审阅甘氨酸/谷氨酸背景。 |
| SLC17A7相关谷氨酸能神经元 | SLC17A7 | SNAP25、SYP、MAP2 | 核心：[S1](#ref-s1)；辅助：[S4](#ref-s4)、[S5](#ref-s5)；[来源定位](#rule-glut-vglut1) | 单marker以外需匹配脑区整体背景；仅单基因证据最多Moderate。 |
| SLC17A6相关谷氨酸能神经元 | SLC17A6 | SNAP25、SYP、MAP2 | 核心：[S1](#ref-s1)；辅助：[S4](#ref-s4)、[S5](#ref-s5)；[来源定位](#rule-glut-vglut2) | 单marker以外需匹配整体背景；DA伴随SLC17A6时不能直接覆盖DA身份。 |
| 甘氨酸能神经元 | SLC6A5 + SLC32A1 | SNAP25、MAP2 | 核心：[S1](#ref-s1)；辅助：[S4](#ref-s4)、[S5](#ref-s5)；[来源定位](#rule-glycinergic) | SLC32A1与GABA能共享；需解剖相容及竞争身份核验。 |
| 5-HT能神经元 | TPH2 + FEV + DDC | SLC18A2 | 核心：[S1](#ref-s1)；辅助：[S2](#ref-s2)；[来源定位](#rule-serotonergic) | TPH1不能替代TPH2；DDC/SLC18A2属于共享单胺背景。 |
| 胆碱能神经元 | CHAT + SLC5A7 | SLC18A3 | 核心：[S1](#ref-s1)、[S4](#ref-s4)；辅助：[S4](#ref-s4)；[来源定位](#rule-cholinergic) | 当前没有CHAT + SLC18A3替代核心的已验证路线。 |
| 去甲肾上腺素能神经元 | DBH + TH + DDC | SLC18A2 | 核心：[S1](#ref-s1)、[S2](#ref-s2)；辅助：[S2](#ref-s2)；[来源定位](#rule-noradrenergic) | DBH结合合成背景；区分DA/肾上腺素能，不直接推断蓝斑来源。 |
| 肾上腺素能神经元 | PNMT + DBH + TH + DDC | SLC18A2 | 核心：[S1](#ref-s1)、[S2](#ref-s2)；辅助：[S2](#ref-s2)；[来源定位](#rule-adrenergic) | 需匹配成人解剖部位和整体参考；PNMT单独不足。 |
| 组胺能神经元候选 | HDC | SNAP25、MAP2、SYP | 核心：[S1](#ref-s1)；辅助：[S4](#ref-s4)、[S5](#ref-s5)；[来源定位](#rule-histaminergic) | 当前身份上限Moderate；HDC高表达也不能解除上限。 |

<a id="table-2"></a>

## 表2．有脑区限制的神经元亚型

| 细胞类型／表达特征 | 核心鉴定／命名marker组合 | 辅助验证marker | 参考文献与来源 | 适用范围及限制 |
|---|---|---|---|---|
| 皮层PVALB相关中间神经元 | PVALB + LHX6 + DLX1 + GAD2 + FOXG1 | GAD1、SLC32A1 | 核心：[S1](#ref-s1)；辅助：[S1](#ref-s1)；[来源定位](#rule-cortical-pvalb) | 限成人皮层；GABA父级High；不是通用中脑PVALB分类器。 |
| 皮层SST相关中间神经元 | SST + LHX6 + DLX1 + GAD2 + FOXG1 | GAD1、SLC32A1 | 核心：[S1](#ref-s1)；辅助：[S1](#ref-s1)；[来源定位](#rule-cortical-sst) | 限成人皮层；GABA父级High；ADARB2竞争背景按来源语境审阅。 |
| 皮层VIP相关中间神经元 | VIP + ADARB2 + CXCL14 + DLX1 + GAD2 + FOXG1 | GAD1、SLC32A1 | 核心：[S1](#ref-s1)；辅助：[S1](#ref-s1)；[来源定位](#rule-cortical-vip) | 限成人皮层；GABA父级High；非皮层VIP表达另作特征。 |
| 皮层LAMP5相关中间神经元 | LAMP5 + ADARB2 + CXCL14 + GAD2 + FOXG1 | GAD1、SLC32A1 | 核心：[S1](#ref-s1)；辅助：[S1](#ref-s1)；[来源定位](#rule-cortical-lamp5) | 限成人皮层；GABA父级High；比较LHX6及近邻参考类别。 |
| 纹状体D1相关中型棘状神经元 | DRD1 + GPR88 + RGS9 + FOXP1 + SLC32A1 + FOXG1 | GAD1、GAD2 | 核心：[S1](#ref-s1)；辅助：[S1](#ref-s1)；[来源定位](#rule-striatal-d1) | 限成人纹状体；GABA父级High和MSN背景；DRD1是受体而非DA合成证据。 |
| 纹状体D2相关中型棘状神经元 | DRD2 + GPR88 + RGS9 + FOXP1 + SLC32A1 + FOXG1 | GAD1、GAD2 | 核心：[S1](#ref-s1)；辅助：[S1](#ref-s1)；[来源定位](#rule-striatal-d2) | 限成人纹状体；GABA父级High和MSN背景；DRD2不证明细胞产生DA。 |
| 小脑Purkinje相关神经元 | PCP2 + SKOR2 + PVALB + GAD2 | GAD1、SLC32A1 | 核心：[S1](#ref-s1)；辅助：[S1](#ref-s1)；[来源定位](#rule-cerebellar-purkinje) | 限成人小脑；GABA父级High；上游理由含小鼠研究，需匹配人类参考。 |
| 小脑颗粒细胞相关神经元 | CBLN1 + CBLN3 + GABRA6 | SLC17A7、SLC17A6 | 核心：[S1](#ref-s1)；辅助：[S1](#ref-s1)；[来源定位](#rule-cerebellar-granule) | 限成人小脑；神经元父级High；GABRA6为受体，不证明GABA合成。 |

<a id="table-3"></a>

## 表3．文献相关亚群与附加表达特征

| 细胞类型／表达特征 | 核心鉴定／命名marker组合 | 辅助验证marker | 参考文献与来源 | 适用范围及限制 |
|---|---|---|---|---|
| DA内SOX6相关表达特征 | SOX6 | TH、SLC6A3、SLC18A2、DDC | 核心：[S2](#ref-s2)；辅助：[S1](#ref-s1)、[S2](#ref-s2)；[来源定位](#rule-da-sox6) | 先有DA父级High；不单独确定精确亚型、解剖层次或PD易损性。 |
| DA内CALB1相关表达特征 | CALB1 | TH、SLC6A3、SLC18A2、DDC | 核心：[S2](#ref-s2)；辅助：[S1](#ref-s1)、[S2](#ref-s2)；[来源定位](#rule-da-calb1) | 先有DA父级High；CALB1并非DA专属，不直接证明PD抗性。 |
| DA内SOX6/AGTR1亚群相关特征 | SOX6 + AGTR1 | TH、SLC6A3、SLC18A2、DDC | 核心：[S2](#ref-s2)；辅助：[S1](#ref-s1)、[S2](#ref-s2)；[来源定位](#rule-da-sox6-agtr1) | 成人黑质、DA父级High；简化相关特征，不等于完整Kamath亚型映射。 |
| DA内CALB1/TMEM200A亚群相关特征 | CALB1 + TMEM200A | TH、SLC6A3、SLC18A2、DDC | 核心：[S2](#ref-s2)；辅助：[S1](#ref-s1)、[S2](#ref-s2)；[来源定位](#rule-da-calb1-tmem200a) | 成人黑质、DA父级High；不能直接推断精确亚型或疾病保护。 |
| RIT2富集神经元特征 | RIT2 | RBFOX3、SNAP25、SYP、MAP2、NRGN | 核心：[S3](#ref-s3)；辅助：[S1](#ref-s1)、[S3](#ref-s3)、[S4](#ref-s4)、[S5](#ref-s5)；[来源定位](#rule-rit2-enriched-program) | 成人中脑/黑质；神经元父级High；需相对富集和供者证据，不要求GALNTL6共表达。 |
| GALNTL6相关神经元特征 | GALNTL6 | RBFOX3、SNAP25、SYP、MAP2、NRGN | 核心：[S3](#ref-s3)；辅助：[S1](#ref-s1)、[S3](#ref-s3)、[S4](#ref-s4)、[S5](#ref-s5)；[来源定位](#rule-galntl6-associated-program) | 成人中脑/黑质；神经元父级High；不要求RIT2共表达，不单独指定DA/GABA。 |
| SLC17A8相关表达特征 | SLC17A8 | SNAP25、SYP、MAP2 | 核心：[S1](#ref-s1)；辅助：[S4](#ref-s4)、[S5](#ref-s5)；[来源定位](#rule-glut-vglut3) | 仅为表达特征，不自动确认为排他的谷氨酸能/兴奋性身份。 |
| HCRT相关神经肽特征 | HCRT | SNAP25、MAP2、SYP | 核心：[S1](#ref-s1)；辅助：[S4](#ref-s4)、[S5](#ref-s5)；[来源定位](#rule-peptide-hcrt) | 先有神经元父级High；当前无完整orexin身份路线，需审阅脑区及环境RNA。 |
| PMCH相关神经肽特征 | PMCH | SNAP25、MAP2、SYP | 核心：[S1](#ref-s1)；辅助：[S4](#ref-s4)、[S5](#ref-s5)；[来源定位](#rule-peptide-pmch) | 先有神经元父级High；当前无完整MCH身份路线，不能凭单基因直接定类型。 |
| NPY相关神经肽特征 | NPY | SNAP25、MAP2、SYP | 核心：[S1](#ref-s1)；辅助：[S4](#ref-s4)、[S5](#ref-s5)；[来源定位](#rule-peptide-npy) | 先有神经元父级High；不对应唯一细胞身份、脑区或递质。 |
| SST相关神经肽特征 | SST | SNAP25、MAP2、SYP | 核心：[S1](#ref-s1)；辅助：[S4](#ref-s4)、[S5](#ref-s5)；[来源定位](#rule-peptide-sst) | 先有神经元父级High；与皮层SST身份路线分开。 |
| VIP相关神经肽特征 | VIP | SNAP25、MAP2、SYP | 核心：[S1](#ref-s1)；辅助：[S4](#ref-s4)、[S5](#ref-s5)；[来源定位](#rule-peptide-vip) | 先有神经元父级High；不自动指定皮层或GABA身份。 |
| 未成熟/发育相关表达特征 | DCX + NEUROD1 + TUBB3 | MAP2、SNAP25、SYP | 核心：[S4](#ref-s4)；辅助：[S4](#ref-s4)、[S5](#ref-s5)；[来源定位](#rule-immature-program) | 上限Moderate；来源年龄/物种/脑区未细分；不能证明成人神经发生。 |

<a id="table-4"></a>

## 表4．非神经元竞争谱系排查

| 细胞类型／表达特征 | 核心鉴定／命名marker组合 | 辅助验证marker | 参考文献与来源 | 适用范围及限制 |
|---|---|---|---|---|
| 少突胶质细胞 | PLP1 + MBP + MOG | SOX10 | 核心：[S1](#ref-s1)、[S4](#ref-s4)；辅助：[S1](#ref-s1)、[S4](#ref-s4)；[来源定位](#rule-oligo-guard) | 成套髓鞘信号仍需排查环境RNA、神经元混合及OPC竞争。 |
| 少突胶质前体细胞 OPC | SOX10 + PDGFRA | CSPG4 | 核心：[S1](#ref-s1)、[S4](#ref-s4)；辅助：[S1](#ref-s1)；[来源定位](#rule-opc-guard) | CSPG4为共享情境信号；不能单独定OPC或替代双核心。 |
| 星形胶质细胞 | AQP4 + GJA1 | ALDH1L1、SLC1A2 | 核心：[S1](#ref-s1)、[S4](#ref-s4)；辅助：[S4](#ref-s4)；[来源定位](#rule-astro-guard) | 辅助集合不是替代核心；比较FOXJ1相关纤毛/室管膜及其他谱系。 |
| 广义髓系细胞，亚型未定 | TYROBP + DOCK8 | 当前未设独立辅助集合 | 核心：[S1](#ref-s1)；辅助：—；[来源定位](#rule-myeloid-guard) | 需完整免疫背景和匹配参考；本规则不直接命名小胶质或BAM。 |
| 巨噬细胞相关类型 | CD163 + MRC1 + F13A1 | TYROBP、DOCK8 | 核心：[S1](#ref-s1)；辅助：[S1](#ref-s1)；[来源定位](#rule-macrophage-guard) | 需与小胶质等比较；不直接推断边界位置、外周浸润或细胞起源。 |
| 内皮细胞 | CLDN5 + PECAM1 + FLT1 | 当前未设独立辅助集合 | 核心：[S1](#ref-s1)；辅助：—；[来源定位](#rule-endothelial-guard) | FLT1单独不足；比较血管壁及免疫候选，不细分动静脉。 |
| 周细胞相关类型 | PDGFRB + CSPG4 | 当前未设独立辅助集合 | 核心：[S1](#ref-s1)；辅助：—；[来源定位](#rule-pericyte-guard) | CSPG4与OPC共享；需区分平滑肌/OPC，MYH11缺测不是排除证据。 |

<a id="references"></a>

## 参考文献与来源版本

<a id="ref-s1"></a>

### S1．Siletti K et al.，2023

Siletti K et al. *Transcriptomic diversity of cell types across the adult human brain*. Science. 2023. [DOI: 10.1126/science.add7046](https://doi.org/10.1126/science.add7046)。

- 实际来源：[资源入口](https://github.com/linnarsson-lab/auto-annotation-ah)；登记版本：`02e092b4a3f0d294d4bcd8ab574dfc98f51d7981`。
- 证据属性与用途：图谱配套作者规则，不是每个marker最早发现的原始实验文献；部分理由引用小鼠研究。核心分组及区域规则中的人工整理并非完整原作者分类器。
- 来源族：`siletti_2023`。

<a id="ref-s2"></a>

### S2．Kamath T et al.，2022

Kamath T et al. *Single-cell genomic profiling of human dopamine neurons identifies a population that selectively degenerates in Parkinson’s disease*. Nature Neuroscience. 2022. [DOI: 10.1038/s41593-022-01061-1](https://doi.org/10.1038/s41593-022-01061-1)。

- 实际来源：[资源入口](https://github.com/tkamath1/Kamathetal2022)；登记版本：`cae72e19290efe1ea8756e2032507905bdea52ba`。
- 证据属性与用途：人类SNpc原始研究；DA三联、SOX6/CALB1分支及SOX6_AGTR1、CALB1_TMEM200A相关特征。精确亚型及易损性不从简化marker直接推断。
- 来源族：`kamath_2022`。

<a id="ref-s3"></a>

### S3．Wang Q, Wang M, Choi I, et al.，2024

Wang Q, Wang M, Choi I, et al. *Molecular profiling of human substantia nigra identifies diverse neuron types associated with vulnerability in Parkinson’s disease*. Science Advances. 2024. [DOI: 10.1126/sciadv.adi8287](https://doi.org/10.1126/sciadv.adi8287)。

- 实际来源：[资源入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC10780895/)；登记版本：`Science Advances 2024;10:eadi8287; DOI 10.1126/sciadv.adi8287`。
- 证据属性与用途：人类黑质原始研究；NRGN见Methods/Cluster cell-type annotation；RIT2见Fig1C、Fig2、TableS2/C9；GALNTL6见Fig1C、Fig4B/E/G、TableS2/C6及部分子群。RIT2与GALNTL6分别登记，不是必需双阳性组合。查询含GSE184950时与来源共享数据，不能算独立验证。
- 来源族：`wang_2024_GSE184950`。

<a id="ref-s4"></a>

### S4．Ianevski A et al.，2022

Ianevski A et al. *Fully-automated and ultra-fast cell-type identification using specific marker combinations from single-cell transcriptomic data*. Nature Communications. 2022. [DOI: 10.1038/s41467-022-28803-w](https://doi.org/10.1038/s41467-022-28803-w)。

- 实际来源：[资源入口](https://github.com/IanevskiAleksandr/sc-type)；登记版本：`630e15cf1e51f2612eda4ad0406dfb17503fa8c9`。
- 证据属性与用途：聚合数据库/方法论文，不是每个marker的原始实验验证；Brain条目的物种、年龄与脑区未充分细分。本文件仅复述本库精选事实，不再分发完整ScType数据库。
- 来源族：`sctype_2022_aggregated_catalog`。

<a id="ref-s5"></a>

### S5．Franzen O et al.，2019

Franzen O et al. *PanglaoDB: a web server for exploration of mouse and human single-cell RNA sequencing data*. Database. 2019. [DOI: 10.1093/database/baz046](https://doi.org/10.1093/database/baz046)。

- 实际来源：[资源入口](https://panglaodb.se/markers.html)；登记版本：`web marker catalog reports last update 2020-03-27; pages checked 2026-10-14`。
- 证据属性与用途：聚合数据库论文；精选人/鼠条目只能作为先验，不能证明成人黑质特异性。
- 来源族：`panglaodb_2019_aggregated_catalog`。

<a id="ref-s6"></a>

### S6．Hu C et al.，2023

Hu C et al. *CellMarker 2.0: an updated database of manually curated cell markers in human/mouse and web tools based on scRNA-seq data*. Nucleic Acids Research. 2023. [DOI: 10.1093/nar/gkac947](https://doi.org/10.1093/nar/gkac947)。

- 实际来源：[资源入口](https://bio-bigdata.hrbmu.edu.cn/CellMarker2.0/index.html)；登记版本：`resource index checked 2026-10-14; complete download not acquired`。
- 证据属性与用途：资源索引，目前没有从完整数据库导入marker断言，因此没有用它为上表任何marker充当直接来源。
- 来源族：`cellmarker_2_aggregated_catalog`。

Siletti全脑图谱与S1同属一个来源族；[固定图谱代码版本](https://github.com/linnarsson-lab/adult-human-brain/tree/2b5aa12dffb8cc1bcb3979c409cb6ac907546b2e)可用于匹配参考选择。[Allen HMBA](https://brain-map.org/consortia/hmba/hmba-release-basal-ganglia)在本SKILL仅为参考入口索引，没有内置完整mapping marker或表达模型；不为未冻结payload编造论文出处。上述版本来自v1.3.0已登记来源，不代表本次重新扫描了各上游网站的最新版本。

<a id="rule-evidence"></a>

## 附录A．每条规则的来源依据及竞争marker

本附录保留JSON中的编辑依据和原始定位。辅助基因的逐基因来源见附录B；同一基因被其他面板借用不产生新的独立证据。竞争marker是需要审阅的替代解释，不是单基因自动否决条件。

<a id="rule-neuronal-background"></a>

### 神经元 Neuron — `neuronal-background`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `curated-neuronal-concordance` 的依据：editorial_combination_from_curated_panel；本库提出的分组证据组合，不是作者原规则或已验证分类器；每组至少一个supported证据，仍需全表达背景及竞争谱系核验。RBFOX3不是必要的单一门槛。
- 辅助用途：NRGN adds supporting neuronal context from Wang 2024 Methods; it does not replace either existing core group or prove a transmitter identity. Other core-group genes provide concordance, not independent validation.
- 竞争审阅 `coherent_oligodendroglial`：SOX10、PDGFRA、PLP1、MBP、MOG；检查少突/OPC成套程序；零散髓鞘RNA不单独否决神经元。
- 竞争审阅 `coherent_astroglial`：AQP4、GJA1、ALDH1L1、SLC1A2；比较星形胶质背景，审查同细胞共表达、环境RNA及混合簇。
- 竞争审阅 `coherent_immune_or_vascular`：TYROBP、DOCK8、CD163、MRC1、CLDN5、PECAM1、PDGFRB、CSPG4；分别按免疫、内皮和周细胞面板检查，而不是把这八个基因混成一个布尔排除集。
- 面板来源 [S4](#ref-s4)：RBFOX3、MAP2、SYP、TUBB3；[ScTypeDB_full.xlsx; Excel row 113; Brain/Mature neurons](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx)。
- 面板来源 [S1](#ref-s1)：RBFOX3；[Human_adult/Class/NEUR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/NEUR.md)。
- 面板来源 [S5](#ref-s5)：SNAP25、STMN2；[Selected Neurons rows inspected 2026-10-14; species column Mm Hs; no specificity validation](https://panglaodb.se/markers.html?cell_type=%27Neurons%27)。
- 面板来源 [S3](#ref-s3)：NRGN；[Methods: Cluster cell-type annotation; NRGN used in major neuronal annotation](https://pmc.ncbi.nlm.nih.gov/articles/PMC10780895/)。

<a id="rule-da-core"></a>

### 多巴胺能神经元 DA — `da-core`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `kamath-da-triad` 的依据：source_positive_combination:kamath_2022；保留Kamath成人黑质DA三联证据；跨脑区使用需匹配当地DA参考。作者簇级证据不能改成每个细胞三个基因UMI均大于0。
- 核心路径 `siletti-da-triad` 的依据：source_positive_combination:siletti_rules:Human_adult/Neurotransmission/NT-DA.md；保留Siletti的独立来源路径；两条路径是OR关系，不要求四个基因同时检出。
- 辅助用途：在采用另一条路径时提供互补合成/囊泡证据；不是独立验证，也不能替代缺失的TH或SLC6A3。
- 竞争审阅 `noradrenergic`：DBH、TH、DDC；成套去甲肾上腺素证据是DA的主要竞争解释；单个DBH弱信号先核查来源。
- 竞争审阅 `adrenergic`：PNMT、DBH、TH、DDC；完整PNMT相关合成程序需比较肾上腺素能身份。
- 竞争审阅 `additional_transmitter`：GAD1、GAD2、SLC32A1、SLC17A6、SLC17A7、SLC17A8；审查混合群、同细胞递质共程序与污染；共程序不自动否决DA，也不直接证明功能性共释放。
- 面板来源 [S2](#ref-s2)：TH、SLC6A3、SLC18A2；[Results: A molecular taxonomy of human SNpc DA neurons; Extended Data Fig1i,j](https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/)。
- 面板来源 [S1](#ref-s1)：TH、DDC、DBH、PNMT；[Human_adult/Neurotransmission/NT-ADR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-ADR.md)。
- 面板来源 [S1](#ref-s1)：TH、DDC、SLC6A3；[Human_adult/Neurotransmission/NT-DA.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-DA.md)。
- 面板来源 [S1](#ref-s1)：TH、DDC、DBH；[Human_adult/Neurotransmission/NT-NOR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-NOR.md)。

<a id="rule-gaba-core"></a>

### GABA能神经元 — `gaba-core`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `siletti-gaba1` 的依据：source_positive_combination:siletti_rules:Human_adult/Neurotransmission/NT-GABA1.md；原规则另有-SLC6A5；其语义保存在冲突审阅中，不将未检出等同真阴性。
- 核心路径 `siletti-gaba2` 的依据：source_positive_combination:siletti_rules:Human_adult/Neurotransmission/NT-GABA2.md；GAD2路径可替代GAD1路径，是作者的替代规则，不是本库临时补救。
- 辅助用途：两种GAD同时支持可增强合成程序一致性；第二种GAD不能在本规则中替代SLC32A1。
- 竞争审阅 `glycinergic_or_cotransmitter`：SLC6A5、SLC32A1；SLC6A5是原GABA规则的阴性标志，但GABA/甘氨酸共程序可存在；区分同细胞证据和混簇，不能机械排除。
- 竞争审阅 `glutamatergic_or_mixed`：SLC17A6、SLC17A7、SLC17A8；检查递质共程序、不同细胞混合和环境RNA，不将单个转运体直接视为双细胞。
- 面板来源 [S1](#ref-s1)：GAD1、SLC32A1、SLC6A5；[Human_adult/Neurotransmission/NT-GABA1.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-GABA1.md)。
- 面板来源 [S1](#ref-s1)：GAD2、SLC32A1、SLC6A5；[Human_adult/Neurotransmission/NT-GABA2.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-GABA2.md)。

<a id="rule-glut-vglut1"></a>

### SLC17A7相关谷氨酸能神经元 — `glut-vglut1`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `siletti-vglut1` 的依据：source_positive_combination:siletti_rules:Human_adult/Neurotransmission/NT-VGLUT1.md；单转运体来源规则只构成必要证据入口；High还需要父级、匹配的整体表达背景和竞争类型检查。
- 辅助用途：确认神经元背景，不当作谷氨酸能特异性补救基因；与父级证据不独立。
- 竞争审阅 `GABA_or_glycine`：GAD1、GAD2、SLC32A1、SLC6A5；逐程序核验递质冲突或共程序，不能合并成单基因排除阈值。
- 竞争审阅 `monoaminergic_or_cholinergic`：TH、DDC、SLC6A3、CHAT、SLC5A7；有其他完整递质程序时检查同细胞共表达与群内异质性。
- 面板来源 [S1](#ref-s1)：SLC17A7；[Human_adult/Neurotransmission/NT-VGLUT1.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-VGLUT1.md)。

<a id="rule-glut-vglut2"></a>

### SLC17A6相关谷氨酸能神经元 — `glut-vglut2`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `siletti-vglut2` 的依据：source_positive_combination:siletti_rules:Human_adult/Neurotransmission/NT-VGLUT2.md；来源单转运体规则不是独立充分判定条件；High必须结合父级与匹配整体背景。
- 辅助用途：提供神经元背景，不替代SLC17A6，也不能与父级重复计为独立验证。
- 竞争审阅 `GABA_or_glycine`：GAD1、GAD2、SLC32A1、SLC6A5；核查各递质程序在相同细胞中的关系及群内混合。
- 竞争审阅 `monoaminergic_or_cholinergic`：TH、DDC、SLC6A3、CHAT、SLC5A7；DA等类型可出现额外递质程序；不能看到SLC17A6就覆盖已支持的父类型。
- 面板来源 [S1](#ref-s1)：SLC17A6；[Human_adult/Neurotransmission/NT-VGLUT2.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-VGLUT2.md)。

<a id="rule-glycinergic"></a>

### 甘氨酸能神经元 — `glycinergic`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `siletti-gly` 的依据：source_positive_combination:siletti_rules:Human_adult/Neurotransmission/NT-GLY.md；保留摄取/囊泡双证据；SLC32A1也是GABA共用转运体。
- 辅助用途：神经元背景支持；不能在缺少SLC6A5时替代甘氨酸相关核心。
- 竞争审阅 `GABA_or_GABA_glycine_coprogram`：GAD1、GAD2、SLC32A1；比较GABA共程序；并存可有生物学解释，不要求互斥，也不从簇均值断言共释放。
- 竞争审阅 `glutamatergic_or_mixed`：SLC17A6、SLC17A7；审阅同细胞归属、混合和污染。
- 面板来源 [S1](#ref-s1)：SLC6A5、SLC32A1；[Human_adult/Neurotransmission/NT-GLY.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-GLY.md)。

<a id="rule-serotonergic"></a>

### 5-HT能神经元 — `serotonergic`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `siletti-ser` 的依据：source_positive_combination:siletti_rules:Human_adult/Neurotransmission/NT-SER.md；成人脑5-HT核心三联；不把TPH1静默改名成TPH2或作为自动替代。
- 辅助用途：单胺囊泡背景的非特异支持，不能单独区分5-HT、DA、NE，也不能替代三联核心。
- 竞争审阅 `catecholaminergic`：TH、SLC6A3、DBH、PNMT；结合DDC等完整程序比较儿茶酚胺类型；DDC为共享证据不能单独区分。
- 竞争审阅 `additional_transmitter`：SLC17A6、SLC17A8、GAD1、GAD2、SLC32A1；审阅共程序/混群和细胞内一致性，不要求转录程序绝对互斥。
- 面板来源 [S1](#ref-s1)：TPH2、FEV、DDC；[Human_adult/Neurotransmission/NT-SER.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-SER.md)。

<a id="rule-cholinergic"></a>

### 胆碱能神经元 — `cholinergic`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `siletti-chol` 的依据：source_positive_combination:siletti_rules:Human_adult/Neurotransmission/NT-CHOL.md；保留Siletti双基因来源规则；SLC18A3是ScType来源的补充证据，本版不宣称它已被验证可替代SLC5A7。
- 辅助用途：提供囊泡转运的互补证据；不得由其单独定义胆碱能身份。
- 竞争审阅 `other_transmitter_or_mixed`：GAD1、GAD2、SLC32A1、SLC17A6、SLC17A7、SLC17A8、TH、SLC6A3；按各竞争面板核验；真实共程序、混簇、污染需要区分，不能凭单marker否决。
- 面板来源 [S4](#ref-s4)：CHAT、SLC18A3；[ScTypeDB_full.xlsx; Excel row 106; Brain/Cholinergic neurons](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx)。
- 面板来源 [S1](#ref-s1)：CHAT、SLC5A7；[Human_adult/Neurotransmission/NT-CHOL.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-CHOL.md)。

<a id="rule-noradrenergic"></a>

### 去甲肾上腺素能神经元 — `noradrenergic`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `siletti-nor` 的依据：source_positive_combination:siletti_rules:Human_adult/Neurotransmission/NT-NOR.md；DBH结合儿茶酚胺合成背景；TH单独并不区分DA与NE。
- 辅助用途：共享单胺囊泡支持，不是NE特异证据，不替代DBH。
- 竞争审阅 `adrenergic`：PNMT、DBH、TH、DDC；PNMT与整套合成背景构成肾上腺素能竞争解释；单个低值先审阅。
- 竞争审阅 `dopaminergic`：TH、SLC6A3、SLC18A2；结合DBH、全表达背景和解剖核验DA/NE；共享核心不能重复计作独立证据。
- 面板来源 [S1](#ref-s1)：DBH、TH、DDC；[Human_adult/Neurotransmission/NT-NOR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-NOR.md)。

<a id="rule-adrenergic"></a>

### 肾上腺素能神经元 — `adrenergic`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `siletti-adr` 的依据：source_positive_combination:siletti_rules:Human_adult/Neurotransmission/NT-ADR.md；肾上腺素合成四联来源组合；单PNMT不足，且需要稀有类型的匹配解剖/参考核验。
- 辅助用途：共享单胺囊泡支持，不提供ADR特异性或补救缺失PNMT。
- 竞争审阅 `noradrenergic_alternative`：DBH、TH、DDC；前三个共享核心只能支持NE/ADR背景；PNMT证据不可靠时不能把NE提升为ADR。
- 竞争审阅 `dopaminergic_or_mixed`：SLC6A3、TH、SLC18A2；检查其他儿茶酚胺身份、混群及同细胞一致性。
- 面板来源 [S1](#ref-s1)：PNMT、DBH、TH、DDC；[Human_adult/Neurotransmission/NT-ADR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-ADR.md)。

<a id="rule-histaminergic"></a>

### 组胺能神经元候选 — `histaminergic`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`Moderate`。
- 核心路径 `siletti-hdc-provisional` 的依据：source_positive_marker:siletti_rules:Human_adult/Neurotransmission/NT-HDC.md；只有单HDC来源marker，当前库缺少可核验的类型特异补充组合；身份上限Moderate。
- 辅助用途：确认神经元背景，不能补成组胺能特异性证据或解除本版置信度上限。
- 竞争审阅 `non_neuronal_HDC_or_source_uncertainty`：TYROBP、DOCK8、CD163、MRC1；有免疫背景或HDC来源不清时检查非神经元来源；本库不完整覆盖所有HDC阳性非神经元，缺少这些基因不能证明排除。
- 面板来源 [S1](#ref-s1)：HDC；[Human_adult/Neurotransmission/NT-HDC.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-HDC.md)。

<a id="rule-cortical-pvalb"></a>

### 皮层PVALB相关中间神经元 — `cortical-pvalb`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `cortical-pvalb-context` 的依据：Siletti INT-PVALB 的已溯源人工整理子集；并非完整原作者分类器。；各项表示本次评估单位的可信表达证据；不要求每个原始单细胞全部检出。
- 辅助用途：加强抑制性神经元背景；不能替换 PVALB 或皮层来源证据。
- 竞争审阅 `competing_cortical_interneuron_program`：SST、VIP、ADARB2、LAMP5；检查竞争亚型的成套证据和是否混合多个细胞群；单个共表达基因不能否决。
- 面板来源 [S1](#ref-s1)：PVALB、LHX6、DLX1、GAD2、FOXG1；[Human_adult/Subtype/Neuronal/INT-PVALB.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-PVALB.md)。

<a id="rule-cortical-sst"></a>

### 皮层SST相关中间神经元 — `cortical-sst`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `cortical-sst-context` 的依据：Siletti INT-SST 的已溯源人工整理子集。；保留来源中的 ADARB2 阴性语境供竞争类型审阅，不把未检出当作可靠阴性。
- 辅助用途：支持抑制性背景与 SST 表达；肽程序与皮层身份使用同一 SST 证据，不能算独立验证。
- 竞争审阅 `ADARB2_associated_or_competing_cortical_program`：ADARB2、VIP、LAMP5、PVALB；来源中的 ADARB2 阴性用于特定定义，不是所有 SST 生物学的普适排除；必须比较成套竞争程序。
- 面板来源 [S1](#ref-s1)：SST、LHX6、DLX1、GAD2、FOXG1、ADARB2；[Human_adult/Subtype/Neuronal/INT-SST.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-SST.md)。

<a id="rule-cortical-vip"></a>

### 皮层VIP相关中间神经元 — `cortical-vip`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `cortical-vip-context` 的依据：Siletti INT-VIP 的已溯源人工整理子集。；评估组合在当前群及成员中的一致性；不能将不同细胞的零散阳性相加。
- 辅助用途：支持神经元/抑制性背景；VIP 肽面板不是独立身份验证。
- 竞争审阅 `competing_LHX6_or_LAMP5_associated_program`：LHX6、PVALB、SST、LAMP5；比较相近皮层类别、混合细胞及参考边界；共享基因不是自动否决。
- 面板来源 [S1](#ref-s1)：VIP、ADARB2、CXCL14、DLX1、GAD2、FOXG1；[Human_adult/Subtype/Neuronal/INT-VIP.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-VIP.md)。

<a id="rule-cortical-lamp5"></a>

### 皮层LAMP5相关中间神经元 — `cortical-lamp5`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `cortical-lamp5-context` 的依据：Siletti INT-LAMP5 的已溯源人工整理子集。；适用于来源所定义的 LAMP5 相关语境；不把它扩展为全部 LAMP5 阳性细胞。
- 辅助用途：支持抑制性背景，不替换亚型组合。
- 竞争审阅 `LHX6_associated_or_other_cortical_program`：LHX6、PVALB、SST、VIP；来源 LHX6 阴性需要在对应参考分类中解释；存在 LAMP5/LHX6 相关其他语境时应重新比较，不能单基因否决。
- 面板来源 [S1](#ref-s1)：LAMP5、ADARB2、CXCL14、GAD2、FOXG1、LHX6；[Human_adult/Subtype/Neuronal/INT-LAMP5.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-LAMP5.md)。

<a id="rule-striatal-d1"></a>

### 纹状体D1相关中型棘状神经元 — `striatal-d1`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `d1-striatal-context` 的依据：Siletti MSN-D1 的已溯源人工整理子集。；DRD1 是受体相关亚型证据；神经元/抑制性及纹状体背景应共同成立。
- 辅助用途：支持抑制性神经元父级；不以受体表达替代 MSN 背景。
- 竞争审阅 `D2_associated_or_mixed_MSN_program`：DRD2；比较 DRD2 相关群及同细胞共表达，不能把单个 DRD2 检出视为否决或自动宣布 D1/D2 混合型。
- 竞争审阅 `DA_synthesis_transport_identity`：TH、SLC6A3、SLC18A2；需要区分接收多巴胺信号的 MSN 和具有 DA 递质程序的神经元；成套冲突可能提示混群。
- 面板来源 [S1](#ref-s1)：DRD1、GPR88、RGS9、FOXP1、SLC32A1、FOXG1；[Human_adult/Subtype/Neuronal/MSN-D1.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D1.md)。

<a id="rule-striatal-d2"></a>

### 纹状体D2相关中型棘状神经元 — `striatal-d2`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `d2-striatal-context` 的依据：Siletti MSN-D2 的已溯源人工整理子集。；DRD2 单独不能确立 MSN，更不能表明该细胞合成多巴胺。
- 辅助用途：支持抑制性父级；不代替纹状体/亚型组合。
- 竞争审阅 `D1_associated_or_mixed_MSN_program`：DRD1；比较 D1 相关群和同细胞表达关系；不以 DRD1 单基因否决。
- 竞争审阅 `DA_synthesis_transport_identity`：TH、SLC6A3、SLC18A2；成套 DA 合成/转运证据提示需要比较不同细胞身份，而不是把 DRD2 当 DA marker。
- 面板来源 [S1](#ref-s1)：DRD2、GPR88、RGS9、FOXP1、SLC32A1、FOXG1；[Human_adult/Subtype/Neuronal/MSN-D2.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D2.md)。

<a id="rule-cerebellar-purkinje"></a>

### 小脑Purkinje相关神经元 — `cerebellar-purkinje`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `purkinje-combination` 的依据：Siletti CB-PURK 的已溯源组合；原规则理由含小鼠小脑研究。；成人查询的物种是人，不等于所有上游证据已经得到人类验证。
- 辅助用途：核对神经元及抑制性背景；PVALB 不是皮层专属或独有 Purkinje 标志。
- 竞争审阅 `cerebellar_granule_or_mixed_program`：CBLN1、CBLN3、GABRA6；审阅完整颗粒细胞程序与 PCP2/SKOR2 组合的细胞归属，区分混群和真实共表达。
- 面板来源 [S1](#ref-s1)：PCP2、SKOR2、PVALB、GAD2；[Human_adult/Subtype/Neuronal/CB-PURK.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/CB-PURK.md)。

<a id="rule-cerebellar-granule"></a>

### 小脑颗粒细胞相关神经元 — `cerebellar-granule`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `cerebellar-granule-combination` 的依据：Siletti CB-GRAN 的已溯源组合。；来源类别字段含 Glial 矛盾，不能把该元数据直接复制为本细胞的谱系。
- 辅助用途：另行核验谷氨酸相关程序；此面板的亚型结论不能自动赋予未独立评估的递质 High。
- 竞争审阅 `Purkinje_or_GABA_associated_program`：PCP2、SKOR2、GAD1、GAD2、SLC32A1；GABRA6 是受体证据，不因名字含 GABA 就视为 GABA 合成；审阅真正 GABA/Purkinje 程序。
- 竞争审阅 `oligodendroglial_program`：SOX10、MOG、MBP；谱系矛盾需由表达证据解决，不能根据原文件 Glial 字段强行命名。
- 面板来源 [S1](#ref-s1)：CBLN1、CBLN3、GABRA6；[Human_adult/Subtype/Neuronal/CB-GRAN.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/CB-GRAN.md)。

<a id="rule-da-sox6"></a>

### DA内SOX6相关表达特征 — `da-sox6`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`program`；当前置信度上限：`High`。
- 核心路径 `sox6-in-confirmed-da` 的依据：Kamath 人类 SNpc DA 分支的 SOX6 相关证据。；此单基因路线只描述已确认 DA 细胞内的程序，不建立新的独立身份。
- 辅助用途：维持 DA 父级；SOX6 缺失时这些基因不能补成 SOX6 程序。
- 竞争审阅 `alternative_DA_branch_or_mixture`：CALB1；比较 DA 内 SOX6/CALB1 的联合分布，不规定互斥；共表达也不自动否决。
- 竞争审阅 `other_catecholaminergic_identity`：DBH、PNMT；成套非 DA 儿茶酚胺证据可能使 DA 父级失效，必须先解决父级冲突。
- 面板来源 [S2](#ref-s2)：SOX6；[Fig1e and Results: SOX6/CALB1 DA branches](https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/)。

<a id="rule-da-calb1"></a>

### DA内CALB1相关表达特征 — `da-calb1`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`program`；当前置信度上限：`High`。
- 核心路径 `calb1-in-confirmed-da` 的依据：Kamath 人类 SNpc DA 分支的 CALB1 相关证据。；CALB1 不是 DA 专属基因，路线必须建立在 DA 父级之上。
- 辅助用途：支持 DA 身份；这些基因不能替代 CALB1 程序证据。
- 竞争审阅 `alternative_DA_branch_or_mixture`：SOX6；检查两种程序的细胞级分布及参考语境，不能机械设为互斥。
- 竞争审阅 `other_catecholaminergic_identity`：DBH、PNMT；完整竞争身份程序要求重新审阅 DA 父级。
- 面板来源 [S2](#ref-s2)：CALB1；[Fig1e and Results: SOX6/CALB1 DA branches](https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/)。

<a id="rule-da-sox6-agtr1"></a>

### DA内SOX6/AGTR1亚群相关特征 — `da-sox6-agtr1`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`program`；当前置信度上限：`High`。
- 核心路径 `sox6-agtr1-in-confirmed-da` 的依据：Kamath SOX6_AGTR1 亚群的已溯源简化相关程序。；两个基因的程序一致性不是完整亚型参考映射；不重命名为已确认的 Kamath SOX6_AGTR1 identity。
- 辅助用途：核查父级与分支背景；同源 SOX6 证据不能重复计算为独立验证。
- 竞争审阅 `other_DA_program_or_mixture`：CALB1、TMEM200A；比较其他 DA 程序与细胞组成；不以一个共同表达基因否决或硬划分互斥亚群。
- 面板来源 [S2](#ref-s2)：SOX6、AGTR1；[Results/Fig3: SOX6_AGTR1 DA subtype; not a query vulnerability claim](https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/)。

<a id="rule-da-calb1-tmem200a"></a>

### DA内CALB1/TMEM200A亚群相关特征 — `da-calb1-tmem200a`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`program`；当前置信度上限：`High`。
- 核心路径 `calb1-tmem200a-in-confirmed-da` 的依据：Kamath CALB1_TMEM200A 亚群的已溯源简化相关程序。；本组合保留为 program，不能代替完整人类 SNpc 参考的亚型鉴别。
- 辅助用途：支持 DA 父级和 CALB1 分支；不能重复计算同一 CALB1 证据或用父级基因替代 TMEM200A。
- 竞争审阅 `other_DA_program_or_mixture`：SOX6、AGTR1；核对不同 DA 程序细胞级关系；共同检出不是单基因否决规则。
- 面板来源 [S2](#ref-s2)：CALB1、TMEM200A；[Results/Fig3: CALB1_TMEM200A DA subtype](https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/)。

<a id="rule-rit2-enriched-program"></a>

### RIT2富集神经元特征 — `rit2-enriched-program`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/study-programs.json)；结论类型：`program`；当前置信度上限：`High`。
- 核心路径 `wang-rit2-enrichment` 的依据：source_expression_association:wang_2024; editorial_program_review_not_fixed_type；Wang原文的RIT2富集神经元有RNA、蛋白及外部队列支持；本规则只审阅程序，要求相对可比神经元富集、可信群体归属和供者证据，不按RIT2单阳性建立固定类型。
- 辅助用途：核验神经元背景；NRGN仅辅助。GALNTL6单独评估，不要求两基因共阳性，不由TH未检出推断TH生物学阴性。
- 竞争审阅 `neuronal_vs_oligodendroglial_source`：PLP1、MBP、MOG、SOX10；原文RIT2也可在非神经元群出现；必须确认神经元归属和群内一致性。单个髓鞘转录本不否决程序。
- 面板来源 [S3](#ref-s3)：RIT2；[Fig1C/Fig2; TableS2 C9; study-associated neuronal enrichment](https://pmc.ncbi.nlm.nih.gov/articles/PMC10780895/)。

<a id="rule-galntl6-associated-program"></a>

### GALNTL6相关神经元特征 — `galntl6-associated-program`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/study-programs.json)；结论类型：`program`；当前置信度上限：`High`。
- 核心路径 `wang-galntl6-association` 的依据：source_expression_association:wang_2024; editorial_program_review_not_fixed_type；作者Fig1C/Fig4/TableS2显示C6及部分神经元亚群的GALNTL6表达；这是表达关联来源，不是已验证的固定类型特异性。
- 辅助用途：仅核验神经元背景。RIT2独立评估；没有预定义RIT2+GALNTL6双核心，也不由GALNTL6推断DA身份。
- 竞争审阅 `neuronal_vs_oligodendroglial_source`：PLP1、MBP、MOG、SOX10；核验信号来源、环境RNA和混群；群体富集与同细胞共表达分别描述。
- 面板来源 [S3](#ref-s3)：GALNTL6；[Fig1C/Fig4B/E/G; TableS2 C6 and subclusters; distinct from RIT2 program](https://pmc.ncbi.nlm.nih.gov/articles/PMC10780895/)。

<a id="rule-glut-vglut3"></a>

### SLC17A8相关表达特征 — `glut-vglut3`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`program`；当前置信度上限：`High`。
- 核心路径 `siletti-vglut3-program` 的依据：source_positive_marker:siletti_rules:Human_adult/Neurotransmission/NT-VGLUT3.md;editorial_claim_restriction；保留来源marker，但把本库可支持的结论限制为程序，不复用来源名称推成排他的谷氨酸能类型。
- 辅助用途：确认信号来自可信神经元单位；只支持背景，不替代核心。
- 竞争审阅 `multiple_transmitter_context`：GAD1、GAD2、SLC32A1、CHAT、SLC5A7、TPH2、FEV、DDC；这些程序与SLC17A8不必互斥；目的为确定表达归属及排查混合，不把共程序当排除项。
- 面板来源 [S1](#ref-s1)：SLC17A8；[Human_adult/Neurotransmission/NT-VGLUT3.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-VGLUT3.md)。

<a id="rule-peptide-hcrt"></a>

### HCRT相关神经肽特征 — `peptide-hcrt`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`program`；当前置信度上限：`High`。
- 核心路径 `hcrt-expression-program` 的依据：Siletti NP-HCRT 的神经肽表达程序。；单基因程序证据不是单基因身份规则。
- 辅助用途：核查信号归属神经元；泛神经元证据不能替代 HCRT。
- 竞争审阅 `PMCH_associated_signal_or_mixed_peptide_population`：PMCH；HCRT/PMCH 在同簇出现需核查不同细胞群、环境 RNA 或真实共表达；共现不自动证明一种共表达类型。
- 面板来源 [S1](#ref-s1)：HCRT；[Neuropeptides/NP-HCRT.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Neuropeptides/NP-HCRT.md)。

<a id="rule-peptide-pmch"></a>

### PMCH相关神经肽特征 — `peptide-pmch`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`program`；当前置信度上限：`High`。
- 核心路径 `pmch-expression-program` 的依据：Siletti NP-PMCH 的神经肽表达程序。；程序存在与细胞身份是两种不同结论。
- 辅助用途：支持神经元信号归属，不能替代 PMCH。
- 竞争审阅 `HCRT_associated_signal_or_mixed_peptide_population`：HCRT；审阅同簇共现是否来自不同细胞、环境污染或真实共表达，不能自动命名共肽类型。
- 面板来源 [S1](#ref-s1)：PMCH；[Neuropeptides/NP-PMCH.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Neuropeptides/NP-PMCH.md)。

<a id="rule-peptide-npy"></a>

### NPY相关神经肽特征 — `peptide-npy`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`program`；当前置信度上限：`High`。
- 核心路径 `npy-expression-program` 的依据：Siletti NP-NPY 的神经肽表达程序。；NPY 表达不是唯一神经元类型定义。
- 辅助用途：支持神经元信号归属；不能由父级或另一种肽代替 NPY。
- 竞争审阅 `non_neuronal_signal_assignment`：SOX10、MOG、AQP4、ALDH1L1；若肽信号落在具有完整非神经元谱系程序的对象，复核父级、混合细胞和环境 RNA；单个胶质转录本不否决。
- 面板来源 [S1](#ref-s1)：NPY；[Neuropeptides/NP-NPY.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Neuropeptides/NP-NPY.md)。

<a id="rule-peptide-sst"></a>

### SST相关神经肽特征 — `peptide-sst`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`program`；当前置信度上限：`High`。
- 核心路径 `sst-expression-program` 的依据：Siletti NP-SST 的神经肽表达程序。；SST 肽程序与 cortical-sst 皮层身份路线分开评估。
- 辅助用途：确认神经元背景；不能仅从 SST 肽表达补成 GABA 或皮层中间神经元。
- 竞争审阅 `non_neuronal_signal_assignment`：SOX10、MOG、AQP4、ALDH1L1；谱系程序与肽信号归属矛盾时复核混群及污染，不以单个共享基因否决。
- 面板来源 [S1](#ref-s1)：SST；[Neuropeptides/NP-SST.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Neuropeptides/NP-SST.md)。

<a id="rule-peptide-vip"></a>

### VIP相关神经肽特征 — `peptide-vip`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`program`；当前置信度上限：`High`。
- 核心路径 `vip-expression-program` 的依据：Siletti NP-VIP 的神经肽表达程序。；VIP 肽程序可跨脑区记录，皮层身份须另走 cortical-vip。
- 辅助用途：核查神经元信号来源；泛神经元与 VIP 单基因不足以补成皮层亚型。
- 竞争审阅 `non_neuronal_signal_assignment`：SOX10、MOG、AQP4、ALDH1L1；完整竞争谱系程序要求复核细胞归属和技术解释，单个胶质转录本不构成自动否决。
- 面板来源 [S1](#ref-s1)：VIP；[Neuropeptides/NP-VIP.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Neuropeptides/NP-VIP.md)。

<a id="rule-immature-program"></a>

### 未成熟/发育相关表达特征 — `immature-program`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/contextual.json)；结论类型：`program`；当前置信度上限：`Moderate`。
- 核心路径 `developmental-associated-combination` 的依据：ScType Brain/Immature neurons 整理组合；原行未给出年龄、物种和脑区细分。；此组合不是经过成人脑神经发生验证的路线。
- 辅助用途：确认神经元相关背景并记录成熟度异质性；成熟程序共现不是单基因否决，也不能补成神经发生证据。
- 竞争审阅 `alternative_lineage_or_technical_mixture`：SOX10、PDGFRA、AQP4、ALDH1L1；检查前体/胶质背景、混群和技术解释；不能从 DCX 或 NEUROD1 单独定为新生神经元。
- 面板来源 [S4](#ref-s4)：DCX、NEUROD1、TUBB3；[ScTypeDB_full.xlsx; Excel row 111; Brain/Immature neurons](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx)。

<a id="rule-oligo-guard"></a>

### 少突胶质细胞 — `oligo-guard`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `siletti-oligo-positive` 的依据：source_positive_combination:siletti_rules:Human_adult/Class/OLIGO.md；原规则另有-PDGFRA，转入OPC竞争审阅；多个髓鞘RNA可来自环境污染，来源三联仍不是自动充分条件。
- 辅助用途：提供少突谱系互补背景，与OPC共享；不能由SOX10单独区分成熟少突和OPC。
- 竞争审阅 `OPC_or_transition`：SOX10、PDGFRA；核查OPC/成熟过渡背景，PDGFRA单个值不是绝对否决。
- 竞争审阅 `neuronal_with_ambient_myelin`：SNAP25、SYP、MAP2、RBFOX3；若完整神经元程序占优，髓鞘基因不能覆盖神经元身份；检查环境RNA与双细胞。
- 面板来源 [S1](#ref-s1)：PLP1、MBP、MOG、PDGFRA；[Human_adult/Class/OLIGO.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/OLIGO.md)。
- 面板来源 [S4](#ref-s4)：MBP、MOG、SOX10；[ScTypeDB_full.xlsx; Excel row 122; Brain/Oligodendrocytes](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx)。

<a id="rule-opc-guard"></a>

### 少突胶质前体细胞 OPC — `opc-guard`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `siletti-opc` 的依据：source_positive_combination:siletti_rules:Human_adult/Class/OPC.md；少突谱系与前体组合；不纳入LHFPL3单基因替代规则。
- 辅助用途：非特异的辅助背景，来源于库中周细胞面板且与OPC共享；不能单独判OPC或补齐SOX10/PDGFRA。
- 竞争审阅 `mature_oligodendroglial`：PLP1、MBP、MOG；比较成熟/过渡少突；部分髓鞘表达并非单基因否决。
- 竞争审阅 `pericytic`：PDGFRB、CSPG4；CSPG4共享，需少突谱系与血管壁整体背景区分。
- 竞争审阅 `neuronal`：SNAP25、SYP、MAP2、RBFOX3；完整神经元程序构成竞争解释；不能因单个所谓OPC marker覆盖神经元身份。
- 面板来源 [S1](#ref-s1)：SOX10、PDGFRA；[Human_adult/Class/OPC.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/OPC.md)。

<a id="rule-astro-guard"></a>

### 星形胶质细胞 — `astro-guard`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `siletti-astro-positive` 的依据：source_positive_combination:siletti_rules:Human_adult/Class/ASTRO.md；原规则另有-FOXJ1，保留为室管膜/纤毛程序审阅。
- 辅助用途：ScType来源辅助背景；可以支持星形胶质一致性，但本版未验证其替代AQP4/GJA1的组合。
- 竞争审阅 `ependymal_ciliated`：FOXJ1；FOXJ1是来源情境阴性；本库未提供完整室管膜面板，应以匹配参考核查而非单gene否决。
- 竞争审阅 `neuronal_or_oligodendroglial`：SNAP25、MAP2、SOX10、PLP1、MBP、MOG；分别比较神经元和少突谱系背景，不把组合列表当互斥布尔公式。
- 面板来源 [S4](#ref-s4)：AQP4、ALDH1L1、SLC1A2；[ScTypeDB_full.xlsx; Excel row 105; Brain/Astrocytes](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx)。
- 面板来源 [S1](#ref-s1)：AQP4、GJA1、FOXJ1；[Human_adult/Class/ASTRO.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/ASTRO.md)。

<a id="rule-myeloid-guard"></a>

### 广义髓系细胞，亚型未定 — `myeloid-guard`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `curated-broad-myeloid` 的依据：editorial_subset_and_label_restriction:siletti_rules:Human_adult/Class/MGL.md；只采用来源正向背景并限制到广义髓系候选；原作者Microglia名称及未完整收录的阴性组合不能自动转移。
- 辅助用途：当前小面板没有可声明为髓系特异替代的辅助组合；需匹配全表达免疫参考补足区分能力，另留溯源。
- 竞争审阅 `macrophage_subtype_context`：CD163、MRC1、F13A1；是髓系内部的巨噬细胞/BAM相关细分方向，不是排除广义髓系；不能自动命名小胶质。
- 竞争审阅 `neuronal_or_vascular`：SNAP25、MAP2、CLDN5、PECAM1、PDGFRB、CSPG4；比较神经元和血管壁候选及混合来源；TYROBP/DOCK8也不足以覆盖全部其他免疫竞争类型。
- 面板来源 [S1](#ref-s1)：TYROBP、DOCK8；[Human_adult/Class/MGL.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/MGL.md)。

<a id="rule-macrophage-guard"></a>

### 巨噬细胞相关类型 — `macrophage-guard`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `siletti-mac` 的依据：source_positive_combination:siletti_rules:Human_adult/Class/MAC.md；保留巨噬细胞相关三联；不能仅靠这些基因决定边界位置或细胞起源。
- 辅助用途：广义髓系/免疫背景支持，不是巨噬细胞特异验证，也不区分微胶质与BAM。
- 竞争审阅 `microglial_or_other_myeloid_alternative`：TYROBP、DOCK8；共享髓系背景不排除任何一方；必须用匹配完整参考比较小胶质及其他髓系候选，本库这两个基因不能完成区分。
- 竞争审阅 `vascular_or_neuronal_mixture`：CLDN5、PECAM1、PDGFRB、CSPG4、SNAP25、MAP2；检查血管邻近细胞混合、环境RNA和双细胞，不由空间邻近推成BAM。
- 面板来源 [S1](#ref-s1)：CD163、MRC1、F13A1；[Human_adult/Class/MAC.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/MAC.md)。

<a id="rule-endothelial-guard"></a>

### 内皮细胞 — `endothelial-guard`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `siletti-endo` 的依据：source_positive_combination:siletti_rules:Human_adult/Class/ENDO.md；内皮三联组合；FLT1单独不具备足够特异性。
- 辅助用途：当前库没有独立内皮辅助集合；匹配整体血管参考提供外部支持并单独溯源。
- 竞争审阅 `mural_pericytic`：PDGFRB、CSPG4、MYH11；血管壁与内皮应区分；相邻细胞混合不能视作单一内皮身份。
- 竞争审阅 `immune_or_neuronal`：TYROBP、DOCK8、CD163、MRC1、SNAP25、MAP2；审阅免疫、神经元竞争程序及环境RNA。
- 面板来源 [S1](#ref-s1)：CLDN5、PECAM1、FLT1；[Human_adult/Class/ENDO.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/ENDO.md)。

<a id="rule-pericyte-guard"></a>

### 周细胞相关类型 — `pericyte-guard`

- 规则文件：[冻结JSON](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/rules/identity.json)；结论类型：`identity`；当前置信度上限：`High`。
- 核心路径 `siletti-per-positive` 的依据：source_positive_combination:siletti_rules:Human_adult/Class/PER.md；原规则另有-MYH11；该来源阴性属于血管壁分型的情境审阅，不将缺测或单个值当自动排除。
- 辅助用途：本库没有可独立补齐的周细胞辅助组合；High依赖有溯源的整体血管壁参考核验。
- 竞争审阅 `oligodendrocyte_precursor`：SOX10、PDGFRA、CSPG4；CSPG4共享，需核验OPC和周细胞整体背景；不可由CSPG4单阳性定名。
- 竞争审阅 `smooth_muscle_or_mural_transition`：MYH11；MYH11情境提示平滑肌/过渡血管壁类型；本库缺完整平滑肌面板，需匹配参考。
- 竞争审阅 `endothelial`：CLDN5、PECAM1、FLT1；检查邻近内皮混入及双细胞。
- 面板来源 [S1](#ref-s1)：PDGFRB、CSPG4、MYH11；[Human_adult/Class/PER.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/PER.md)。

<a id="gene-evidence"></a>

## 附录B．逐基因、逐面板、逐来源溯源

以下131条记录与v1.3.0的`assets/marker_literature.tsv`逐条对应，覆盖77个不同基因。`positive`表示所列精选面板的阳性条目，`negative`表示情境阴性/竞争项；不等于该基因在所有规则中的固定角色。实际核心、辅助或冲突用途由附录A及机器规则决定。某行数据库论文仅提供实际采用来源，不冒称原始发现文献。

| marker gene | 来源面板 | 面板极性 | 文献 | 原文／规则位置及直接来源 | 来源物种语境 |
|---|---|---|---|---|---|
| RBFOX3 | neuronal-background | positive | [S4](#ref-s4) | [ScTypeDB_full.xlsx; Excel row 113; Brain/Mature neurons](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx) | unspecified per row; mixed-case symbols present |
| RBFOX3 | neuronal-background | positive | [S1](#ref-s1) | [Human_adult/Class/NEUR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/NEUR.md) | human; some rule justifications cite mouse studies |
| MAP2 | neuronal-background | positive | [S4](#ref-s4) | [ScTypeDB_full.xlsx; Excel row 113; Brain/Mature neurons](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx) | unspecified per row; mixed-case symbols present |
| SNAP25 | neuronal-background | positive | [S5](#ref-s5) | [Selected Neurons rows inspected 2026-10-14; species column Mm Hs; no specificity validation](https://panglaodb.se/markers.html?cell_type=%27Neurons%27) | human/mouse; filter per row |
| STMN2 | neuronal-background | positive | [S5](#ref-s5) | [Selected Neurons rows inspected 2026-10-14; species column Mm Hs; no specificity validation](https://panglaodb.se/markers.html?cell_type=%27Neurons%27) | human/mouse; filter per row |
| SYP | neuronal-background | positive | [S4](#ref-s4) | [ScTypeDB_full.xlsx; Excel row 113; Brain/Mature neurons](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx) | unspecified per row; mixed-case symbols present |
| TUBB3 | neuronal-background | positive | [S4](#ref-s4) | [ScTypeDB_full.xlsx; Excel row 113; Brain/Mature neurons](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx) | unspecified per row; mixed-case symbols present |
| TH | da-core | positive | [S2](#ref-s2) | [Results: A molecular taxonomy of human SNpc DA neurons; Extended Data Fig1i,j](https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/) | human primary; comparative animal datasets separately |
| TH | da-core | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-ADR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-ADR.md) | human; some rule justifications cite mouse studies |
| TH | da-core | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-DA.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-DA.md) | human; some rule justifications cite mouse studies |
| TH | da-core | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-NOR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-NOR.md) | human; some rule justifications cite mouse studies |
| DDC | da-core | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-ADR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-ADR.md) | human; some rule justifications cite mouse studies |
| DDC | da-core | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-DA.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-DA.md) | human; some rule justifications cite mouse studies |
| DDC | da-core | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-NOR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-NOR.md) | human; some rule justifications cite mouse studies |
| SLC6A3 | da-core | positive | [S2](#ref-s2) | [Results: A molecular taxonomy of human SNpc DA neurons; Extended Data Fig1i,j](https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/) | human primary; comparative animal datasets separately |
| SLC6A3 | da-core | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-DA.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-DA.md) | human; some rule justifications cite mouse studies |
| SLC18A2 | da-core | positive | [S2](#ref-s2) | [Results: A molecular taxonomy of human SNpc DA neurons; Extended Data Fig1i,j](https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/) | human primary; comparative animal datasets separately |
| DBH | da-core | negative | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-ADR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-ADR.md) | human; some rule justifications cite mouse studies |
| DBH | da-core | negative | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-NOR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-NOR.md) | human; some rule justifications cite mouse studies |
| PNMT | da-core | negative | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-ADR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-ADR.md) | human; some rule justifications cite mouse studies |
| GAD1 | gaba-core | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-GABA1.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-GABA1.md) | human; some rule justifications cite mouse studies |
| GAD2 | gaba-core | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-GABA2.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-GABA2.md) | human; some rule justifications cite mouse studies |
| SLC32A1 | gaba-core | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-GABA1.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-GABA1.md) | human; some rule justifications cite mouse studies |
| SLC32A1 | gaba-core | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-GABA2.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-GABA2.md) | human; some rule justifications cite mouse studies |
| SLC6A5 | gaba-core | negative | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-GABA1.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-GABA1.md) | human; some rule justifications cite mouse studies |
| SLC6A5 | gaba-core | negative | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-GABA2.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-GABA2.md) | human; some rule justifications cite mouse studies |
| SLC17A7 | glut-vglut1 | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-VGLUT1.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-VGLUT1.md) | human; some rule justifications cite mouse studies |
| SLC17A6 | glut-vglut2 | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-VGLUT2.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-VGLUT2.md) | human; some rule justifications cite mouse studies |
| SLC17A8 | glut-vglut3 | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-VGLUT3.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-VGLUT3.md) | human; some rule justifications cite mouse studies |
| SLC6A5 | glycinergic | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-GLY.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-GLY.md) | human; some rule justifications cite mouse studies |
| SLC32A1 | glycinergic | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-GLY.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-GLY.md) | human; some rule justifications cite mouse studies |
| TPH2 | serotonergic | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-SER.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-SER.md) | human; some rule justifications cite mouse studies |
| FEV | serotonergic | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-SER.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-SER.md) | human; some rule justifications cite mouse studies |
| DDC | serotonergic | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-SER.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-SER.md) | human; some rule justifications cite mouse studies |
| CHAT | cholinergic | positive | [S4](#ref-s4) | [ScTypeDB_full.xlsx; Excel row 106; Brain/Cholinergic neurons](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx) | unspecified per row; mixed-case symbols present |
| CHAT | cholinergic | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-CHOL.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-CHOL.md) | human; some rule justifications cite mouse studies |
| SLC5A7 | cholinergic | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-CHOL.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-CHOL.md) | human; some rule justifications cite mouse studies |
| SLC18A3 | cholinergic | positive | [S4](#ref-s4) | [ScTypeDB_full.xlsx; Excel row 106; Brain/Cholinergic neurons](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx) | unspecified per row; mixed-case symbols present |
| DBH | noradrenergic | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-NOR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-NOR.md) | human; some rule justifications cite mouse studies |
| TH | noradrenergic | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-NOR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-NOR.md) | human; some rule justifications cite mouse studies |
| DDC | noradrenergic | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-NOR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-NOR.md) | human; some rule justifications cite mouse studies |
| PNMT | adrenergic | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-ADR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-ADR.md) | human; some rule justifications cite mouse studies |
| DBH | adrenergic | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-ADR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-ADR.md) | human; some rule justifications cite mouse studies |
| TH | adrenergic | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-ADR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-ADR.md) | human; some rule justifications cite mouse studies |
| DDC | adrenergic | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-ADR.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-ADR.md) | human; some rule justifications cite mouse studies |
| HDC | histaminergic | positive | [S1](#ref-s1) | [Human_adult/Neurotransmission/NT-HDC.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Neurotransmission/NT-HDC.md) | human; some rule justifications cite mouse studies |
| PVALB | cortical-pvalb | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-PVALB.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-PVALB.md) | human; some rule justifications cite mouse studies |
| LHX6 | cortical-pvalb | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-PVALB.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-PVALB.md) | human; some rule justifications cite mouse studies |
| DLX1 | cortical-pvalb | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-PVALB.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-PVALB.md) | human; some rule justifications cite mouse studies |
| GAD2 | cortical-pvalb | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-PVALB.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-PVALB.md) | human; some rule justifications cite mouse studies |
| FOXG1 | cortical-pvalb | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-PVALB.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-PVALB.md) | human; some rule justifications cite mouse studies |
| SST | cortical-sst | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-SST.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-SST.md) | human; some rule justifications cite mouse studies |
| LHX6 | cortical-sst | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-SST.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-SST.md) | human; some rule justifications cite mouse studies |
| DLX1 | cortical-sst | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-SST.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-SST.md) | human; some rule justifications cite mouse studies |
| GAD2 | cortical-sst | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-SST.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-SST.md) | human; some rule justifications cite mouse studies |
| FOXG1 | cortical-sst | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-SST.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-SST.md) | human; some rule justifications cite mouse studies |
| ADARB2 | cortical-sst | negative | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-SST.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-SST.md) | human; some rule justifications cite mouse studies |
| VIP | cortical-vip | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-VIP.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-VIP.md) | human; some rule justifications cite mouse studies |
| ADARB2 | cortical-vip | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-VIP.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-VIP.md) | human; some rule justifications cite mouse studies |
| CXCL14 | cortical-vip | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-VIP.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-VIP.md) | human; some rule justifications cite mouse studies |
| DLX1 | cortical-vip | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-VIP.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-VIP.md) | human; some rule justifications cite mouse studies |
| GAD2 | cortical-vip | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-VIP.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-VIP.md) | human; some rule justifications cite mouse studies |
| FOXG1 | cortical-vip | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-VIP.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-VIP.md) | human; some rule justifications cite mouse studies |
| LAMP5 | cortical-lamp5 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-LAMP5.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-LAMP5.md) | human; some rule justifications cite mouse studies |
| ADARB2 | cortical-lamp5 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-LAMP5.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-LAMP5.md) | human; some rule justifications cite mouse studies |
| CXCL14 | cortical-lamp5 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-LAMP5.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-LAMP5.md) | human; some rule justifications cite mouse studies |
| GAD2 | cortical-lamp5 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-LAMP5.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-LAMP5.md) | human; some rule justifications cite mouse studies |
| FOXG1 | cortical-lamp5 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-LAMP5.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-LAMP5.md) | human; some rule justifications cite mouse studies |
| LHX6 | cortical-lamp5 | negative | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/INT-LAMP5.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-LAMP5.md) | human; some rule justifications cite mouse studies |
| DRD1 | striatal-d1 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/MSN-D1.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D1.md) | human; some rule justifications cite mouse studies |
| GPR88 | striatal-d1 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/MSN-D1.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D1.md) | human; some rule justifications cite mouse studies |
| RGS9 | striatal-d1 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/MSN-D1.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D1.md) | human; some rule justifications cite mouse studies |
| FOXP1 | striatal-d1 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/MSN-D1.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D1.md) | human; some rule justifications cite mouse studies |
| SLC32A1 | striatal-d1 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/MSN-D1.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D1.md) | human; some rule justifications cite mouse studies |
| FOXG1 | striatal-d1 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/MSN-D1.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D1.md) | human; some rule justifications cite mouse studies |
| DRD2 | striatal-d2 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/MSN-D2.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D2.md) | human; some rule justifications cite mouse studies |
| GPR88 | striatal-d2 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/MSN-D2.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D2.md) | human; some rule justifications cite mouse studies |
| RGS9 | striatal-d2 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/MSN-D2.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D2.md) | human; some rule justifications cite mouse studies |
| FOXP1 | striatal-d2 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/MSN-D2.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D2.md) | human; some rule justifications cite mouse studies |
| SLC32A1 | striatal-d2 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/MSN-D2.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D2.md) | human; some rule justifications cite mouse studies |
| FOXG1 | striatal-d2 | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/MSN-D2.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D2.md) | human; some rule justifications cite mouse studies |
| PCP2 | cerebellar-purkinje | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/CB-PURK.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/CB-PURK.md) | human; some rule justifications cite mouse studies |
| SKOR2 | cerebellar-purkinje | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/CB-PURK.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/CB-PURK.md) | human; some rule justifications cite mouse studies |
| PVALB | cerebellar-purkinje | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/CB-PURK.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/CB-PURK.md) | human; some rule justifications cite mouse studies |
| GAD2 | cerebellar-purkinje | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/CB-PURK.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/CB-PURK.md) | human; some rule justifications cite mouse studies |
| CBLN1 | cerebellar-granule | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/CB-GRAN.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/CB-GRAN.md) | human; some rule justifications cite mouse studies |
| CBLN3 | cerebellar-granule | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/CB-GRAN.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/CB-GRAN.md) | human; some rule justifications cite mouse studies |
| GABRA6 | cerebellar-granule | positive | [S1](#ref-s1) | [Human_adult/Subtype/Neuronal/CB-GRAN.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/CB-GRAN.md) | human; some rule justifications cite mouse studies |
| SOX6 | da-sox6 | positive | [S2](#ref-s2) | [Fig1e and Results: SOX6/CALB1 DA branches](https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/) | human primary; comparative animal datasets separately |
| CALB1 | da-calb1 | positive | [S2](#ref-s2) | [Fig1e and Results: SOX6/CALB1 DA branches](https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/) | human primary; comparative animal datasets separately |
| SOX6 | da-sox6-agtr1 | positive | [S2](#ref-s2) | [Results/Fig3: SOX6_AGTR1 DA subtype; not a query vulnerability claim](https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/) | human primary; comparative animal datasets separately |
| AGTR1 | da-sox6-agtr1 | positive | [S2](#ref-s2) | [Results/Fig3: SOX6_AGTR1 DA subtype; not a query vulnerability claim](https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/) | human primary; comparative animal datasets separately |
| CALB1 | da-calb1-tmem200a | positive | [S2](#ref-s2) | [Results/Fig3: CALB1_TMEM200A DA subtype](https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/) | human primary; comparative animal datasets separately |
| TMEM200A | da-calb1-tmem200a | positive | [S2](#ref-s2) | [Results/Fig3: CALB1_TMEM200A DA subtype](https://pmc.ncbi.nlm.nih.gov/articles/PMC9076534/) | human primary; comparative animal datasets separately |
| HCRT | peptide-hcrt | positive | [S1](#ref-s1) | [Neuropeptides/NP-HCRT.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Neuropeptides/NP-HCRT.md) | human; some rule justifications cite mouse studies |
| PMCH | peptide-pmch | positive | [S1](#ref-s1) | [Neuropeptides/NP-PMCH.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Neuropeptides/NP-PMCH.md) | human; some rule justifications cite mouse studies |
| NPY | peptide-npy | positive | [S1](#ref-s1) | [Neuropeptides/NP-NPY.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Neuropeptides/NP-NPY.md) | human; some rule justifications cite mouse studies |
| SST | peptide-sst | positive | [S1](#ref-s1) | [Neuropeptides/NP-SST.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Neuropeptides/NP-SST.md) | human; some rule justifications cite mouse studies |
| VIP | peptide-vip | positive | [S1](#ref-s1) | [Neuropeptides/NP-VIP.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Neuropeptides/NP-VIP.md) | human; some rule justifications cite mouse studies |
| PLP1 | oligo-guard | positive | [S1](#ref-s1) | [Human_adult/Class/OLIGO.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/OLIGO.md) | human; some rule justifications cite mouse studies |
| MBP | oligo-guard | positive | [S4](#ref-s4) | [ScTypeDB_full.xlsx; Excel row 122; Brain/Oligodendrocytes](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx) | unspecified per row; mixed-case symbols present |
| MBP | oligo-guard | positive | [S1](#ref-s1) | [Human_adult/Class/OLIGO.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/OLIGO.md) | human; some rule justifications cite mouse studies |
| MOG | oligo-guard | positive | [S4](#ref-s4) | [ScTypeDB_full.xlsx; Excel row 122; Brain/Oligodendrocytes](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx) | unspecified per row; mixed-case symbols present |
| MOG | oligo-guard | positive | [S1](#ref-s1) | [Human_adult/Class/OLIGO.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/OLIGO.md) | human; some rule justifications cite mouse studies |
| SOX10 | oligo-guard | positive | [S4](#ref-s4) | [ScTypeDB_full.xlsx; Excel row 122; Brain/Oligodendrocytes](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx) | unspecified per row; mixed-case symbols present |
| PDGFRA | oligo-guard | negative | [S1](#ref-s1) | [Human_adult/Class/OLIGO.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/OLIGO.md) | human; some rule justifications cite mouse studies |
| SOX10 | opc-guard | positive | [S1](#ref-s1) | [Human_adult/Class/OPC.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/OPC.md) | human; some rule justifications cite mouse studies |
| PDGFRA | opc-guard | positive | [S1](#ref-s1) | [Human_adult/Class/OPC.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/OPC.md) | human; some rule justifications cite mouse studies |
| AQP4 | astro-guard | positive | [S4](#ref-s4) | [ScTypeDB_full.xlsx; Excel row 105; Brain/Astrocytes](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx) | unspecified per row; mixed-case symbols present |
| AQP4 | astro-guard | positive | [S1](#ref-s1) | [Human_adult/Class/ASTRO.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/ASTRO.md) | human; some rule justifications cite mouse studies |
| GJA1 | astro-guard | positive | [S1](#ref-s1) | [Human_adult/Class/ASTRO.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/ASTRO.md) | human; some rule justifications cite mouse studies |
| ALDH1L1 | astro-guard | positive | [S4](#ref-s4) | [ScTypeDB_full.xlsx; Excel row 105; Brain/Astrocytes](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx) | unspecified per row; mixed-case symbols present |
| SLC1A2 | astro-guard | positive | [S4](#ref-s4) | [ScTypeDB_full.xlsx; Excel row 105; Brain/Astrocytes](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx) | unspecified per row; mixed-case symbols present |
| FOXJ1 | astro-guard | negative | [S1](#ref-s1) | [Human_adult/Class/ASTRO.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/ASTRO.md) | human; some rule justifications cite mouse studies |
| TYROBP | myeloid-guard | positive | [S1](#ref-s1) | [Human_adult/Class/MGL.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/MGL.md) | human; some rule justifications cite mouse studies |
| DOCK8 | myeloid-guard | positive | [S1](#ref-s1) | [Human_adult/Class/MGL.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/MGL.md) | human; some rule justifications cite mouse studies |
| CD163 | macrophage-guard | positive | [S1](#ref-s1) | [Human_adult/Class/MAC.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/MAC.md) | human; some rule justifications cite mouse studies |
| MRC1 | macrophage-guard | positive | [S1](#ref-s1) | [Human_adult/Class/MAC.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/MAC.md) | human; some rule justifications cite mouse studies |
| F13A1 | macrophage-guard | positive | [S1](#ref-s1) | [Human_adult/Class/MAC.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/MAC.md) | human; some rule justifications cite mouse studies |
| CLDN5 | endothelial-guard | positive | [S1](#ref-s1) | [Human_adult/Class/ENDO.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/ENDO.md) | human; some rule justifications cite mouse studies |
| PECAM1 | endothelial-guard | positive | [S1](#ref-s1) | [Human_adult/Class/ENDO.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/ENDO.md) | human; some rule justifications cite mouse studies |
| FLT1 | endothelial-guard | positive | [S1](#ref-s1) | [Human_adult/Class/ENDO.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/ENDO.md) | human; some rule justifications cite mouse studies |
| PDGFRB | pericyte-guard | positive | [S1](#ref-s1) | [Human_adult/Class/PER.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/PER.md) | human; some rule justifications cite mouse studies |
| CSPG4 | pericyte-guard | positive | [S1](#ref-s1) | [Human_adult/Class/PER.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/PER.md) | human; some rule justifications cite mouse studies |
| MYH11 | pericyte-guard | negative | [S1](#ref-s1) | [Human_adult/Class/PER.md](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Class/PER.md) | human; some rule justifications cite mouse studies |
| DCX | immature-program | positive | [S4](#ref-s4) | [ScTypeDB_full.xlsx; Excel row 111; Brain/Immature neurons](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx) | unspecified per row; mixed-case symbols present |
| NEUROD1 | immature-program | positive | [S4](#ref-s4) | [ScTypeDB_full.xlsx; Excel row 111; Brain/Immature neurons](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx) | unspecified per row; mixed-case symbols present |
| TUBB3 | immature-program | positive | [S4](#ref-s4) | [ScTypeDB_full.xlsx; Excel row 111; Brain/Immature neurons](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx) | unspecified per row; mixed-case symbols present |
| NRGN | neuronal-background | positive | [S3](#ref-s3) | [Methods: Cluster cell-type annotation; NRGN used in major neuronal annotation](https://pmc.ncbi.nlm.nih.gov/articles/PMC10780895/) | human primary; mouse and human organoids as separately described validation |
| RIT2 | rit2-enriched-program | positive | [S3](#ref-s3) | [Fig1C/Fig2; TableS2 C9; study-associated neuronal enrichment](https://pmc.ncbi.nlm.nih.gov/articles/PMC10780895/) | human primary; mouse and human organoids as separately described validation |
| GALNTL6 | galntl6-associated-program | positive | [S3](#ref-s3) | [Fig1C/Fig4B/E/G; TableS2 C6 and subclusters; distinct from RIT2 program](https://pmc.ncbi.nlm.nih.gov/articles/PMC10780895/) | human primary; mouse and human organoids as separately described validation |

机器可读完整字段（DOI、固定版本、evidence_family及各规则用途）见[冻结逐基因溯源表](https://github.com/MiaoranZhang/zmr-neuron-markers/blob/38c5c25087ffb98d7836b2cbd7a7e7d2498b57d1/assets/marker_literature.tsv)。本次只新增文档；未上传项目表达矩阵、供者元数据或私有分析结果。
