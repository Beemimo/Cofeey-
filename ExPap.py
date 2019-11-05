# x = [1, 2, 3]
# y = [1,2]
# x.append(y)
# # print(x)

x = [10, 12, 15, 0, 10, 5]
mean = sum(x)/len(x)
mean = round(mean, 2)
# sum_heights = sum(heights)
# mean_heights = sum_heights/len(heights)
# #Assignment
# variance = [num - mean_heights for num in heights]

# print (variance)
# deviation = [num ** 2 for num in variance]
# print(deviation)

# BeetRoot = 0
# variance = []
# while BeetRoot < len(x):
#     value = (x[BeetRoot] - mean) ** 2
#     variance.append(value)
#     BeetRoot += 1
# print(variance)

# PapAz = [num ** 2 for num in variance]
# print(PapAz)
# Anz = []

# for num in x:
#     val = (num - mean) ** 2
#     Anz.append(val)
# print(Anz)

file_name = "XBunch.csv"
file = open(file_name, "a")
file.close()

file = open(file_name, "r")

if len(file.readlines()) < 1:
    file.close()
    file = open(file_name, "a")
    text1 = f"X, X-X, (X-X)2  \n"
    file.writelines(text1)
file.close()

file = open(file_name, "a")

BeetRoot = 0
variance = []
while BeetRoot < len(x):
    value = x[BeetRoot] - mean
    variance.append(value)
    BeetRoot += 1
print(variance)


Anz = []
for num in x:
    val = (num - mean) ** 2
    val = round(val, 2)
    Anz.append(val)
print(Anz)
lab = 0


while lab < len(x):
    textINT = f"{x[lab]}, {variance[lab]}, {Anz[lab]} \n"
    lab += 1
    file.writelines(textINT)


# x = int(x+x[lab])
# print(x)


