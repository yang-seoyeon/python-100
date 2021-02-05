s = input('영어 문자열을 입력하세요: ')

result = ''
for i in range(len(s)):
    if s[i].isupper():
        result += s[i].lower()
    else:
        result += s[i].upper()

print(result)