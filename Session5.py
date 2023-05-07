import random
number = random.randint(1,10)
chance = 3
count = 0
print("guess a number between 1 and 10 :")
while count < chance :
    guess = int(input())
    if guess == number :
        print("you won!")
        break
    elif guess < number :
        print("guess a higher number")
    else:
        print("guess a lower number")
        count +=1
        if count >= chance:
            print("you lose! number is",number)

