n = list(map(int, input('숫자를 입력하세요: ').split()))

a = n.copy()
rn = a.reverse()
print(a)
print(n)


# for i in range(len(n)):
#    print(n.pop())

#print(n)

class abc:
    def __init__(self, l):
        self.l = l

    def reverse(self):
        self.l.reverse()
        return self.l

    def __str__(self):
        return str(self.l)

b = abc(n)
print(b)
b.reverse()
print(b)
print(b.reverse())

