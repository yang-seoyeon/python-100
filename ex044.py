n = input('양의 정수를 입력하세요: ')
list_1 = []
score = 0
for i in range(1, len(n) + 1, 1):
    list_1.append(n[i - 1 : i])
    s = int(list_1[i - 1])
    score += s
print(score)

#-----------------

# n = input('양의 정수를 입력하세요: ')
s = set(n)
print(s)
l = list(n)
print(l)

ns = list(map(int, l))
print(ns)

print(sum(ns))

#----------------------
