print("select ur ride: ")
print("1. bike")
print("2. car")
choice=int(input("enter ur choice"))
if choice==1:
    print("what type of bike? ")
    print("1. scooty\n")
    print("2. scooter\n")
    choice2=int(input("enter the choice 2"))
    if choice2==1:
        print("u have selected scooty")
    else:
        print("u have selected scooter")
elif choice==2:
    print("what type of car? ")
    print("1. tesla\n")
    print("2. lemborgini\n")
    choice3=int(input("enter ur choice 3"))
    if choice3==1:
        print("u have selected tesla")
    else:
        print("u have selected lemorgini")
else:
    print("wrong choice")