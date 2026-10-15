# 脑区亚型与附加表达程序规则

对应机器可读文件：[`assets/rules/contextual.json`](../assets/rules/contextual.json)。本文件覆盖 8 个脑区亚型、4 个 DA 相关程序、5 个神经肽程序和 1 个成熟度程序，共 18 项。它们继承统一的适用范围、质量、竞争类型鉴别和冲突审阅门槛。

这里的 **核心组合** 是经过表达审阅后支持的证据组合；`all_of` 外层为 AND、内层为 ANY。它不是原始 UMI > 0 的布尔判定，不要求每个低深度单细胞全部检出，也不能将同簇不同细胞的零散阳性拼成同细胞组合。群体支持与逐细胞标签必须分开。下列所有规则均为 `curated_unbenchmarked`，没有校准准确率或已经验证的替代路线；`rescue_routes` 均为空。辅助集合可以加强证据，不能自动补齐缺失核心。High 的额外条件包括匹配参考时，必须在实际查询中完成并记录，不能因本文件列出条件就视为已完成。

亚型路线的父级必须为 High；父级不确定时保留更粗的可靠身份。**程序 High 只表示所述表达程序得到充分支持，不表示精细身份 High，更不表示功能活性、投射关系或疾病易损性已被证明。** 不同程序可共存。完整竞争程序触发人工审阅，一个冲突基因不构成自动否决。

## 成人皮层亚型

这四个身份名称限制在成人皮层，不是在宣称 PVALB、SST、VIP、LAMP5 这些基因是皮层专属。所有四项都以 `gaba-core` High 为父级，并比较匹配成人皮层参考中的近邻类别。当前组合是已有溯源面板的人工整理子集，不是完整原作者分类器。

### cortical-pvalb

- **核心**：PVALB + LHX6 + DLX1 + GAD2 + FOXG1。
- **辅助**：GAD1、SLC32A1 及神经元父级，支持抑制性背景。
- **冲突审阅**：SST、VIP/ADARB2、LAMP5 相关完整程序，核查混群或共享表达。
- **High**：皮层来源、GABA 父级、核心与近邻参考比较均支持该粗粒度亚型；不向更精细皮层类型自动延伸。
- **降级**：核心不完整时保留皮层 GABA 亚型未定或 PVALB-associated candidate；PVALB 单基因不能定名。
- **来源**：[固定版本 INT-PVALB](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-PVALB.md)。

### cortical-sst

- **核心**：SST + LHX6 + DLX1 + GAD2 + FOXG1。
- **辅助**：GAD1、SLC32A1 及神经元背景；SST 肽程序与此路线共享证据，不算独立验证。
- **冲突审阅**：ADARB2/VIP/LAMP5 相关程序及其他近邻类别。原规则中的 ADARB2 阴性是特定分类语境，不能推广为所有 SST 细胞必须不表达 ADARB2，也不能以未检出证明阴性。
- **High**：成人皮层与 GABA 父级 High，核心和匹配参考一致，ADARB2 等竞争证据已有解释。
- **降级**：保留 GABA 父级及可证实的 SST 肽程序；组合不全不补成皮层 SST 身份。
- **来源**：[固定版本 INT-SST](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-SST.md)。

### cortical-vip

- **核心**：VIP + ADARB2 + CXCL14 + DLX1 + GAD2 + FOXG1。
- **辅助**：GAD1、SLC32A1 及神经元背景；VIP 肽程序不是独立验证。
- **冲突审阅**：LHX6/PVALB/SST 及 LAMP5 相关近邻程序，按整套证据与细胞归属判断。
- **High**：成人皮层、GABA 父级 High，并且核心能够在匹配参考中区分相近类别。
- **降级**：只保留 GABA 父级、VIP 程序或亚型候选；非皮层细胞不套用该身份。
- **来源**：[固定版本 INT-VIP](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-VIP.md)。

### cortical-lamp5

- **核心**：LAMP5 + ADARB2 + CXCL14 + GAD2 + FOXG1。
- **辅助**：GAD1、SLC32A1 及神经元背景。
- **冲突审阅**：来源的 LHX6 阴性及其他皮层类别；LAMP5/LHX6 相关其他分类语境需要重新比较参考，不机械否决。
- **High**：成人皮层和 GABA 父级 High，匹配参考支持本来源语境下的 LAMP5 类别，竞争证据已解决。
- **降级**：LAMP5-associated candidate 或 GABA 皮层亚型未定；不能覆盖全部 LAMP5 阳性细胞。
- **来源**：[固定版本 INT-LAMP5](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/INT-LAMP5.md)。

## 成人纹状体亚型

### striatal-d1

- **核心**：DRD1 + GPR88 + RGS9 + FOXP1 + SLC32A1 + FOXG1。
- **辅助**：GAD1、GAD2 及神经元背景；父级为 `gaba-core` High。
- **冲突审阅**：DRD2 相关表达及完整 DA 合成/转运程序。DRD1 是受体证据，不能把接受多巴胺信号解释为产生多巴胺。DRD1/DRD2 共同检出需检查细胞级关系，不自动二分或称共表达类型。
- **High**：成人纹状体来源、MSN 背景、核心与匹配人类参考支持 D1-associated 类别，且能区分 D2 及近邻群。
- **降级**：MSN-associated candidate 或 GABA 纹状体亚型未定；单 DRD1 不足。身份标签不直接确认投射靶点、直接通路或功能活性。
- **来源**：[固定版本 MSN-D1](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D1.md)。

### striatal-d2

- **核心**：DRD2 + GPR88 + RGS9 + FOXP1 + SLC32A1 + FOXG1。
- **辅助**：GAD1、GAD2 及神经元背景；父级为 `gaba-core` High。
- **冲突审阅**：DRD1 相关表达及完整 DA 合成/转运程序；DRD2 不属于 DA 产生身份的充分依据。
- **High**：成人纹状体来源、MSN 背景、核心和匹配参考一致，并已比较 D1 及其他近邻类别。
- **降级**：MSN-associated candidate 或 GABA 纹状体亚型未定；核心缺失不以 DRD1 或泛神经元补成 D2。身份标签不直接确认间接通路或疾病作用。
- **来源**：[固定版本 MSN-D2](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/MSN-D2.md)。

## 成人小脑亚型

### cerebellar-purkinje

- **核心**：PCP2 + SKOR2 + PVALB + GAD2。
- **辅助**：GAD1、SLC32A1 及神经元背景；父级为 `gaba-core` High。
- **冲突审阅**：CBLN1/CBLN3/GABRA6 相关颗粒细胞程序和混合细胞来源。
- **High**：成人小脑来源、核心一致，且在匹配**人类**小脑参考中得到支持并能区别近邻类型。原规则理由含小鼠小脑研究，仅该物种来源不能完成成人查询验证。
- **降级**：GABA 小脑亚型未定或 Purkinje-associated candidate；PVALB 不单独决定身份。
- **来源**：[固定版本 CB-PURK](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/CB-PURK.md)。

### cerebellar-granule

- **核心**：CBLN1 + CBLN3 + GABRA6；父级为 `neuronal-background` High。
- **辅助**：独立核验 SLC17A7/SLC17A6 相关谷氨酸程序；递质置信度另行保存，不由亚型结论反向自动赋 High。
- **冲突审阅**：PCP2/SKOR2、GAD1/GAD2/SLC32A1 相关程序及完整少突谱系。GABRA6 的受体表达不等于合成 GABA。
- **High**：成人小脑来源、神经元父级、完整组合和匹配人类小脑参考均支持；原来源类别中的 `Glial` 元数据矛盾已记录而未被沿用。
- **降级**：神经元小脑亚型未定；谷氨酸转运体不替代颗粒亚型组合。谱系冲突未解决时为 Uncertain。
- **来源**：[固定版本 CB-GRAN](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Human_adult/Subtype/Neuronal/CB-GRAN.md)。

## DA 父级内的表达程序

以下四项以 `da-core` High 为父级，辅助集合均为 TH、SLC6A3、SLC18A2、DDC。这些辅助基因确认 DA 背景，不能替代各程序的命名基因。来源为 [Kamath 等人类 SNpc DA 研究](https://doi.org/10.1038/s41593-022-01061-1)；SOX6/CALB1 分支及 SOX6_AGTR1、CALB1_TMEM200A 亚群是来源语境。当前简化面板只给出相关 **program**，不自动复现精确参考亚型。

### da-sox6

- **核心**：SOX6，限定已确认的成人中脑/黑质 DA 父级。
- **辅助**：上述 DA 核心与父级证据。
- **冲突审阅**：CALB1 相关分布及 DBH/PNMT 竞争身份程序；SOX6/CALB1 不硬设互斥。
- **High**：SOX6 表达可信地归属 DA 评估单位，父级与质量条件成立；仅为程序 High。
- **降级**：SOX6 证据不足保留 DA 父级及程序未定。不能从 SOX6 阳性推断全部细胞易损、具体 SNpc 位置或精确 Kamath 亚型。
- **来源位置**：Kamath Results / Figure 1 的 SOX6/CALB1 DA 分支。

### da-calb1

- **核心**：CALB1，限定已确认的成人中脑/黑质 DA 父级。
- **辅助**：DA 核心与父级证据。
- **冲突审阅**：SOX6 分布及 DBH/PNMT 竞争身份程序；CALB1 本身不是 DA 专属。
- **High**：可信的 DA 内 CALB1 程序及父级条件成立。
- **降级**：保留 DA 父级、CALB1 程序未定；不得把 CALB1 阳性等同于 PD 保护或抗性。
- **来源位置**：Kamath Results / Figure 1 的 SOX6/CALB1 DA 分支。

### da-sox6-agtr1

- **核心**：SOX6 + AGTR1，成人黑质 DA 父级。
- **辅助**：DA 核心及 SOX6 分支；同一 SOX6 不能重复算作独立证据。
- **冲突审阅**：CALB1/TMEM200A 相关程序的细胞级分布及混群。
- **High**：两基因组合在同一可靠 DA 评估群中成立，群内异质性已核查；只给程序 High。
- **降级**：仅 SOX6 充分时可转评 `da-sox6`，不是补齐本路线；只有 AGTR1 不足。精确亚型与疾病易损性需额外完整参考/独立疾病分析。
- **来源位置**：Kamath Results / Figure 3 的 SOX6_AGTR1 相关结果。

### da-calb1-tmem200a

- **核心**：CALB1 + TMEM200A，成人黑质 DA 父级。
- **辅助**：DA 核心及 CALB1 分支；同一来源的共享证据不独立。
- **冲突审阅**：SOX6/AGTR1 相关程序与混群，不根据单基因硬排除。
- **High**：两基因组合在可靠 DA 评估单位中成立，细胞归属和异质性已核查；只给程序 High。
- **降级**：仅 CALB1 时可另评 `da-calb1`；不能补成双基因程序。不从该程序推断精确亚型、背侧层或 PD 抗性。
- **来源位置**：Kamath Results / Figure 3 的 CALB1_TMEM200A 相关结果。

## 神经肽程序

以下程序都以 `neuronal-background` High 为父级，辅助集合为 SNAP25、MAP2、SYP；辅助基因核验信号归属，不替代肽基因。程序 High 可以针对一个明确转录本的可信表达成立，但不能转换成细胞身份 High。程序共同存在时可分别记录，是否共表达必须在细胞层面检查。

**HCRT、PMCH在匹配下丘脑及完整多基因参考支持下能够参与细胞类型鉴定。** 本版本没有构建完整下丘脑HCRT/PMCH身份路线，因此保留为program。相关人类下丘脑背景可参见[HYPOMAP](https://www.nature.com/articles/s41586-024-08504-8)；本规则未导入该完整参考或其全部marker。

### peptide-hcrt

- **核心**：HCRT。
- **辅助**：神经元背景与上述泛神经元集合。
- **冲突审阅**：PMCH 同簇共现、混合细胞、环境 RNA 和异常取材语境。
- **High**：神经元父级及 HCRT 信号的细胞归属、质量成立；实际脑区已记录，异常解剖背景已复核；只声明 HCRT 程序。
- **降级**：HCRT 证据不足为程序未定，其他肽不能替代；不直接命名 orexin 神经元。
- **来源**：[固定版本 NP-HCRT](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Neuropeptides/NP-HCRT.md)。

### peptide-pmch

- **核心**：PMCH。
- **辅助**：神经元背景与上述泛神经元集合。
- **冲突审阅**：HCRT 共现、混群、环境 RNA 和解剖来源。
- **High**：PMCH 信号可信地属于神经元评估单位，语境与技术解释已审阅；只声明 PMCH 程序。
- **降级**：PMCH 程序未定，不以 HCRT 或其他肽补齐，也不直接命名完整下丘脑类型。
- **来源**：[固定版本 NP-PMCH](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Neuropeptides/NP-PMCH.md)。

### peptide-npy

- **核心**：NPY。
- **辅助**：神经元背景与上述泛神经元集合。
- **冲突审阅**：完整非神经元谱系及环境 RNA/细胞混合解释。
- **High**：NPY 信号有可信神经元归属；只声明程序，不据此推断唯一脑区、递质或生理功能。
- **降级**：程序未定，保留可靠父级；不以另一肽基因替代。
- **来源**：[固定版本 NP-NPY](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Neuropeptides/NP-NPY.md)。

### peptide-sst

- **核心**：SST。
- **辅助**：神经元背景与上述泛神经元集合。
- **冲突审阅**：完整非神经元程序及信号归属，单个胶质 RNA 不否决。
- **High**：神经元内 SST 程序证据充分；非皮层也可描述程序，不能因此命名皮层 SST 中间神经元。
- **降级**：SST 程序未定；皮层身份另走 `cortical-sst`。两条路线共享 SST 不算独立验证。
- **来源**：[固定版本 NP-SST](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Neuropeptides/NP-SST.md)。

### peptide-vip

- **核心**：VIP。
- **辅助**：神经元背景与上述泛神经元集合。
- **冲突审阅**：完整非神经元程序及环境污染/混合细胞。
- **High**：VIP 信号可靠归属于神经元，只确认程序，不自动推导 GABA 身份或皮层类别。
- **降级**：VIP 程序未定；皮层身份另走 `cortical-vip`，共享 VIP 证据不构成独立验证。
- **来源**：[固定版本 NP-VIP](https://github.com/linnarsson-lab/auto-annotation-ah/blob/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981/Neuropeptides/NP-VIP.md)。

## 成熟度相关程序

### immature-program

- **核心**：DCX + NEUROD1 + TUBB3；父级为 `neuronal-background` High。
- **辅助**：MAP2、SNAP25、SYP 核验神经元背景和成熟度异质性；成熟程序共现不机械否决。
- **冲突审阅**：SOX10/PDGFRA、AQP4/ALDH1L1 相关完整胶质程序与混群、技术解释。
- **置信上限**：**Moderate**。ScType 对应行没有年龄、物种与脑区细分；现有组合没有成人脑神经发生的验证能力。保留来源 `stage=unspecified`，不得擅自当成人特异证据。
- **降级**：核心不全只记录实际支持的表达及成熟度程序未定；TUBB3 也在泛神经元面板中，不能重复算独立证据。
- **不可推断**：成人神经发生、细胞增殖、出生时间、命运或新生神经元身份。提升规则需要新增匹配人类证据并修订版本。
- **来源**：[固定版本 ScType 工作簿](https://raw.githubusercontent.com/IanevskiAleksandr/sc-type/630e15cf1e51f2612eda4ad0406dfb17503fa8c9/ScTypeDB_full.xlsx)，`Brain / Immature neurons`，原检查定位 Excel 第 111 行；完整数据库未随本包分发。

每个辅助或冲突基因的来源通过规则中的 `source_panel_ids` 追溯至 [`curated_marker_assertions.tsv`](../assets/curated_marker_assertions.tsv) 与 [`panel_source_map.json`](../assets/panel_source_map.json)。来源分类名、人工规则的适用范围、查询数据表达证据是分别保存的层级。
