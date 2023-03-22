import random
number = random.randint(1,50)
chances = 5

while chances > 0:
    guess = int(input("Enter the number"))

    if guess == number :
        print(f" CONGRUTULATIONS YOU WON! {number}")
        break

    if guess < number:
        print(f"The number is too low {guess}") 
    else:
        print(f"The number is too High {guess}")

    chances-=1
    if chances > 0:
        print(f"you have left with {chances} chances")
    else:
        print(f"sorry you lost the game the correct number is {number}")    

