import random
from time import time
import statistics

score = 0
questionCount = random.randint(2, 5)
operators = ["*", "/", "+", "-"]
# List for time taken values
timeTakenList = []
timeTakenForAdd = []
timeTakenForSub = []
timeTakenForDiv = []
timeTakenForMul = []

# variables for score values 
scoreForAdd = 0
scoreForSub = 0
scoreForMul = 0
scoreForDiv = 0

# variable to calcualte question count 

questionCountForAdd = 0
questionCountForSub = 0
questionCountForDiv = 0
questionCountForMul = 0

questionsCount = {
    "add":0,
    "sub":0,
    "mul":0,
    "div":0
}

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
            questionCountForMul += 1
        elif operator == "/":
            number1 = number2 * random.randint(1, 10)
            questionCountForDiv += 1
        elif operator =="-":
            questionCountForSub += 1
            if number1 < number2 :
                number1 , number2 = number2 , number1
        else:
            questionCountForAdd+=1
            questionsCount["add"] += 1
        question = str(number1) + operator + str(number2)
        answer = eval(question)
        print(question)
        givenAnswer = int(input("enter your answer: "))
        end = time()    
        time_taken = end-start
        timeTakenList.append(time_taken)
        
        if answer == givenAnswer:
            if operator == "+":
                scoreForAdd+=1
                timeTakenForAdd.append(time_taken)
            elif operator == "-":
                timeTakenForSub.append(time_taken)
                scoreForSub +=1
            elif operator == "/":
                timeTakenForDiv.append(time_taken)
                scoreForDiv += 1
            elif operator == "*":
                timeTakenForMul.append(time_taken)
                scoreForAdd +=1
            print("your answer is correct")
            score += 1
        else:
            print("incorrect")
        



elif check == "n":
    print("come back when youre ready")
    exit()
else:
    print("you typed an ivalid input please try again")

acc = (score/questionCount)*100
timeTaken = sum(timeTakenList)

averageTimeTaken = statistics.getMean(timeTakenList)
standardDeviation = statistics.getStandardDeviation(timeTakenList)

# mean of timeTaken for specific type of questions ( operators )
meanTimeForAdd = statistics.getMean(timeTakenForAdd)
meanTimeForSub = statistics.getMean(timeTakenForSub)
meanTimeForDiv = statistics.getMean(timeTakenForDiv)
meanTimeForMul = statistics.getMean(timeTakenForMul)

# accuracy for each type of question ( operator )
if questionsCount["add"] == 0 :
    accForAdd = 100
else:
    accForAdd = (scoreForAdd/questionsCount["add"] ) * 100

if questionCountForSub == 0 :
    accForSub = 100
else:
    accForSub = (scoreForSub /questionCountForSub) *100

if questionCountForDiv == 0:    
    accForDiv = 100
else: 
    accForDiv = (scoreForDiv / questionCountForDiv) * 100  #Output

if questionCountForMul == 0 :
    accForMul = 100
else:
    accForMul = (scoreForMul/questionCountForMul) * 100

print()
print("Conclusions")
print()
print("Comming Soon")
print()
print("Results :")
print("------------------------------------")
print()
print("---Accuracy values---")
print()
print(f"Your accuracy is : {acc}%")
print()
print(f"Accuracy for addition : {accForAdd}")
print(f"Accuracy for subtraction : {accForSub}")
print(f"Accuracy for Divivsion : {accForDiv}")
print(f"Accuracy for Multiplication : {accForMul}")
print()
print("---Mean Values---")
print()
print(f"Mean time taken per question: {averageTimeTaken}")
print()
print(f"Mean Time For Addition: {meanTimeForAdd}"  )
print(f"Mean Time For Subtraction: {meanTimeForSub}")
print(f"Mean Time For Multiplication: {meanTimeForMul}")
print(f"Mean Time For Division: {meanTimeForDiv}")
print()
print("---Additional Details---")
print()
print(f"standard deviation is {standardDeviation}")
print(f"timetaken: {timeTaken} ")
print("your score was", score, "out of ", questionCount)

