def f_print_largest(int1,int2):
    if int1<int2:
        print (int2),("is the largest")
    elif int2<int1:
        print (int1),("is the largest")
vNumber = (f_print_largest(10,15))

def insult():
    print("You know, you are a classic example of the inverse ratio between the size of the mouth and the size of the brain.-The Doctor, Doctor Who \n" * 3)

print(insult())

def number_to_change():
    num=int(input("pick one number"))
    print(num*2+1)

print (number_to_change())
