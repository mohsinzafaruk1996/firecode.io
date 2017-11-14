play = True

while play:


  
  print("Draw Please choose again")
  a = str(input("R, P, S"))
  b = str(input("R, P, S"))
  if a == b :
    print ("Draw")
    
  if a == str("R") and  b == str("P"):
    print ("Paper wins")
  
  elif a == str("R") and  b == str("S"):
    print ("Rock wins")

  elif a == str("P") and  b == str("R"):
    print ("Paper wins")
  
  elif a == str("P") and  b == str("S"):
    print ("Scissor wins")

  elif a == str("S") and  b == str("R"):
    print ("Rock wins")
  
  elif a == str("S") and  b == str("P"):
    print ("Scissor wins")
  
  again=str(input("Do you want to play again, type yes or no "))
  if again == "no":
    print("Have a nice day")
    play = False  
  
