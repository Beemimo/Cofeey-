import time
import random
filename = "Lyrics.txt"

data = open(filename, "r", errors="ignore")

LenOData = len(data.readline())


for i in range(LenOData):
    # print(f"|\t{i+1}. {filename[i]} |\t", end="\r")
    
    delay = random.randint(1,5)
    print(delay)
    print(i, data.readline())
    time.sleep(delay)

print(data.close())
