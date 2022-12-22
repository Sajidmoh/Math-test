import random


def getMathQuestion():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = str(number1) + " + " + str(number2)
    answer = number1 + number2
    print(question)
    givenAnswer = int(input("enter your answer: "))
    if answer == givenAnswer:
        print("your answer is correct")
    else:
        print("incorrect")


def getBegining():
    questionCount = random.randint(5, 10)
    print("there are ", questionCount, " question in your test")
    print("         y or n ")
    check = input("are you ready to start: ")
    if check == "y":
        for i in range(questionCount):
            getMathQuestion()
    elif check == "n":
        print("come back when youre ready")
        exit()
    else:
        print("you typed an ivalid input please try again")
        getBegining()


getBegining()
