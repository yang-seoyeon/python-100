def bubble(n, data):
    for i in range(n-1):
        for j in range(n-1-i):
            if data[j] > data[j+1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    for i in range(n):
        print(data[i], end = " ")

n = int(input())
data = list(map(int, input().split()))

data_sort = data.copy()
bubble(n, data)

data_sort.sort()
print(data_sort)

data_sort.reverse()
print(data_sort)