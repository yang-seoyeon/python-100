
t = list(map(int, input('키를 입력하세요: ').split()))

tt = sorted(t)

if t == tt:
    print('YES')
else:
    print('NO')

print(type(tt))

