a = [6,30,22,54,9]
m = a.index(max(a))
x = a.index(min(a))
a[m], a[x] = a[x], a[m]
print(a)

