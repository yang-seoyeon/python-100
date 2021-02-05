twenty = '1234567891011121314151617181920'
score = 0
for i in range(len(twenty)):
    t = twenty[i - 1]
    score += int(t)

print(score)

#-----------
twenty_list = list(twenty)
twenty_map = list(map(int, twenty_list))
twenty_sum = sum(twenty_map)
print(twenty_sum)

#-----------

print(sum(list(map(int, list(twenty)))))