import random


number = random.randint(100, 10)
def cow(n,number):
  bullcounter=0
  n_s=str(n).strip()
  a_s=str(number)
  
  for i in range(len(str(n))):#list or array
    if n_s[i]==a_s[i]:
      bullcounter= bullcounter +1
	
  
  return bullcounter
	

    


b= True

while b == True:	
  n1=int(input("Give me a number between 100 and 102"))
  cowww= int(len(str(n1))) - int(cow(n1,number))
  
  print("you have " + str(cow(n1,number)) + " cows and " + str(cowww) + " bulls "  )
  if cow(n1,number) == len(str(n1)):
    print("You beat the game well done")
    answer=input("do you want to play again yes or no ")
    if answer == "yes":
      print("You get a new random number between 100 and 102")
      number = random.randint(100, 102)
    else:
      print("Thank you for playing")
      b = False
