# 문제15 : 자기소개

#신학기가 시작되고, 아이들이 돌아가면서 자기소개를 하기로 했습니다.
#만약 입력으로 김다정이라는 이름이 주어지면

안녕하세요. 저는 김다정입니다.

#라고 출력하게 해주세요.

# >>입력
김승주

# >>출력
안녕하세요 저는 김승주입니다.

# ------------------------------

s = input('이름을 입력해주세요.')
print("안녕하세요. 저는 {}입니다.".format(s))