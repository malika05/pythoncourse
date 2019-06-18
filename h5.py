import re
a = 'id:2; name:Nastya; age:20; sex:female'
print(re.findall(r'\w+', a))
