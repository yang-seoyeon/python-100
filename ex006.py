# #문제 6 : False

# 다음은 파이썬 문법 중에서 False로 취급하는 것들 입니다.
# 앗, False로 취급하지 않는 것이 하나 있네요! True를 찾아주세요.

1) None
2) 1
3) ""
4) 0
5) bool(0)

# ------------------------------

# 답 : 2번

if None:
    print("None은 True")
elif 1:
    print("1은 True")
elif "":
    print('""은 True')
elif 0:
    print("0은 True")
elif bool(0):
    print("bool(0)은 True")