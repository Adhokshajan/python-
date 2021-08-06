import random


print("Number Guessing Game ")
 

number = random.randint(1,9)

print ("Guess Any Number Between 1 and 9 ")

chance = 0 

while chance < 5 :
    guess = int(input("Enter Your Guess:"))
     

    if guess==number:
        print("Congrates You Have Won!")
        break

    elif guess<number:
        print("The Guess is lower Please Guess a Higher Number ")

    else: 
        print("The Guess is Higher Please Guess a Lower Number ")

    chance +=1 


if not chance < 5 :
    print("You Have Lost The Number is " , number )

