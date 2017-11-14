a = str(input("Give me a string please"))

#print(a[::-1])

print(a[0:int(len(a)/2)+1])

#print(a[int(len(a)/2)::])
a1=a[int(len(a)/2)::]
#print(a1)
a1 = a1[::-1]
print(a1)

if a1== a[0:int(len(a)/2)]:
  print("It's a palindrome  " + a)
  
if a1 == a[0:int(len(a)/2)+1] :
  print("It's a palindrome  " + a)
  
  
    
wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")  
  
  
