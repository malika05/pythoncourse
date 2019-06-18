f = open("C:/Users/User/Desktop/python2.txt", 'r', encoding = 'utf-8')
s = f.read()
l = open("C:/Users/User/Desktop/python4.txt", 'w', encoding = 'utf-8')
l.append(f.write(s))