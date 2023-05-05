# Import math Library
import math

# Return the cosine of different numbers
print (math.cos(0.00))
print (math.cos(-1.23))
print (math.cos(10))

# Return the sine of different values
print (math.sin(0.00))
print (math.sin(-1.23))
print (math.sin(10))
print (math.sin(math.pi))
print (math.sin(math.pi/2))

# Return the sine value of 30 degrees
print(math.sin(math.radians(30)))

# Return the sine value of 90 degrees
print(math.sin(math.radians(90)))

# Return the tangent of different numbers
print (math.tan(90))
print (math.tan(-90))
print (math.tan(45))
print (math.tan(60))

# Round a number upward to its nearest integer
print(math.ceil(1.4))
print(math.ceil(5.3))
print(math.ceil(-5.3))
print(math.ceil(22.6))
print(math.ceil(10.0))

#Return factorial of a number
print(math.factorial(9))
print(math.factorial(6))
print(math.factorial(12))

# Convert different degrees into radians
print(math.radians(180))
print(math.radians(100.03))
print(math.radians(-20))

# Return the tangent of different numbers
print (math.tan(90))
print (math.tan(-90))
print (math.tan(45))
print (math.tan(60))

while True:
    import math

    x = float(input("Enter number1:"))
    y = float(input("Enter number2:"))

    op = input("Enter operator:")
    if op == "+":
        z = x+y
        print(z)
  
        op = input("Enter operator:")
        if op == "-": 
              z = x-y
              print(z)

              op = input("Enter operator:")
        if op == "*":
              z = x*y  
              print(z)

              op = input("Enter operator:")
        if op == "/":  
         z = x/y    
         print(z)

        op= input("continue?....Y/N")
        
        if  z == "N":
           break
        
