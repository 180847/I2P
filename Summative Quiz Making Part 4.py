file= open("Quiz4", "r")
file= open("Quiz4answers", "r")
name=""
Score=0

name=input("\n""What is your name?")
print("Welcome",name,"Looks like you are taking this Knowledge test, have fun!(Calculators are not allowed)")
Score=0
QUESTIONSASKED=0
QUESTIONNUMBER=0

def askquestion(QUESTIONNUMBER):
    global QUESTIONSASKED
    while QUESTIONSASKED >= 0 and QUESTIONSASKED < 18:
        global Score

