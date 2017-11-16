import random
a= random.sample(range(100),16)

def get_fl():
  
  c=[]
  c.append(a[0])
  c.append(a[len(a)-1])
  
  print(c)
  
get_fl()
