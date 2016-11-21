vScore = 75

if vScore >= 50:
    print("\nPass")
else:
    print("\nFail")

vMonth = "September"
vLetter = "e"

if vLetter in vMonth:
    print("There is a letter"),(vLetter),("in"),(vMonth)
else:
    print("There is not a letter"),(vLetter),("in"),(vMonth)


vChoice = input("Enter Number 1 to 3")

if vChoice == 1:
    print("Chosen Item 1")

elif vChoice == 2:
    print("Chosen Item 2")

elif vChoice== 3:
    print("Chosen Item 3")
# this is for if the retarded consumer put a different answer
else:
    print("Sorry, your answer is invalid, please go check your IQ")

#program that works out the score for a given word
#a = 5
#e = 4
#i = 3
#o = 2
#u = 1

word = str(raw_input("What is your word?"))
print ("Your word will be scored by the following...a=5, e=4, i=3, o=2, u=1...any other letter will be scored as zero")
word=word.lower()


score=0


for letter in word:
   if letter == "a":
       score=score+5
   elif letter == "e":
       score=score+4
   elif letter =="i":
       score=score+3
   elif letter =="o":
       score=score+2
   elif letter == "u":
       score=score+1
   else:
       score=score
print ("Your word score is", score)


