def nameit():
  a= str(input("give me a sentence "))
  
  print(" ".join(a.split(" ")[::-1]))
  
  
nameit()  
