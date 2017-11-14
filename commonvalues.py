import random 
ainp = int(input("how big is the first array"))
binp = int(input("how big is the second array"))
a=random.sample(range(1,100), ainp)
b=random.sample(range(1,100), binp)

common=[]

for i in a:
  if i in b:
    common.append(i)
    print(i)
  

print(common)
