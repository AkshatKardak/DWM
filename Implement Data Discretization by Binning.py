# Implement Data Discretization by Binning
import math
from collections import OrderedDict

print("\n\t\tSmoothing by Bin Means\n")

print("\nEnter the data:")
x = list(map(float, input().split()))

print("\nEnter the number of bins:")
bi = int(input())

x_sorted = sorted(x)
n = len(x)
bin_size = math.ceil(n / bi)
bins = []
smoothed = []

for i in range(0, n, bin_size):
    current_bin = x_sorted[i:i + bin_size]
    bins.append(current_bin)
    mean_val = round(sum(current_bin) / len(current_bin), 3)
    smoothed.append([mean_val] * len(current_bin))

print("\nNumber of data in each bin:", bin_size, "\n")

print("Partitioning elements:")
for i, b in enumerate(bins, 1):
    print("Bin", i, ":", b)

print("\nSmoothing by bin means:")
for i, b in enumerate(smoothed, 1):
    print("Bin", i, ":", b)

##Enter the data:
##1948 6026 5589 11646 8117 8882 42409 16368 235 15813 9748 14632 28322 13997 10923 8645 5671 18189 7488 7415 11527 5161 14494 24468 697 1615 9469 4832
##Enter the number of bins:
##2