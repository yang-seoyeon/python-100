def one(n):
    def two(p):
        return p ** n
    return two

a = one(2)
b = one(3)
c = one(4)
d = one(5)

print(a(10))
print(b(10))
print(c(10))
print(d(10))

def pow2(n):
    return n**2

def pow3(n):
    return n**3

def pow4(n):
    return n**4

def pow5(n):
    return n**5

print(pow2(10))
print(pow3(10))
print(pow4(10))
print(pow5(10))