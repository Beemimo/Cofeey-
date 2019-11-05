file_name = "Python_HomeWek.csv"
file = open(file_name, "a")
file.close()

file = open(file_name, "r")

if len(file.readlines()) < 1:
    file.close()
    file = open(file_name, "a")
    text1 = f"1st Name, LastName, DOB, Sex, Feeling Well, HeadAche,  \n"
    file.writelines(text1)
file.close()

Name1st = input("Please enter your name > ")
Name2nd = input("Surname > ")
Sez = input("Sex > ")
DOB = input("Your date of birth in this format dd/mm/yyyy > ")
print("Hello %s" %(Name1st))
print("This is a diagnostics Test")
print("Please enter your answers in Yes/No or any other format assigned to the question")

q1 = input("Are you feeling alright today?(Yes/No/Not really) ").lower()
if q1 == "yes":
    print("That's great! Have a nice day. :)")
if q1 == ("no" or "not really"):
    print(q1 == "no" or "not really")
    q2 = input("Do you have a HeadAche?(Yes/No)").lower()
    if q2 == "yes":
        q3H = input("Have you been sleeping well lately %s hmmm?🤓(Yes/No) " %(Name1st)).lower()
        if q3H == "yes":
            q4H = input("Hast thou thought of ingesting some painkillers(Yes/No/Not really)? ").lower()
            if q4H == "yes":
                print("It would be best if you consult a doctor")
            elif q4H == "no":
                print("You should try Panadol or Paracetamol")
            else:
                print("I do not understand that reply 🤷‍")
                print(q4H)
        elif q3H == ("no" or "not really")
            print("%s you currently need sleep" %(Name1st))
        else:
            print("I do not understand that reply 🤷‍")
            print(q3H)
    elif q2 == "no":
        q3T = input("Are you experiencing any stomach pain?")
        if q3T == "yes":
            q4T = input("It would be best if you consult a doctor")
        elif q3T == "no":
            print("I cannot diagnos this problem please consult a doctor")
        else:
            print("I do not understand that reply 🤷‍")
            print(q3T)
    else:
        print("I do not understand that reply 🤷‍")
        print(q2)
else:
    print("I do not understand that reply 🤷‍")
    print(q1)

