n = int(input("Give me a number, please"))

rar = range(1,n)

div = []

for i in rar:
  if n % i == 0:
    div.append(i)
    
    
print(div)
