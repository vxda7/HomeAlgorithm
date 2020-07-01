temp = [1]*10000000
this = [0]*10000000
for i in range(1000000):
    this[i] = temp[i] * 2

print(this[999999])