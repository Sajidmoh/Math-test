import random
from time import time
import statistics

score = 0
questionCount = random.randint(1, 3)
operators = ["*", "/", "+", "-"]
timeTakenList = []
print("there are ", questionCount, " question in your test")
print("         y or n ")
check = input("are you ready to start: ")
if check == "y":
    for i in range(questionCount):
        start = time()
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operator = random.choice(operators)
        if operator == "*":
            number2 = random.randint(1, 10)
        if operator == "/":
            number1 = number2 * random.randint(1, 10)
        question = str(number1) + operator + str(number2)
        answer = eval(question)
        print(question)
        givenAnswer = int(input("enter your answer: "))
        if answer == givenAnswer:
            print("your answer is correct")
            score += 1
        else:
            print("incorrect")
        end = time()    
        timeTakenList.append(end-start)
elif check == "n":
    print("come back when youre ready")
    exit()
else:
    print("you typed an ivalid input please try again")

timeTaken = sum(timeTakenList)
averageTimeTaken = statistics.getMean(timeTakenList)
standardDeviation = statistics.getStandardDeviation(timeTakenList)
print(f"standard deviation is {standardDeviation}")
print(f"average time taken per question: {averageTimeTaken}")
print(f"timetaken: {timeTaken} ")
print("your score was", score, "out of ", questionCount)
