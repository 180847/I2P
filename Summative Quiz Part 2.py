name=""
Score=0
checker=True
highscore=Score
highname=name
while checker==True:
    name=input("\n""What is your name?")
    print("Welcome",name,"Looks like you are taking this IQ test, have fun!(Calculators are not allowed)")
    Score=0

    print("President Obama is the #_____ president? A :1st B: 26th C:44 D: 47")
    Answer1=input("Input Letter")
    Answer1=Answer1.upper()
    if Answer1=="C":
        print("You are correct!")
        Score=Score+1
        print("score=",Score)
    else:
        print("You are wrong.Score=",Score)

    print("53 x 7""\n""A:226,B:137,C:373,D:371")#add a line here
    Answer2=input("Input Letter")
    Answer2=Answer2.upper()
    if Answer2=="D":
        print("You are correct!")
        Score=Score+1
        print("score=",Score)
    else:
        print("You are wrong.Score=",Score)

    print("When was WW2""\n""A:1900-1911,B:1939-1945,C:1944-1950,D:2012-2014")
    Answer3=input("Input Letter")
    Answer3=Answer3.upper()
    if Answer3=="B":
        print("You are correct!")
        Score=Score+1
        print("score=",Score)
    else:
        print("You are wrong.Score=",Score)

    print("Where is the capital of Zimbabwe""\n""A:Berlin,B:Abuja,C:Harare,D:Norton")
    Answer4=input("Input Letter")
    Answer4=Answer4.upper()
    if Answer4=="C":
        print("You are correct!")
        Score=Score+1
        print("score=",Score)
    else:
        print("You are wrong.Score=",Score)

    print("What is the Jersey Number of Michael Jordan""\n""A:6,B:23,C:24,D:34")
    Answer5=input("Input Letter")
    Answer5=Answer5.upper()
    if Answer5=="B":
        print("You are correct!")
        Score=Score+1
        print("score=",Score)
    else:
        print("You are wrong.Score=",Score)

    print("When did Hong Kong get returned to China""\n""A:1997,B:1920,C:1954,D:2012")
    Answer6=input("Input Letter")
    Answer6=Answer6.upper()
    if Answer6=="A":
        print("You are correct!")
        Score=Score+1
        print("score=",Score)
    else:
        print("You are wrong.Score=",Score)

    print("How much dirt is there in a hole 3 feet deep, 6 ft long and 4 ft wide?""\n""A:72,B:128,C:78.5,D:0")
    Answer7=input("Input Letter")
    Answer7=Answer7.upper()
    if Answer7=="D":
        print("You are correct!")
        Score=Score+1
        print("score=",Score)
    else:
        print("You are wrong(How is it a hole if there is dirt in it?.Score=",Score)

    print("How old is Donald Trump. A:55,B:70,C:63,D:82")
    Answer8=input("Input Letter")
    Answer8=Answer8.upper()
    if Answer8=="B":
        print("You are correct!")
        Score=Score+1
        print("score=",Score)
    else:
        print("You are wrong.Score=",Score)

    print("You are in a dark room with a candle, a wood stove, and a gas lamp. If you only have 1 match, what do you light first?""\n""A:Candle,B:Woodstove,C:Gas Lamp,D:None of the above")
    Answer9=input("Input Letter")
    Answer9=Answer9.upper()
    if Answer9=="D":
        print("You are correct!")
        Score=Score+1
        print("score=",Score)
    else:
        print("You are wrong.You need to light the match first.Score=",Score)

    print("A plane crashes on the United States/Canada border. Where are the survivors buried?""\n""A:The family gets to decide where to bury,B:United States,C:Canada,D:None of the above")
    Answer10=input("Input Letter")
    Answer10=Answer10.upper()
    if Answer10=="D":
        print("You are correct!")
        Score=Score+1
        print("score=",Score)
    else:
        print("You are wrong.We don't bury survivors.Score=",Score)

    print("Who is the creator of Star Wars""\n""A:Walt Disney B:Rick Riordian,C:George Lucas D:JK. Rolling")
    Answer11=input("Input Letter")
    Answer11=Answer11.upper()
    if Answer11=="C":
        print("You are correct!")
        Score=Score+1
        print("score=",Score)
    else:
        print("You are wrong.Score=",Score)

    print("x^2=49, what is x^3""\n""A:343 B:97,C:G473 D:689")
    Answer12=input("Input Letter")
    Answer12=Answer12.upper()
    if Answer12=="A":
        print("You are correct!")
        Score=Score+1
        print("score=",Score)
    else:
        print("You are wrong.Score=",Score)

    print("Who won the 2016 NBA Champions""\n""A:Spurs B:Lakers,C:Warriors D:Cavaliers")
    Answer13=input("Input Letter")
    Answer13=Answer13.upper()
    if Answer13=="D":
        print("You are correct!")
        Score=Score+1
        print("score=",Score)
    else:
        print("You are wrong.Score=",Score)

    print("Sn is the chemical symbol for which element?""\n""A:Sodium B:Sulphur,C:Strontium D:Tin")
    Answer14=input("Input Letter")
    Answer14=Answer14.upper()
    if Answer14=="D":
        print("You are correct!")
        Score=Score+1
        print("score=",Score)
    else:
        print("You are wrong.Score=",Score)

    print("At room temperature, what is the only metal that is in liquid form??""\n""A:Water B:Mercury,C:Lead D:Magnesium")
    Answer15=input("Input Letter")
    Answer15=Answer15.upper()
    if Answer15=="B":
        print("You are correct!")
        Score=Score+1
        print("score=",Score)
    else:
        print("You are wrong.Score=",Score)
    print("Congratulations",name,"your score is",Score)
    print("Is there another person who is going to take the test?")
    retake=input("Type 'Y' for yes, 'N' for No")
    retake=retake.upper()
    if retake=="N":
        checker=False
    if Score>highscore:
        highscore=Score
        highname=name
        print("Congratulations, you beat the new highscore""\n""Highscore:",highscore,"Name:",highname)
    else:
        print("Highscore:",highscore,"Name:",highname)
