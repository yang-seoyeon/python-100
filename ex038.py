
s = list(map(int, input('시험 점수를 입력하세요: ').split()))

max_value = 0
ranking = 0
candy = 0
for i in range(len(s)):
    if max_value != max(s):
        max_value = max(s)
        ranking += 1
    if ranking > 3:
        break
    print(max(s))
    s.remove(max(s))
    candy += 1


print(candy)