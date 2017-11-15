from random import randint


game= True

n=randint(0, 9)

#print(n)

counter=0 

while game == True:


  
  

  a=input("Guess a number or type exit to finish")
  
  
  
  if a == "exit":
    print("you did not finish and you used " + str(counter) + " trie(s)")
        
    break
  
  a= int(a)
  
  
  if n > a:
    print("Too low")
    counter = counter +1
    
  elif n < a:
    print("Too high")
    counter = counter +1
    
  elif n == a:
    counter = counter +1
    print("Correct with " + str(counter) + " trie(s)" )
    answer=input("do you want to play again yes or no ")
    if answer == "yes":
      print("You get a new random number and your counter is back to 0")
      n=randint(0, 9)
      counter = 0
    else:
      print("Thank you for playing")
      game = False
    
