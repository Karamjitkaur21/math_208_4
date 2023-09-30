import numpy as npy
import matplotlib.pyplot as plt

# calculate mean
def calculate_mean(data):
    return sum(data) / len(data)

# calculate median
def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        mid1 = sorted_data[n // 2]
        mid2 = sorted_data[n // 2 - 1]
        median = (mid1 + mid2) / 2
    else:
        median = sorted_data[n // 2]
    return median

# calculate standard deviation
def calculate_std_dev(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return std_dev

# Generate 500 random numbers with mean = 10 and std deviation = 0.5
mean = 10
std_dev = 0.5
random_data = npy.random.normal(mean, std_dev, 500)

# mean, median, and standard deviation
mean_value = calculate_mean(random_data)
median_value = calculate_median(random_data)
std_dev_value = calculate_std_dev(random_data)

# Plot histogram with 10 bins
plt.hist(random_data, bins=10, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of 500 Random Numbers (Mean=10, Std Dev=0.5)')
plt.grid(True)

# Print the calculated statistics
print(f"Mean: {mean_value:.2f}")
print(f"Median: {median_value:.2f}")
print(f"Standard Deviation: {std_dev_value:.2f}")

# Show the plot
plt.show()
