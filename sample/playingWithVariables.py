a = 10
print(a)
a = "someString"
print(a)


d: str = "new value of variable"
print(d)
d: int = "12"
print(d)


# The below will not work
# print(a + 12)
# The below works
print(a + str(d))