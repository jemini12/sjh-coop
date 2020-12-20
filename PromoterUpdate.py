# text line count
resultLine = []
tmp = open('K562_RNA_expression.txt','r')
header=tmp.readline()
result = open("ResultUpdater.txt","w+") 
result.writelines(str(header).replace("\n","") + "\t" + "promoter_start" + "\t" + "promoter_end\n")
while True:
    line = tmp.readline().split("\t")
    
    if len(line) == 0:
        break
    else:
        line[18] = str(line[18]).replace("\n","")
        resultLine = line
        
        if line[5] == "+":
            promoter_start = int(line[3]) - 2000
            promoter_end = int(line[3]) + 1000
            resultLine.append(str(promoter_start))
            resultLine.append(str(promoter_end) + "\n")
        elif line[5] == "-":
            promoter_start = int(line[4]) - 1000
            promoter_end = int(line[4]) + 2000 
            resultLine.append(str(promoter_start))
            resultLine.append(str(promoter_end) + "\n")
        
        result.writelines('\t'.join(resultLine))