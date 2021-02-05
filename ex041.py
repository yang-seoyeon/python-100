n = int(input('숫자를 입력하세요: '))
f = 0
for i in range(2, n):
    if n % i == 0:
        f = 1
if f == 1:
    print('NO')
else:
    print('YES')