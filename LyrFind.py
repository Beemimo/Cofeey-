filename = "GaLyrics.txt"

data = open(filename, "r", errors="ignore")

Lyrk = input("Word Finder \n\n Seperate by comma for multi-word search > ")

for line in data.readlines():
    if Lyrk in line:
        lower_case_line = line.lower()
        lower_case_line = lower_case_line.replace(Lyrk, ( f'"{Lyrk.upper()}"'))

        print (lower_case_line)
# if Lyrk not in line:
#     print("I cannot find this word🤷‍♀️")
FoundWord = False
