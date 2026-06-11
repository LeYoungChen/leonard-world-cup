# Leonard World Cup（世界杯比赛预测器）

一个可跨 agent 移植的 Skill / 工作流，用于基于**实时公开信息**、**市场隐含概率**和**可解释的足球建模**，估算 FIFA 世界杯比赛 90 分钟内的胜 / 平 / 负概率。

> 英文说明见 [README.md](README.md)。

## 它做什么

- 为每场比赛检索当前公开信息。
- 对每一条实质性论断要求可点击的来源链接。
- 把 1X2 十进制赔率转换成原始隐含概率和去水（no-vig）隐含概率。
- 产出一份面向公众的简洁预测：概率表、置信度、关键理由、不确定性和来源表。
- 支持技术扩展：市场 vs 模型对比、证据权重表、敏感性分析、JSON 输出。
- 拒绝投注建议、注码管理、博彩平台推荐和"稳赚"话术。

## 它不做什么

- 不预测具体比分（如"2:1"）——必要时给进球分布草图，而不是单一自信比分。
- 不做"谁夺冠"的全程赛事模拟——晋级/夺冠是另一个目标，会明确说明并收敛到单场。
- 不做比赛进行中的实时滚动更新——工作流假设赛前公开数据。
- 不提供投注执行——注码、资金分配、平台选择、套利或任何"稳赚"框架一律重定向。

## Skill 位置

```text
skills/leonard-world-cup/
```

- `SKILL.md`：核心规则、适用范围、工作流。
- `references/modeling.md`：概率方法、去水转换、研究谱系、评估指标。
- `references/public-positioning.md`：公开措辞与安全边界。
- `references/output-formats.md`：表格、可视化与 JSON schema。
- `references/checklist.md`：交付前的硬约束自检清单。
- `scripts/normalize_odds.py`：确定性的赔率转换工具。

## 示例

```text
用 $leonard-world-cup 估算阿根廷 vs 法国 90 分钟胜/平/负概率，并附可点击来源。
```

## 赔率工具

```bash
python3 skills/leonard-world-cup/scripts/normalize_odds.py 1.80 3.60 4.80
```

输出 JSON 包含：输入赔率、原始隐含概率、过水值（overround）、去水概率，以及校正到合计 100% 的百分比。

该脚本是**可选项**。Skill 也能按 `references/modeling.md` 里的步骤手动完成同样的去水转换。

## 纯 Markdown 版本（用于只接受 `.md` / `.txt` 的平台）

部分平台（如小红书）只接受 Markdown / 文本文件，不接受 `.py` 和 `.yaml`。用下面的命令生成一份只保留 Markdown 内容、去掉 `scripts/` 和 `agents/` 的副本：

```bash
scripts/build-xhs-package.sh
# 输出：dist/leonard-world-cup/
```

其余无需改动——赔率改用 `references/modeling.md` 的步骤手算。

## 安全边界

这个工作流用于**概率预测和证据解释**。它不是投注建议、不是金融建议、不做注码管理，也不是自动下注系统。

## 测试

```bash
python3 -m unittest discover -s tests -v
```
