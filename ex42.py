import datetime

dates = list(map(int, input('달을 입력하세요: ').split()))
month = dates[0]
date = dates[1]

r = datetime.datetime.today().weekday()
print(r)
d = datetime.date(2021, month, date)
print(d)

weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
r = d.weekday()
print(weekdays[r])