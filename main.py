import random
from time import time
import statistics

score = 0
operators = ["*", "/", "+", "-"]

# List for time taken values
timeTakenList = []
timeTakenForAdd = []
timeTakenForSub = []
timeTakenForDiv = []
timeTakenForMul = []

scores ={
    "add":0,
    "sub":2,
    "mul":0,
    "div":0
}

questionsCount = {
    "add":0,
    "sub":0,
    "mul":0,
    "div":0
}

accuracy = {
    "add":100,
    "sub":100,
    "mul":100,
    "div":100
}



def handleQuestion(questionCount):
     global score
     for i in range(questionCount):
        start = time()
        
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operator = random.choice(operators)
        
        if operator == "*":
            number2 = random.randint(1, 10)
            questionsCount["mul"]+=1
            
        elif operator == "/":
            number1 = number2 * random.randint(1, 10)
            questionsCount["div"] += 1
            
        elif operator =="-":
            questionsCount["sub"] += 1
            
            if number1 < number2 :
                number1 , number2 = number2 , number1
                
        else:
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
                scores["add"]+=1
                timeTakenForAdd.append(time_taken)
            elif operator == "-":
                timeTakenForSub.append(time_taken)
                scores["sub"] +=1
            elif operator == "/":
                timeTakenForDiv.append(time_taken)
                scores["div"] += 1
            elif operator == "*":
                timeTakenForMul.append(time_taken)
                scores["mul"] +=1
            print("your answer is correct")
            score += 1
        else:
            print("incorrect")



            # ----------------------------------

            
# start
while True :
    questionCount = random.randint(5,10)            
    print("there are ", questionCount, " question in your test")
    print("         y or n ")
    check = input("are you ready to start: ")
    
    if check == "y":
       handleQuestion(questionCount)
            
    elif check == "n":
        print("come back when youre ready") #40 +1 10-21 21-30
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
    
    for i in questionsCount:
        if not questionsCount[i] == 0 :
            accuracy[i] = (scores[i] / questionsCount[i] ) * 100
            
    print()
    print("Conclusions")
    print()
    
    
    accLst = []
    
    for i,j in accuracy.items():
        accLst.append([j,i])
    
    accLst.sort()
    
    minAcc = accLst[0][1]
    
    print("practice more"  , minAcc)
        
    
    print("... More .. -> Comming Soon")
        
    print()
    print("Results :")
    print("------------------------------------")
    print()
    print("---Accuracy values---")
    print()
    print(f"Your accuracy is : {acc}%")
    print()
    print(f"Accuracy for addition : {accuracy['add']}")
    print(f"Accuracy for subtraction : {accuracy['sub']}")
    print(f"Accuracy for Divivsion : {accuracy['div']}")
    print(f"Accuracy for Multiplication : {accuracy['mul']}")
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
    
    repeat = input(f"Would you like to repeat the test with harder ")
    print(minAcc)
    print()
    print("                y or n")
    if repeat ==  "y":
        print("Okay then practice!")
        operators.append("-")
    else :
        print("Be serious in your calculations")
        break
        