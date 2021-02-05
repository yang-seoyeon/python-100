n = list(map(int,input('숫자 10개를 입력하세요: ').split()))

max_n = 0
for i in range(len(n)):
    if n[i] > max_n:
        max_n = n[i]

print(max_n)


print(max(n))