import random
from time import time
score = 0
questionCount = random.randint(1, 3)
operators = []


print("there are ", questionCount, " question in your test")
print("         y or n ")
check = input("are you ready to start: ")
if check == "y":
    start = time()
    for i in range(questionCount):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        question = str(number1) + " + " + str(number2)
        answer = number1 + number2
        print(question)
        givenAnswer = int(input("enter your answer: "))
        if answer == givenAnswer:
            print("your answer is correct")
            score += 1
        else:
            print("incorrect")
    end = time()        
elif check == "n":
    print("come back when youre ready")
    exit()
else:
    print("you typed an ivalid input please try again")
   
timeTaken = end - start
print(f"timetaken: {timeTaken} " )
print("your score was",score,"out of ",questionCount)
