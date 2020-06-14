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