# 문제19 : 제곱을 구하자

#공백으로 구분하여 두 숫자 a와 b가 주어지면, a의 b승을 구하는 프로그램을 작성하세요.

# >>입력
3 2

# >>출력
9

# ------------------------------

a, b = map(int, input('숫자 두개를 입력하세요.').split())
s = a ** b

print(s)