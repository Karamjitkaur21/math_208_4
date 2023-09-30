import matplotlib.pyplot as plt


causes = [
    "Alzheimer’s", "Chronic Respiratory Disease", "Diabetes",
    "Heart Disease", "Influenza/Pneumonia", "Malignant Neoplasms",
    "Accidents", "Nephritis/Nephrosis", "Septicemia", "Stroke"
]

deathsData = [
    83150, 88416, 72524, 631636, 56285, 559888, 121599, 49883, 34463, 135952
]

total_deathsData = sum(deathsData)


cumulative_percentage = [sum(deathsData[:i + 1]) / total_deathsData * 100 for i in range(len(deathsData))]

# Create a Pareto chart
fig, ax1 = plt.subplots()

ax1.bar(causes, deathsData, color='b', alpha=0.7, align='center', width=0.6, label='deathsData')
ax1.set_xlabel('Causes of Death')
ax1.set_ylabel('Number of deaths', color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.plot(causes, cumulative_percentage, color='r', marker='o', label='Cumulative Percentage')
ax2.set_ylabel('Cumulative Percentage', color='r')
ax2.tick_params(axis='y', labelcolor='r')

plt.title('Pareto Chart of Leading Causes of Death in 2006')
plt.xticks(rotation=45, ha="right")
plt.legend(loc='upper left', bbox_to_anchor=(0.75, 0.9))
plt.tight_layout()

plt.show()
