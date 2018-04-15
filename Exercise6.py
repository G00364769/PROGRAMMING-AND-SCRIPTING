#adarsha sachan
#Exercise 6 factorial function
#factorial() that takes a single input/argument which is a positive integer and returns its factorial. 
x=int(input("Please enter the value"))
def facrorial(x):
  i=1
  for j in range (i,x+1):
    i=i*j
  return (i)
print (facrorial(x))

