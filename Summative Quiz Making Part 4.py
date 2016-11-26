file = open("Quiz4", "r")
file2= open("Quiz4answers", "r")
name=""
Score=0

name=input("\n""What is your name?")
print("Welcome",name,"Looks like you are taking this Knowledge test, have fun!(Calculators are not allowed)")
Score=0
Questionasked=0
Questionnumber=0

def askquestion(Questionnumber):
    global Questionasked
    while Questionasked >= 0 and Questionasked < 17:
        global Score
        print(file.readline())
        answer=input("Enter Letter")
        answer=answer.upper
        realanswer=file2.readline()
        realanswer=realanswer[0]
