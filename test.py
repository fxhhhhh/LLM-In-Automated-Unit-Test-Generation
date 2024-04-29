import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

# 定义SDLC流程的开始和结束日期
start_date = datetime(2023, 9, 10)
end_date = datetime(2023, 11, 20)

# SDLC流程的阶段
phases = ["Analyzing", "Design", "Development", "Testing", "Improvement"]

# 计算总天数
total_days = (end_date - start_date).days

# 分配更多的天数给“Design”阶段，其余平分
# 假设给“Design”阶段分配30%的时间
design_duration = int(total_days * 0.30)
remaining_duration = total_days - design_duration
other_phase_duration = remaining_duration // (len(phases) - 1)

# 计算每个阶段的开始和结束日期
phase_dates = [start_date]
for phase in phases:
    if phase == "Design":
        next_date = phase_dates[-1] + timedelta(days=design_duration)
    else:
        next_date = phase_dates[-1] + timedelta(days=other_phase_duration)
    phase_dates.append(next_date)

# 准备绘图数据
data = {
    "Phase": phases,
    "Start Date": phase_dates[:-1],
    "End Date": phase_dates[1:]
}

df = pd.DataFrame(data)

# 绘制图表
fig, ax = plt.subplots(figsize=(10, 6))

# 为每个阶段绘制一个线段
for i in range(len(df)):
    ax.plot([df['Start Date'][i], df['End Date'][i]], [i, i], marker='o', markersize=6)

# 设置y轴显示阶段名称
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df['Phase'])

# 格式化图表
ax.set_title('VandyChat Project Timeline', fontsize=16)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Phases', fontsize=14)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()
