import json
a = dict()
n=1
while n==1:
    name = str(input())
    age = str(input())
    grade = str(input())
    shool = str(input())

    a[name] = dict()
    a[name]['age'] = age
    a[name]['grade'] = grade
    a[name]['shool'] = shool

    n = int(input())

res = json.dumps(a, indent=4)
print(res)