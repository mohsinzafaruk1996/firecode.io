import random
import string
list(string.ascii_lowercase)
def nameit():
  a= str(input("how strong W or S? "))
  b=[]
  if a == "W":
    a=["bala","silly", "vain"]
    
    b.append(random.choice(a))
    b1 = ''.join(b)
    
    
  else:
    n=int(input("How long should yuor password be ? (8-25) "))
    c= string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    d=list(c)
    b=random.sample(d, n)
    b1 = ''.join(b)
  print(b1)    


nameit()


