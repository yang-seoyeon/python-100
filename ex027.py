
names = input('이름을 입력하세요: ').split()
maths = list(map(int, input('수학 점수를 입력하세요: ').split()))

dictionary = dict(zip(names, maths))

print(names)
print(maths)
print(dictionary)
