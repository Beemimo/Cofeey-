
Accounts = {}
Nam_pls = ""

print ("Hello, this is your personal notepad")
Prev_Acc = input("Do you already have an account? ").capitalize()

if Prev_Acc == "Yes":
    Nam_pls = input("Please enter your username > ").capitalize() 
            # if Note_Choice in Accounts[f"{Name}"]:


elif Prev_Acc == "No": 
    New_Acc = input("Please enter your username to create an account > ").capitalize()

    Accounts[New_Acc] = []
    print("WOOHOO! You have successfully created an account 🙆🏾‍♀️")
    Nam_pls = input("Please enter your username > ").capitalize() 
    # Accounts = {f"{Nam_pls}" : []}

if Nam_pls in Accounts:
    print("User Recognised")
    Quest1 = input("Would you like to open or create a file? (Open/New)").capitalize()
    if Quest1 == "Open":
        print(Accounts[f"{Nam_pls}"])
        Note_Choice = input("Choose your note > ").capitalize()

Quest1 = input("Would you like to open or create a file? (Open/New)").capitalize()
if Quest1 == "Open":
    print(Accounts[f"{Nam_pls}"])
    Note_Choice = input("Choose your note > ").capitalize()
    # if Note_Choice in Accounts[f"{Name}"]:
    # 

file_name = f"{Nam_pls} NotePaD.txt"
file = open(file_name, "a")
file.close()

for item in Nam_pls:
    Accounts[f"{Nam_pls}"].append(Nam_pls)


print(Nam_pls)

file = open(file_name, "a")

Notes = input("Write your notes here > ")

file.writelines(Notes)

file.close()
