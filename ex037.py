#c = list(map(int, input('후보를 입력하세요: ').split()))
#for i in range(len(c)):
#    c.count(list(set(c))[i])

#print('{}(이)가 총 {}표로 반장이 되었습니다.').format(반장, 표수)

c = input('후보를 입력하세요: ').split()
print(c)
name = ''
max_count = 0
for a in c:
    if c.count(a) > max_count:
        name = a
        max_count = c.count(a)
print('{}(이)가 총 {}표로 반장이 되었습니다.'.format(name, max_count))


