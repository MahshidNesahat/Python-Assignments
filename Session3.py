# Import math Library
while True:
   import math


   num1 = float(input("Enter first number: "))
   op = (input("Enter operator: "))
   num2 = float(input("Enter second number:" ))

   if op == "+":
    print(num1 + num2)
   elif op == "-":
    print(num1 - num2)
   elif op == "/":
    print(num1 / num2)
   elif op == "*":
    print(num1 * num2)   

   if op == "cos":
    print (math.cos(num1))

   elif op == "tan":
    print (math.tan(num1))

   elif op == "sin":
    print (math.sin(num1))

   elif op == "factorial":
     print(math.factorial(num1))
   
   elif op == "radians":
    print(math.radians(num1))
   print("Invalid operator")
 
    