
import random
print("Hello User\n")

while True:
    roll_again = "yes"
    while roll_again == "yes" or roll_again == "y":
     roll_again = random.randint(1,6)
     
     print("daram taas mindazam.......")
     print("maghader shoma shod:")
   
    
    print(roll_again)
    if roll_again == 6:
        continue
    
    else:
       
         roll_again = input("Dobare tass bendazam??")

    if roll_again == "No":
     break

        
  
