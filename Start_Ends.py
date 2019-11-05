# Word = input("Enter a word >").upper()

# if Word.endswith(Word[0]):
#     print("%s starts and ends with the same character" %(Word))
# print(Word, "starts and ends with the same character:", Word.endswith(Word[0]))

# Word = "Octa-directional-bias"

# print(Word[0:4][::-1], len(Word[0:4]), len(Word[5:16]), Word[5:16][::-1], len(Word[17:21]), Word[17:21][::-1])

# DOB = input("Enter your name and Date of Birth in this fomat: dd-mm-yyyy >")
# DOB.strip()

# BYear = int(DOB[6:10])
# print("Day --> ", DOB[0:2]) 
# print("Month -->", DOB[3:5])
# print("Year -->", DOB[6:10])

# print("You were born in a leap year:", BYear % 4 == 0)

# if BYear % 4 != 0:
#     print ("You were born in year %s" %(BYear))
#     print ("Which is not a leap year!")

# if BYear % 4 == 0:
#     print ("You were born in year %s" %(BYear))
#     print ("Which is a leap year!! WEEHEE!")
  

file_name = "CSV_Test_File.csv"
file = open(file_name, "a")
file.close()

print ("Please enter your information")

Name = input("Name ")
DOB = input("Date of birth e.g dd-mm-yyyy > ")
Gender = input("Sex > ")

file = open(file_name, "r")

if len(file.readlines()) < 1:
    file.close()
    file = open(file_name, "a")
    text1 = f"Name, DOB, MOB, YOB, Ad/Mi, Sex \n"
    file.writelines(text1)
file.close()

file = open(file_name, "a")
Day = int(DOB[0:2])
Month = int(DOB[3:5])
Year = int(DOB[6:10])

Age = 2019 - Year 

if Age > 18:
    Min_Adu = "Adult"
elif Age < 18:
    Min_Adu = "Minor"

textINT = f"{Name}, {Day}, {Month}, {Year}, {Min_Adu}, {Gender} \n"

file.writelines(textINT)

file.close()

# is_happy = 1
# if is_happy:
#     print("oops")
