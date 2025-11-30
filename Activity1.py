medical_cause=input("Did you have a medical cause Y or N")
attendence=int(input("enter the attendence of the student: "))
if medical_cause=="Y":
    print("you are allowed")
else:
    if attendence>=75:
        print("allowed")
    else:
        print("not allowed")