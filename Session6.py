
import random

number = int (input("Enter a number:"))
array = random.sample((range(0,number * 10)),number)

print("array",array)

for i in range(len(array)):
 print(array[i])

for i in range(number):
 number = int(input("Enter nam:"))
for i in range(number):
    print("*" , end ="")

 

