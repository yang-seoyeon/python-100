import sys

total_weight = int(input())
number = int(input())

weights = []
for i in range(number):
    weight = int(input())
    weights.append(weight)

print(weights)
print(sys.maxsize)

min_value = sys.maxsize
weight_sum = 0
count = 0
for i in range(len(weights)):
    min_value = min(weights)
    weight_sum += min_value
    if weight_sum > total_weight:
        break
    weights.remove(min_value)
    count += 1


print(count)