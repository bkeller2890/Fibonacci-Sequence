#Benjamin Keller
#Fibonacci Sequence 

number = int(input()) 

def fib_sequence(x)
  if x in {0,1}: 
    return x
  else: 
    return fib_sequence(x-1)+fib_sequence(x-2) 

for i in range(number): 
  print(fib_sequence(i))
