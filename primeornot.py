n=int(input("Number please"))
x=range(2,n)


a=[n % i for i in x]

if 0 in a:
  print("Not a prime")

elif n==1:
  print("Not a prime")
  
else:
  print("prime")
