import matplotlib.pyplot as plt

# Categories and their corresponding coverage percentages
categories = ["Graph", "Math", "Trees", "Simple", "Complex", "CPU-bounded", "String", "Io-bounded", "array"]
coverage = [100, 80, 80, 78, 62.5, 60, 60, 67, 44]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12,8))

# Bar settings
bar_width = 0.6
bar_positions = range(len(categories))

# Create bars
bars = ax.bar(bar_positions, coverage, bar_width, color='blue', alpha=0.7, label='Coverage %')

# Set the title and labels
ax.set_title('Risk Assessment of Functions across Categories')
ax.set_xlabel('Function Categories')
ax.set_ylabel('Percentage of Functions with Potential Issues (%)')
ax.set_xticks(bar_positions)
ax.set_xticklabels(categories)
ax.set_ylim(0, 110)  # 110 to make sure 100% clearly fits within the frame
ax.legend()

# Attach a text label above each bar displaying its height (optional)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height, '%d' % int(height), ha='center', va='bottom')

# Rotate x labels for better visibility if they overlap
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
