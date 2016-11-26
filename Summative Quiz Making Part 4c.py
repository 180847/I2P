import datetime
date=datetime.date.today()
from random import shuffle
x = [i for i in range(17)]
shuffle(x)
counter=0
RandomVariable1=x[counter]
#with open("Quiz4") as f:
#    questions = f.readlines()
#with open ("Quiz4answers") as g:
#   realanswers= g.readlines()
questions = [line.rstrip('\n') for line in open ("Quiz4")]
realanswers = [line.rstrip('\n') for line in open ("Quiz4answers")]
    #global realanswer

name = input("What is your name?")
print ("Welcome",name,"Looks like you are taking this Knowledge test, have fun!(Calculators are not allowed)")

#file = open('Quiz4', "r+")
#file2 = open("Quiz4answers", "r+")
Score = 0
#r+ mean read and write
questionnumber = 0
questionsasked = 0

#def askquestion(questionnumber):
#global questionsasked
while questionsasked >= 0 and questionsasked < 16:
    #global Score
    #global RandomVariable1
    #print (RandomVariable1)
    print(questions[RandomVariable1])

    answer = input("Input Letter")
    answer=str(answer)
    answer=answer.upper()
        #realanswer=file2.readline()
    correct=realanswers[RandomVariable1]
    correct=str(correct)
    #print(correct)
    #print(answer)
    if correct==answer:
        Score=Score+1
        print ("You are correct. Your score is: ", str(Score))
        questionsasked=questionsasked+1
        #askquestion(questionnumber + 1)
        counter=counter+1
        RandomVariable1=x[counter]
    else:
        print ("You were incorrect. The correct answer is:", correct)
        print ("Your score is: ", str(Score))
        questionsasked=questionsasked+1
        #askquestion(questionnumber + 1)
        counter=counter+1
        RandomVariable1=x[counter]

#askquestion(questionnumber)

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
