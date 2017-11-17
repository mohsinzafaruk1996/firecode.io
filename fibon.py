def fib():
  n=int(input("how many fib numbers? "))
  
  counter=0
  a=[]
  while counter < n:
    if n == 1:
      a.append(1)
      counter=counter+1
      
      
    elif n == 2:
      a.append(1)
      a.append(1)
      counter=counter+2
      
      
    else:
      
      if counter + 2 < n :
        if 1 not in a:
          
          a.append(1)
          a.append(1)
          a.append(a[len(a)-1]+a[len(a)-2])
          counter=counter+1
          
        else:
          a.append(a[len(a)-1]+a[len(a)-2])
          counter=counter+1
          
      else:
        break
      
    
    
    
  print(a)  
    
    
fib()
