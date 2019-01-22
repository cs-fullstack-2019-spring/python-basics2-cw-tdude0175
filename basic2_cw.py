import random

def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    problem2again()
# Create a random number. Print the number.
#
# Hint:
# import random
# randomNumber = random.randint(0,9)
# easy enough


def problem1():
    print(random.randint(0,9))

# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
# if else can be used for different sequences.
# is there a way to use a for loop? x in a range of 0,2
# if user enters incorrectly x-=1?

def problem2():
    while(True):
        userInput = input("can you find the exit?!?!")
        if(userInput == "q"):
            print("YOU FOUND THE EXIT!!?!?")
            break
        else:
            print("YOU'LL BE TRAPPED HERE FOREVER!!!")


# IGNORE THIS IS WORK IN PROGRESS

def problem2again():
    for x in range(0,2):
        userInput = int(input("guess the escape number!!"))
        if(userInput == 0):
            print("you found it!")
            break
        else:
            x-=1


# Create a function that will loop until the user enters '0'.
# Ask the user to enter a positive integer number.
# Print 0 to that number and ask them again to enter a number until they enter '0'. Repeat.

# can i have some loops brother
# ignore my stupid meme comments
# switch case would be nice but pthon doesn't have that


def problem3():
    while(True):
        userInput=int(input("i need a positive number to count to."))

        if(userInput==0):
            print("wow you're no fun")
            break
        else:
            for x in range(1,userInput+1):
                print(x)

# Create a function that creates a random number.
# Ask the user to guess the random number.
# Keep letting the user guess until they get it right, then quit.
# If they don't get it right, tell them if their next guess has to be higher or lower.

# i reused the code from in class practice
#this being an example of being able to build a function for something rather than having to type it out every time
# this is a lazy approach for the graded class work which i will not deny and if i lose the point for this please let me know.



def problem4():
    targetNumber = (random.randint(1,50))
    tries = 0

    while(True):
        userInput = int(input("guess a number between 1 and 50"))
        tries+=1
        if(tries==3):
            print("sorry you lose")
            break
        elif(userInput > targetNumber):
            print("that's to high")
        elif(userInput < targetNumber):
            print("that's to low")
        elif(userInput == targetNumber):
            print("good job")
            break





if __name__ == '__main__':
    main()