# zmr-neuron-markers

面向成人脑、尤其 PD 中脑/黑质 scRNA-seq 与 snRNA-seq 的个人神经元鉴定 SKILL。维护者：MiaoranZhang。首次整理：2026-10-14。

本包整合**资源的使用方式与证据结构**，不是把所有公开 marker 合并成一个自动分类器。包含分层人工精选面板、来源登记、来源冲突核验、基因可测性审计和上游规则导入器。完整上游数据库不随包再分发，参考图谱不随包下载。没有患者数据、项目细胞矩阵、供者信息或私有分析结果。

**当前规则版本：1.3.0。** [逐类型规则总则](references/rulebook.md) → [谱系与递质](references/rules-identity.md) → [区域亚型与程序](references/rules-contextual.md)。39个面板、77个基因均有来源与用途记录。NRGN新增为辅助；RIT2和GALNTL6分别登记为文献支持的表达程序，见[新增规则](references/rules-study-programs.md)。最终身份以正式cluster/subcluster整体鉴定为准，成员统一继承cluster标签；逐细胞表达与参考仅辅助核验。程序面板不等于固定细胞类型，暂无经过独立评估的缺失补救组合。

## Excel 下载

[下载细胞鉴定 marker 与参考来源 Excel（v1.3.0）](https://github.com/MiaoranZhang/zmr-neuron-markers/raw/refs/heads/main/downloads/zmr-neuron-markers-v1.3.0-marker-tables.zh-CN.xlsx)

包含7个工作表：神经元大类与递质、脑区限制亚型、亚群与表达特征、非神经元排查、规则依据与冲突、参考文献与版本、逐基因来源。覆盖39项规则、77个基因及131条逐来源记录，支持筛选和冻结表头。Excel为2026-10-18的v1.3.0静态快照，不改变规则逻辑；后续规则更新不会自动改写该文件。

## 使用

下载完整仓库目录，作为 `zmr-neuron-markers` 放入你的 Codex skills 目录；保留 scripts/references/assets/agents 子目录。在新对话中可调用 `$zmr-neuron-markers`。入口是 [SKILL.md](SKILL.md)。

示例请求：

> 使用 $zmr-neuron-markers，基于未整合表达核验这个成人中脑神经元簇的递质身份；比较来源规则与匹配参考，保留不确定细胞，不修改原始对象。

## 文件

- [细胞类型 × 核心/辅助marker及参考来源汇总](references/celltype-marker-tables-v1.3.0.zh-CN.md)：四类总表、39项规则、77个基因与131条逐来源记录；含适用范围、组合依据及竞争marker。整理于2026-10-18，仅补充文档，不改变v1.3.0鉴定规则。

- `assets/curated_panels.json`、`assets/curated_marker_assertions.tsv`：本项目原创组织的精选审阅面板与逐基因事实索引，不是上游原始规则全文。
- `assets/source_registry.json`：8个来源ID及其论文、固定commit、使用边界和许可状态。
- [marker文献索引](references/marker-literature.md)、`assets/marker_literature.tsv`：全部77个基因的逐来源参考文献、DOI、定位及实际用途；原始研究与数据库聚合来源分别标记。
- `assets/source_conflicts.tsv`：不能盲目合并的具体条目。
- `assets/rules/`、`assets/rulebook_manifest.json`：与面板一一对应的原创审阅规则，保留来源组合与编辑推论的区别。
- `references/`：鉴定流程、来源指南和数据字段。
- `scripts/`：本地导入、覆盖度审计及离线验证。
- `tests/`：缺失不等于阴性、脑区限制、替代规则、重复简称等行为测试。

核心本地工具只用 Python 标准库；ScType Excel 导入额外需要 pandas/openpyxl，版本由操作者核验，不自动安装。工具不执行上游代码，不上传表达数据。

```text
python scripts/validate_package.py
python -m unittest discover -s tests -v
python scripts/review_rules.py --validate
python scripts/review_rules.py --template da-core
python scripts/review_rules.py --evidence YOUR_REVIEW.json
python scripts/audit_coverage.py --genes genes.txt --region midbrain --species human --output marker_coverage.tsv
```

## 许可与限制

本项目原创说明和代码采用 [MIT](LICENSE)。第三方来源有各自条款，不能以本包 MIT 许可覆盖它们，见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。精选事实面板是审阅起点，不是独立队列验证、校准概率或完整亚型分类。版本冻结仅保障可追溯，不保障生物学准确性。

`review_rules.py` 只检查操作者填写的证据是否满足规则，不从矩阵自动识别细胞，也不验证证据附件的真实性。High 是有条件的审阅等级，不是已知准确率；跨供者复现和独立验证分别报告。
