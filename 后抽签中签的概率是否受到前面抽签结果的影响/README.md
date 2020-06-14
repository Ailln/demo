# 后抽签中签的概率是否受到前面抽签结果的影响

> 某人参加一档电视节目，很幸运地获得了上台抽奖的机会。舞台上升起A、B、C三扇道具门，其中一扇门后面是一辆最新款的特斯拉，只要猜对，他就可以直接把车开走。
>
> 全场沸腾了。选任何一扇门，猜中的概率都是1/3。他犹豫了一下，选了B。这时，主持人打开了另外两扇门中的一扇，是空的。只剩下两扇门了，特斯拉必然在其中一扇门之后。主持人问：“我再额外送你一次改变的机会，你是坚持选B呢，还是选另外一扇门？”
>
> 根据统计，在这种情况下，大部分人会选择坚持。理由是：现在不管选哪一扇门，猜中的概率都是50%，既然概率一样，我还是相信直觉，坚持自己的第一选择吧。
>
>恭喜大部分人——你们都错了！正确的答案是：换。从B换成另一扇门，猜中的概率会提高一倍。很多人一定觉得很惊讶：为什么？这和直觉不符啊！事实上，人们的直觉和客观概率常常是不相符的。行为经济学家把人们自以为的概率称为“心理概率”，而心理概率和客观概率不吻合的现象，叫作“概率偏见”。
>
> 出自《一分钟商学院——全世界一半的娃都丑到了平均水平以下》刘润

## 分析

上面这个问题等同于「后抽签中签的概率是否受到前面抽签结果的影响」。

未完成。

## 代码

```python
from random import choice

# 实验次数
experiment_times = 10000
print(f"试验次数（总样本数目）: {experiment_times}\n")

samples = []
for _ in range(experiment_times):
    # 初始化实验样本，0 代表无奖励，1 代表有奖励
    sample = {"A": 0,  "B": 0, "C": 0}
    # 随机选择 ABC 其中一个
    sample[choice(["A", "B", "C"])] = 1
    samples.append(sample)

print(f"前 5 个样本: {samples[:5]}\n")

# 不管 A 如何，直接选择 B 的胜率
choose_b_times = 0
for sample in samples:
    if sample["B"] == 1:
        choose_b_times += 1

print(f"直接选择 B 的胜率: {choose_b_times / experiment_times}\n")

# A 无奖励的情况下，分别选择 B、C 的胜率
a_is_reward_times = 0
choose_b_times = 0
choose_c_times = 0
for sample in samples:
    if sample["A"] == 1:
        a_is_reward_times += 1
    else:
        if sample["B"] == 1:
            choose_b_times += 1
        if sample["C"] == 1:
            choose_c_times += 1

print(f"A 无奖励的情况下，选择 B 的胜率: {choose_b_times / (experiment_times - a_is_reward_times)}")
print(f"A 无奖励的情况下，选择 C 的胜率: {choose_c_times / (experiment_times - a_is_reward_times)}")

# 试验次数（总样本数目）: 10000

# 前 5 个样本: [{'A': 1, 'B': 0, 'C': 0}, {'A': 1, 'B': 0, 'C': 0}, {'A': 0, 'B': 1, 'C': 0}, {'A': 1, 'B': 0, 'C': 0}, {'A': 0, 'B': 1, 'C': 0}]

# 直接选择 B 的胜率: 0.3365

# A 无奖励的情况下，选择 B 的胜率: 0.5010422870756402
# A 无奖励的情况下，选择 C 的胜率: 0.49895771292435975
```
