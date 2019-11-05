import time
import winsound
name = "Bimbo", "Bolu", "Tooh", "Bleh", "Terance", "Khan", "Choku", "Teni", "Ikokobiko", "Chika"



for i in range(len(name)):
    winsound.Beep(500, 500)
    print(f"|\t{i+1}. {name[i]} |\t", end="\r")
    time.sleep(1)

# for Bimi in reversed(range(21)):
#     print(f"|\t {Bimi} |\t", end="\r")
#     time.sleep(1)