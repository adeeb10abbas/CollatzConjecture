n = int(input())
counter = 0


while n>1:
  counter = counter +1
  if n%2 == 0:
    n = n//2
    
    if n == 1:
      print("n is 1 after", counter, "steps")
  elif n%2 != 0:
    n = 3*n + 1
    
    if n == 1:
      print("n is 1 after", counter, "steps")

  
