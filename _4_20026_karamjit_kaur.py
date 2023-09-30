import numpy as npy
from collections import Counter

# Data
data = [
    11, 14, 15, 15, 16, 16, 17, 18, 19, 21, 25, 36,
    12, 14, 15, 15, 16, 16, 17, 18, 19, 21, 25, 39,
    13, 14, 15, 15, 16, 17, 17, 18, 20, 22, 26, 43,
    13, 14, 15, 15, 16, 17, 17, 18, 20, 22, 26, 46,
    13, 14, 15, 16, 16, 17, 17, 18, 20, 22, 27, 50,
    13, 14, 15, 16, 16, 17, 17, 19, 20, 23, 27, 54,
    13, 14, 15, 16, 16, 17, 18, 19, 20, 23, 29, 59,
    13, 15, 15, 16, 16, 17, 18, 19, 20, 23, 30, 67,
    14, 15, 15, 16, 16, 17, 18, 19, 21, 24, 31,
    14, 15, 15, 16, 16, 17, 18, 19, 21, 24, 34, 
]

# Calculate statistics
median = npy.median(data)
mode_count = Counter(data)
mode = [k for k, v in mode_count.items() if v == mode_count.most_common(1)[0][1]][0]
q1 = npy.percentile(data, 25)
q3 = npy.percentile(data, 75)
p10 = npy.percentile(data, 10)
p95 = npy.percentile(data, 95)

# Print the results
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Q1 (25th percentile): {q1}")
print(f"Q3 (75th percentile): {q3}")
print(f"P10 (10th percentile): {p10}")
print(f"P95 (95th percentile): {p95}")
