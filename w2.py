import json
a = dict()
a['apartament'] = dict()
a['apartament']['furniture'] = 28000
a['apartament']['electricity'] = 800
a['apartament']['water'] = 500
a['apartament']['gas'] = 600

b = json.dumps(a, indent = 4)
s = (28000+800+500+600)/4
print(b,s)

