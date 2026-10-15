# 文献相关的神经元表达程序

对应[`study-programs.json`](../assets/rules/study-programs.json)，新增两个program，不增加固定名称的细胞类型。适用成人、人类中脑/黑质；其他脑区需要重新核验来源适用性。

## RIT2富集程序

核心为可信的RIT2表达及相对可比神经元的富集证据，父级是已审阅的神经元High。RBFOX3、SNAP25、SYP、MAP2、NRGN辅助核验神经元归属，不能替代RIT2。群内一致性、表达比例、效应量与可评估供者需记录；程序High只说明表达程序得到支持。

来源为Wang 2024的Fig1C、Fig2及TableS2/C9。RIT2阳性不单独证明固定亚型、DA身份或PD易损性；TH未检出不证明TH生物学阴性。RIT2在来源数据的非神经元群也可出现，先核实谱系背景。

## GALNTL6相关程序

核心为可信的GALNTL6表达及神经元间的富集/分布证据，父级同为神经元High，辅助同上。来源为Fig1C、Fig4B/E/G和TableS2/C6及部分亚群。来源支持的是表达关联，并没有校准该基因的跨队列类型特异性。

不把RIT2设为GALNTL6的必需核心或辅助补救。两种程序可以在一个正式cluster分别记录；声称同细胞共表达时另查原始计数共同检出比例。广泛分布、低深度或供者集中的信号不能直接改名为固定细胞群。

## 与最终身份的关系

最终身份仍由cluster整体审阅决定。主要身份及递质名称保留，程序写入独立字段，例如`cluster_RIT2_program`、`cluster_GALNTL6_program`。需要可读显示标签时可附加“RIT2-enriched program”等描述，但不把程序赋予排他身份；单个成员细胞未检出不改变其cluster身份。

`rescue_routes`为空，没有“NRGN或RIT2高就补齐神经元/DA核心”的路径。未解决谱系或来源冲突时保留父层级/程序未定。来源与当前GSE184950共享数据时不得宣称独立验证。
