import datetime
date=datetime.date.today()


name = input("What is your name?")
print ("Welcome",name,"Looks like you are taking this Knowledge test, have fun!(Calculators are not allowed)")

file = open('Quiz4', "r+")
file2 = open("Quiz4answers", "r+")
Score = 0
#r+ mean read and write
questionnumber = 0
questionsasked = 0

def askquestion(questionnumber):
    global questionsasked
    while questionsasked >= 0 and questionsasked < 17:
        global Score
        print(file.readline())
        answer = input("Input Letter")
        answer=str(answer)
        answer=answer.upper()
        realanswer=file2.readline()
        realanswer=realanswer[0]
        realanswer=str(realanswer)
        if realanswer==answer:
            Score=Score+1
            print ("You are correct. Your score is: ", str(Score))
            questionsasked=questionsasked+1
            askquestion(questionnumber + 1)
        else:
            print ("You were incorrect. The correct answer is:", realanswer)
            print ("Your score is: ", str(Score))
            questionsasked=questionsasked+1
            askquestion(questionnumber + 1)

askquestion(questionnumber)

print (name, ",", str(Score), "out of 17 was your score, completed on", date)
file3=open("Highscores", "r+")
file3.writelines(["\n", str(Score)])
file3=sorted(file3.readlines())
scoreslist=[]
for line in file3:
    scoreslist.append(line)
highscore=int(scoreslist[-1])
if Score > highscore:
    print ("You have beaten the highscore!")
else:
    print ("The highest score is:", str(highscore), "Keep trying and you may get it.")
file4=open("Highscores2", "a")
resultline=(name, "got", Score, "on", date)
resultline=str(resultline)
print (resultline)
file4.writelines(resultline)
