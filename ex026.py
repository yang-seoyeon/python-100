p = input('헹성 이름을 한글로 입력하세요: ')

if p == '수성':
    print('Mercury')
elif p == '수성':
    print('Venus')
elif p == '수성':
    print('Earth')
elif p == '수성':
    print('Mars')
elif p == '수성':
    print('Jupiter')
elif p == '수성':
    print('Saturn')
elif p == '수성':
    print('Uranus')
elif p == '수성':
    print('Neptune')

planet = {'수성':'Mercury', '금성':'Venus', '지구':'Earth', '화성':'Mars', '목성':'Jupiter', '토성':'Saturn', '천왕성':'Uranus', '해왕성':'Neptune'}
print(planet[p])