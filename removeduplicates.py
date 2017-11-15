import random
from random import randint
a = random.sample(range(100), 16)
b = random.sample(range(101), 10)

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(a)

c1=[i for i in a if i in b]

d1=[]



c1.sort()

for i in c1:
  if i not in d1:
    d1.append(i)
    
    

d1.sort()
print(c1)
print(d1)
