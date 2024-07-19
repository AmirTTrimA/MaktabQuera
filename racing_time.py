def min_time_to_reach_murray_arty(k, n, a):
    total_time = 0
    for i in range(n):
        if i == 0:
            time_to_first_building = (a[i] + k - 1) // k
            total_time += time_to_first_building
        else:
            time_to_next_building = max(1, (a[i] - a[i-1] + k - 1) // k)
            total_time += time_to_next_building
    return total_time

# Read input
k = int(input())
n = int(input())
a = [int(x) for x in input().split()]

# Compute and print the minimum time
min_time = min_time_to_reach_murray_arty(k, n, a)
print(int(min_time))
