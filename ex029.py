

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ss = 'abcdefghijklmnopqrstuvwxyz'
b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
bb = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

i = input('대문자를 입력하세요: ')
if i in s:
    print('NO')
if i in b:
    print('YES')
if i in ss:
    print('NO')
if i in bb:
    print('YES')
if i.isupper():
    print('YES')
else:
    print('NO')

