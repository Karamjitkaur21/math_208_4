import numpy as np
import matplotlib.pyplot as plt

# calculate mean
def calculate_mean_data(data):
    return sum(data) / len(data)

# calculate median
def calculate_median_data(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        mid1 = sorted_data[n // 2]
        mid2 = sorted_data[n // 2 - 1]
        median = (mid1 + mid2) / 2
    else:
        median = sorted_data[n // 2]
    return median

# standard deviation
def calculate_std_dev(data):
    mean = calculate_mean_data(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return std_dev

# Generate 500 random numbers between -20 and 20
random_data = np.random.uniform(-20, 20, 500)

# Calculate mean, median, and standard deviation
mean_value = calculate_mean_data(random_data)
median_value = calculate_median_data(random_data)
std_dev_value = calculate_std_dev(random_data)

# Plot a histogram with 10 bins
plt.hist(random_data, bins=10, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of 500 Random Numbers')
plt.grid(True)

print(f"Mean: {mean_value:.2f}")
print(f"Median: {median_value:.2f}")
print(f"Standard Deviation: {std_dev_value:.2f}")

# Show plot
plt.show()
