#print("Hello world")
#name = "Nicholas Tam"
#print(name*10)
# this will print your name 10 times
#print(7)
#print(2+4)
#print(10-3)
#print(4*3)
#print(12/3)
#print(5**2)
#print("6x6="),(6*6)
#print("seconds in a week="),(7*24*60*60)

#vnumber= input ("What is your favourite sports player number")
#print("Your favourite number is recorded as: "),(vnumber),("...that is cool")

#vnum = int (input("What is your number?"))
#print(vnum),("x 1 ="),(vnum*1)
#print(vnum),("x 2 ="),(vnum*2)
#print(vnum),("x 3 ="),(vnum*3)
#print(vnum),("x 4 ="),(vnum*4)
#print(vnum),("x 5 ="),(vnum*5)
#print(vnum),("x 6 ="),(vnum*6)
#print(vnum),("x 7 ="),(vnum*7)
#print(vnum),("x 8 ="),(vnum*8)
#print(vnum),("x 9 ="),(vnum*9)
#print(vnum),("x 10 ="),(vnum*10)

#x = input("what time tables do you want to do?")
#for i in range(1,12):
    #print(x,'*',i,"=",x*i)

#print("1.number of seconds in a month="),(30*24*60*60)
#print("2.number of seconds in a year="),(365*24*60*60)
#print("3.")
#print(49/7)
#print(8**2)
#from random import shuffle
#x = [i for i in range(18)]
#shuffle(x)

#print(x)
#a = x[0]+x[1]
#print (a)

#file= open("Quiz4")
#for line in range(7,9):
#    print(file.readlines())

with open("Quiz4") as f:
    questions = f.readlines()

print(questions[9])
