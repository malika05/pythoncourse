f = open("C:/Users/User/Desktop/python.txt.txt", 'r', encoding = 'utf-8')
s = f.read()
n = sum(map(int, f))
print(s,n)

