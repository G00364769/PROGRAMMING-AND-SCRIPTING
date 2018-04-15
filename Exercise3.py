
#adarsha sachan
# exercise 3 Collatz conjecture
i=int(input("Please enter the value"))
while i!=1:
  #print(i)
  # if divide by 2 if even, multiply by three and 1 if odd 
  if (i % 2)==0:
      i = int(i / 2)
      #print(i)
  else:
      i=(i*3) +1
      #print(i)
  print(i)
