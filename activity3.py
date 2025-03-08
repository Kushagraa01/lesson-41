def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

num1=int(input("Enter the first number"))
num2=int(input("Enter the secound number"))

print("Sum of",num1,"and",num2,"is",add(num1,num2))
print("Difference of",num1,"and",num2,"is",subtract(num1,num2))
print("Product of",num1,"and",num2,"is",multiply(num1,num2))
print("Quotient of",num1,"and",num2,"is",divide(num1,num2)) 