promoter = open('ResultChecker.txt','r')
h3k4me3Count = 0
h3k27me3Count = 0
bothCount = 0
noneCount = 0
header=promoter.readline()
while True:
    line = promoter.readline().split("\t")
    if len(line) == 0 or line == "\n":
        break
    else:
        try:
            if line[21] == "True" and line[22] == "True\n":
                bothCount += 1
            if line[21] == "True" and line[22] == "False\n":
                h3k4me3Count += 1
            if line[22] == "True\n" and line[21] == "False":
                h3k27me3Count += 1
            if line[21] == "False" and line[22] == "False\n":
                noneCount += 1
        except:
            break
promoter.close()
print("Both Count : ", bothCount)
print("H3K4me3 Count : ", h3k4me3Count)
print("H3K27me3 Count : ", h3k27me3Count)
print("NONE Count : ", noneCount)