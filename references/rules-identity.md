# 大类、递质与非神经元竞争身份规则

本文件解释 `assets/rules/identity.json` 的 19 条规则。它们是成人、人类神经元分析的审阅规则，状态均为 **curated_unbenchmarked**：已整理来源并明确证据条件，但尚未在留出数据上校准分类性能。High 表示证据充分程度，不是一个准确率或后验概率。

## 共同解释

- `core_routes` 的不同路径是 OR；一条路径的 `all_of` 外层是 AND、每个内组是 ANY。例如 `[[SNAP25,SYP],[MAP2,RBFOX3,STMN2,TUBB3]]` 要求两组分别有支持证据。
- 此处 supported 是对**指定鉴定单位**完成表达质量审阅后的证据状态，不等于 UMI > 0，也不是要求每个细胞全部检出。单位可为单细胞、可解释的同质亚群或簇；单细胞未检出不能用簇均值冒充其自身表达。由父簇继承的标签必须另标为继承，而非逐细胞核心组合实测通过。
- High 还需要通过适用范围、质量、区分竞争类型和冲突解释四个门槛。仅满足基因组合不自动输出 High。`regions: all` 表示各脑区可进入审阅，不表示这些细胞普遍存在于所有脑区。
- 多数递质规则要求神经元父级 High。非神经元 guard 的父级为 null，因为它们检查另一条谱系，而非神经元的子类。
- “辅助”可以加强判断，不能随意替换缺失核心。所有 `rescue_routes` 均为空：当前没有被声明为已经验证的补救组合。来源原本存在的两条 DA/GABA 路径保留为核心替代路径，并非本库临时拼凑的补救。
- 未测量、可测但未检出、低检测能力和有可信反证应分别记录。阴性基因缺失不等于“已排除竞争类型”；阳性冲突也不能由单个弱信号一票否决。
- 同一来源中的规则、参考图谱标签和衍生 marker 不是三份独立验证。参与补充定名的参考证据也应记录为鉴定依据，而非事后独立验证。

## 1. 神经元背景 — `neuronal-background`

**核心：** `(SNAP25 或 SYP) 且 (MAP2、RBFOX3、STMN2、TUBB3 中至少一个)`。这是本库提出的分组编辑规则，不是 Siletti 的单 `RBFOX3` 原规则，也不是经性能验证的“两基因分类器”。其余核心组成员提供一致性支持，当前没有额外、独立的辅助组。

**竞争检查：** 分别比较少突/OPC 的 SOX10、PDGFRA、PLP1、MBP、MOG，星形胶质的 AQP4、GJA1、ALDH1L1、SLC1A2，以及免疫/血管面板。零散髓鞘 RNA 不单独否定神经元。

**High：** 核心组合、整体神经元表达背景和该单位内的一致性均成立，且可区分主要非神经元候选。**降级：** 仅有部分泛神经元证据时为 Neuron candidate，最多 Moderate；成套谱系冲突未解释则保留 Uncertain。RBFOX3 不是必要的单一门槛。

## 2. 多巴胺能 — `da-core`

**核心路径 A：** TH + SLC6A3 + SLC18A2，保留 Kamath 成人黑质来源组合。**路径 B：** TH + DDC + SLC6A3，保留 Siletti 来源组合。两条为 OR，不要求四个基因一起检出。跨出来源脑区时要核查匹配参考。DDC 或 SLC18A2 可为另一条已采用路径提供互补证据，不算独立验证。

**竞争检查：** DBH/TH/DDC 的去甲肾上腺素程序、PNMT/DBH/TH/DDC 的肾上腺素程序。GAD 与 SLC17A6/7/8 相关共程序要区分同细胞表达、混簇和污染；并存不必自动否定 DA。

**High：** 神经元父级 High，至少一条三联路径 supported，且匹配脑区的整体背景可区分其他单胺候选。**降级：** 路径不足时为 DA candidate/monoaminergic unresolved，最高 Moderate；SOX6、CALB1 等亚型信号不能补成 DA 核心。DA High 不传递为亚型、黑质解剖层次或 PD 易损性 High。

## 3. GABA 能 — `gaba-core`

**核心路径 A：** GAD1 + SLC32A1；**路径 B：** GAD2 + SLC32A1。分别保留原 GABA1/GABA2 路径 ID。另一种 GAD 提供合成程序一致性，不能在本版中取代 SLC32A1。

**竞争检查：** 两条来源原规则都含 `-SLC6A5`。它是阴性项，不是甘氨酸的阳性项被误混进 GABA 核心。本库将其作为甘氨酸/共程序审阅，避免把真实 GABA–甘氨酸并存机械排除；同时检查 SLC17A6/7/8 背景。

**High：** 神经元父级 High、至少一条来源路径成立、竞争递质程序已有可审阅解释。**降级：** 只有 GAD 或只有 SLC32A1 为候选，最高 Moderate；混合来源未解时 transmitter unresolved。RNA 支持 GABA 身份不等于验证实际递质释放或生理抑制作用。

## 4. SLC17A7 相关谷氨酸能 — `glut-vglut1`

**核心：** SLC17A7。SNAP25、SYP、MAP2 是父级神经元背景支持，不能替代谷氨酸相关核心。

**竞争检查：** GAD1/GAD2/SLC32A1、SLC6A5，以及其他完整单胺/胆碱能程序。需要确定高信号来自同一细胞群，不能用少数异常值代表整个簇。

**High：** 神经元父级 High，可信且一致的 SLC17A7 证据，另有匹配成人脑区的整体谷氨酸能表达参考与竞争程序比较。只有一个 marker、没有整体背景核验时最多 Moderate。**降级：** 缺核心回到父级；冲突未解为 transmitter unresolved。该规则不推断皮层层次、投射类型或递质独占性。

## 5. SLC17A6 相关谷氨酸能 — `glut-vglut2`

**核心：** SLC17A6。辅助 SNAP25、SYP、MAP2 只支持神经元背景。

**竞争检查：** GABA/甘氨酸和单胺/胆碱能整体程序。DA 等类型出现额外 SLC17A6 程序时，不能直接覆盖已经有充分依据的身份。

**High：** 神经元父级 High，核心信号可信且非少量异常细胞驱动，整体表达与匹配脑区的谷氨酸能参考相符，竞争解释已核验。只有单 marker 则上限 Moderate。**降级：** 核心缺失回到父级；未解混合则 transmitter unresolved，已确认的表达共程序可作非排他描述。

## 6. SLC17A8 相关程序 — `glut-vglut3`

**核心：** SLC17A8；神经元背景由 SNAP25、SYP、MAP2 等支持。虽然原来源放在递质分类中，本库明确将 `claim_kind` 和 `level` 设为 **program**。

**情境检查：** GABA、胆碱能、5-HT 等表达程序可与其并存。检查目的在于确认来源、区分同细胞与混群，不要求所有递质程序互斥。

**High：** 神经元父级 High，SLC17A8 信号来源和单位内一致性可信，并报告其他递质背景。此 High 仅指程序证据充分，绝不能改写为“排他的谷氨酸能/兴奋性细胞 High”。**降级：** 核心未支持则程序不可评估；来源不明则 Moderate/Uncertain，保留已可靠的父级身份。

## 7. 甘氨酸能 — `glycinergic`

**核心：** SLC6A5 + SLC32A1。辅助 SNAP25/MAP2 只确认神经元背景。SLC32A1 与 GABA 共用，不能单独区分二者。

**竞争检查：** GAD1/GAD2 程序、SLC17A6/7 程序，以及解剖相容性。GABA–甘氨酸表达并存不自动否定甘氨酸能候选，也不能只凭簇均值宣布功能性共释放。

**High：** 神经元父级 High、双核心成立、取材/参考支持且混合来源已解决。**降级：** 只见 SLC6A5 为候选；只见 SLC32A1 则递质未定；核心不完整最高 Moderate。

## 8. 5-HT 能 — `serotonergic`

**核心：** TPH2 + FEV + DDC。SLC18A2 来自本库 DA 核心面板，只提供共享的单胺囊泡背景，并非 DA 或 5-HT 特异辅助。

**竞争检查：** TH/SLC6A3/DBH/PNMT 所属儿茶酚胺组合，以及额外 SLC17A6/8 或 GAD 程序。DDC 本身是共享证据。TPH1 不能被静默改名或自动当作 TPH2 替代；本版没有引入库外补救基因。

**High：** 神经元父级 High、三联路径成立、匹配成人脑区/取材支持，能够区分更合理的其他单胺身份。**降级：** 部分核心只能形成 5-HT candidate；强冲突未解为 monoamine/transmitter unresolved。

## 9. 胆碱能 — `cholinergic`

**核心：** CHAT + SLC5A7，保留 Siletti 原组合。**辅助：** SLC18A3，为 ScType 来源的囊泡证据。本版没有把 CHAT + SLC18A3 声明为已验证的替代路径。

**竞争检查：** GABA、谷氨酸相关、DA 等程序；共程序需要审阅而非自动否决。

**High：** 神经元父级 High、核心组合成立、匹配脑区的整体胆碱能背景支持且群内异质性检查通过。**降级：** 核心不足为胆碱能候选，最多 Moderate；未解冲突为 transmitter unresolved。不据此自动推断运动神经元或基底前脑细类。

## 10. 去甲肾上腺素能 — `noradrenergic`

**核心：** DBH + TH + DDC。**辅助：** SLC18A2 为共享单胺囊泡证据，不能替代 DBH。

**竞争检查：** PNMT + DBH + TH + DDC 的肾上腺素背景，和 TH/SLC6A3/SLC18A2 的 DA 背景。共享的 TH/DDC 不能重复当作两份独立证据。

**High：** 神经元父级 High、三联 supported、解剖相容且整体背景能区分 DA/ADR。PNMT 未检出必须结合检测能力解释。**降级：** DBH 不足或背景不全为 NE/catecholaminergic candidate，最高 Moderate；不能分辨则 catecholaminergic unresolved。不直接推断蓝斑来源。

## 11. 肾上腺素能 — `adrenergic`

**核心：** PNMT + DBH + TH + DDC。**辅助：** SLC18A2 为非特异单胺背景。

**竞争检查：** NE 与 DA。NE 的三个共享合成基因不能补齐未支持的 PNMT。

**High：** 神经元父级 High、四联组合可信，并有匹配成人解剖部位的 ADR 整体参考证据；PNMT 细胞归属明确且不是罕见异常高值/污染。**降级：** 核心不足或 NE/DA 冲突未解时保留 catecholaminergic unresolved；不以罕见性本身作为真实性依据。

## 12. HDC 相关组胺能候选 — `histaminergic`

**核心：** 当前只有 HDC。SNAP25、MAP2、SYP 只能支持神经元背景。**情境检查：** 免疫/非神经元 HDC 来源和混合；本库免疫 guard 并不完整覆盖所有 HDC 阳性非神经元，缺少其标志不能证明已排除。

**当前身份置信度上限为 Moderate。** 神经元父级 High 和很高的 HDC 表达也不能解除上限。未来要升级，需新增有溯源的成人匹配脑区组胺能特异组合或整体参考证据、竞争来源核验，并经新版本规则审阅和适用数据验证；本版没有这样的补救路径。

**降级：** HDC 缺失则不支持该候选；来源不明则 Low/Uncertain。可另报 HDC 程序，但不可把程序可信度转成组胺能身份 High。

## 13. 少突胶质细胞 — `oligo-guard`

**核心：** PLP1 + MBP + MOG，来自 Siletti。**辅助：** SOX10，提供少突谱系背景但与 OPC 共享。来源 `-PDGFRA` 进入 OPC/成熟过渡竞争核验。

**竞争检查：** OPC 的 SOX10/PDGFRA，和完整神经元程序。多种髓鞘 RNA 也可能同时来自环境污染，不能仅凭三联存在就改标签。

**High：** 三联、整体少突背景及细胞来源一致，神经元与 OPC 竞争解释审阅通过。**降级：** 核心不全为 oligodendroglial candidate；未解神经元/胶质混合则 Uncertain。SOX10 不能自动补成已验证替代路径。

## 14. OPC — `opc-guard`

**核心：** SOX10 + PDGFRA。**辅助：** CSPG4，仅为共享情境信号，出处记录到 `pericyte-guard`，不伪称独立 OPC 验证。LHFPL3 不构成此规则的单基因替代。

**竞争检查：** 成熟少突的 PLP1/MBP/MOG、周细胞的 PDGFRB/CSPG4，以及完整神经元背景。

**High：** 双核心及整体少突前体背景一致，能区分成熟少突、周细胞和神经元。**降级：** 只有 CSPG4 或其他非特异信号不能定 OPC；冲突未解保留谱系候选/Uncertain。

## 15. 星形胶质细胞 — `astro-guard`

**核心：** AQP4 + GJA1，保留 Siletti。**辅助：** ALDH1L1、SLC1A2，来自 ScType；尚未声明为替代核心的已验证组合。

**竞争检查：** 来源 `-FOXJ1` 提示室管膜/纤毛程序核验；同时比较神经元与少突谱系。完整室管膜面板不在当前库中，因此需匹配整体参考，不能仅用 FOXJ1 缺失作已排除证明。

**High：** 核心和整体星形胶质背景一致，信号不是边界混合/污染，竞争身份已核验。**降级：** 仅辅助背景为 astroglial candidate，最多 Moderate；强冲突未解为 glial/Uncertain。本规则不定义功能状态。

## 16. 广义髓系候选 — `myeloid-guard`

**核心：** TYROBP + DOCK8。这是对来源 MGL 正向部分的编辑性提取，并把输出限制为广义髓系；原作者 microglia 名称及未完整收录的阴性组合不能直接移植。当前无额外特异辅助集合。

**竞争检查：** CD163/MRC1/F13A1 是髓系内部细分方向，不排除广义髓系。还需比较非髓系免疫、神经元与血管候选；本小面板不足以覆盖全部竞争细胞。

**High：** 双核心及整体免疫背景一致，并有匹配成人脑免疫参考区分非髓系候选；High 仅允许广义髓系身份。**降级：** 缺参考或竞争解释未解时为 immune-associated candidate，最高 Moderate/Uncertain。此规则永远不单独产出 microglia 或 BAM 精细标签。

## 17. 巨噬细胞相关 — `macrophage-guard`

**核心：** CD163 + MRC1 + F13A1。**辅助：** TYROBP、DOCK8，只支持共享髓系背景，不区分小胶质与 BAM。

**竞争检查：** 匹配参考中的小胶质与其他髓系类型，以及血管邻近细胞/神经元混合。空间邻近和髓系共有基因不能证明 BAM 身份。

**High：** 三联成立、免疫/髓系背景可信，并完成匹配成人参考的主要竞争类型比较。标签限为 macrophage-associated，不能进一步宣称边界位置、外周浸润或起源。**降级：** 组合不全至多 Moderate；微胶质/巨噬不能区分时保留 myeloid unresolved。

## 18. 内皮细胞 — `endothelial-guard`

**核心：** CLDN5 + PECAM1 + FLT1。当前无独立辅助基因集合，匹配血管整体参考可提供外部支持并另行溯源。FLT1 单独不足。

**竞争检查：** 周细胞/平滑肌的 PDGFRB、CSPG4、MYH11，以及免疫和神经元整体程序。

**High：** 三联与整体内皮背景、细胞归属一致，主要血管壁/免疫竞争解释已核验。**降级：** 部分血管证据为 vascular/endothelial candidate，最多 Moderate；未解混合为 vascular/mixed-lineage unresolved。不由此规则区分动静脉、毛细血管或功能状态。

## 19. 周细胞相关 — `pericyte-guard`

**核心：** PDGFRB + CSPG4。来源另有 `-MYH11`，用于血管壁情境审阅。当前没有经验证的辅助替代组合。

**竞争检查：** OPC 的 SOX10/PDGFRA/CSPG4、MYH11 相关平滑肌/过渡血管壁程序、内皮三联。CSPG4 共享，不应单独定 OPC 或周细胞；本库没有完整平滑肌面板。

**High：** 双核心在可信血管壁背景中一致，并有匹配成人脑血管整体参考区分 OPC、平滑肌和其他血管壁候选。MYH11 缺测不算排除成功。**降级：** 双 marker 之外缺乏区分证据时至多 Moderate；冲突未解为 mural/vascular-associated unresolved。

## 溯源与范围

每条机器规则的 `source_panel_ids` 记录所有实际借用基因的本库面板；这些面板通过 `assets/panel_source_map.json` 和 `assets/curated_marker_assertions.tsv` 连接到来源版本及原始条目。JSON 的 `basis` 区分原来源正向组合、原来源单 marker 与本库编辑组合。原阴性项的保留和解释在每条规则中单列。

- Siletti 规则固定版本：[02e092b4a3f0d294d4bcd8ab574dfc98f51d7981](https://github.com/linnarsson-lab/auto-annotation-ah/tree/02e092b4a3f0d294d4bcd8ab574dfc98f51d7981)。原来源是研究规则，跨数据集适配仍需核验。
- DA 来源：[Kamath 等，2022](https://doi.org/10.1038/s41593-022-01061-1)。本库保留来源 DA 三联，不把疾病关联移植为 query 的易损性结论。
- ScType 与 PanglaoDB 来源版本、物种/阶段限制见 `references/resource-guide.md` 和 source registry。多库重复记录并不自动构成独立证据。

这 19 条规则不更改任何 PD 数据、原作者标签或既有 cluster 注释。它们定义未来审阅所需的证据，实际应用必须另交付逐单位的证据、冲突、缺失状态、判断人/版本及各层级置信度。
