###### Python calculator Program ##############################
### taking two numbers as input from user and option

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choose = int(input("Enter your option : 1,2,3,4 : "))
a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
    
def add(a,b):
    print("addition of two numbers is ", a+b)
def subtract(a,b):
    print("Subtraction of two numbers is ", a-b)
def multiply(a,b):
    print("Multiplication is",a*b)
def division(a,b):
    print("Division is :", a/b)

if choose == 1:
    add(a,b)
elif choose == 2:
    subtract(a,b)
elif choose ==3:
    multiply(a,b)
else:
    division(a,b)
    
    
    
    
