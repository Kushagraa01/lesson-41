def recurfactorial(n):
   if n==1:
     return n
   else:
    return n*recurfactorial(n-1)
num=int(input("Enter the number"))
if num < 0:
  print("Sorry, Factorial does not exist for negitive numbers.")
elif num==0:
  print("The factorial of 0 is 1")
else:
  print("The factorial of",num,"is",recurfactorial(num))