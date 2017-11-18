import random
import numpy as np


def code1():
  a= np.random.choice(100, 99, replace=True)
  a=sorted(a)
  print(a)
  a=set(a)
  a= list(a)
  a =sorted(a)
  print(a)



def code2():
  a= np.random.choice(100, 99, replace=True)
  b=[]
  for i in a:
    if i not in b:
      b.append(i)
  
  b=sorted(b)
  print(b)
  
  
  
code1()
code2()

