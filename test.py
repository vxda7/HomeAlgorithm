this = {'봄': {}, '여': {'울': {}}}
print(this['봄'])

try:
    this['호']
    print('hmm')
except:
    print('yeap')

# print(dict([0]))

try:
    this['봄']
    print("True")
    if this['봄'] == {}:
        print('ㅗ')
except:
    print("false")
