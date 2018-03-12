
# Adarsha sachan
# Fibonacci numbers.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 2
ans = fib(x)
print("Fibonacci number", x, "is", ans)


# exercise 2
# Adarsha sachan
def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i
fullname = "Sachan"
firstname = fullname[0]
print(firstname)

lastname= fullname[-1]
print(lastname)

first=ord(firstname)
print("my firstorder is ",first)

last=ord(lastname)
print("my lastorder is ",last)

x = first+last
ans = fib(x)
print("Fibonacci number", x, "is", ans)
