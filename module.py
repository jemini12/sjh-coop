class PromoterUpdater():
    def promoterupdate(self):
        # text line count
        resultLine = []
        tmp = open('K562_RNA_expression.txt','r')
        header=tmp.readline()
        result = open("ResultUpdater.txt","w+") 
        result.writelines(str(header).replace("\n","") + "\t" + "promoter_start" + "\t" + "promoter_end\n")
        while True:
            line = tmp.readline().split("\t")
            
            if len(line) == 0 or line == "\n":
                break
            else:
                # avoid index error
                try:
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
                except:
                    break
        tmp.close()
        result.close()
        return True

class PromoterChecker():
    def promotercheck(self):
        # text line count
        resultLine = []
        promoter = open('ResultUpdater.txt','r')
        h3k27me3 = open('K562_H3K27me3_ChIP-seq.bed','r')
        h3k4me3 = open('K562_H3K4me3_ChIP-seq.bed','r')
        header=promoter.readline()
        result = open("ResultChecker.txt","w+") 
        result.writelines(str(header).replace("\n","") + "\t" + "H3K4me3" + "\t" + "H3K27me3\n")
        while True:
            line = promoter.readline().split("\t")
            k27line = h3k27me3.readline().split("\t")
            k4line = h3k4me3.readline().split("\t")
            if len(line) == 0 or line == "\n":
                break
            else:
                # avoid index error
                try:
                    # line19, line20이 k4* 시리즈들과 일치하는지 확인
                    # k4line[1] < line[19] || k4line[2] > line[20] --> H3K4me3 == True
                    # k27line[1] < line[19] || k27line[2] > line[20] --> H3K27me3 == True
                    line[20] = str(line[20]).replace("\n","")
                    resultLine = line
                    
                    # k4와 영역이 겹침
                    # 1) k4 start -- promoter start -- k4 end
                    # 2) promoter start -- k4 start -- promoter end
                    if (k4line[1] <= line[19] and line[19] <= k4line[2]) \
                        or (line[19] <= k4line[1] and k4line[1] <= line[20]):
                        resultLine.append("True")
                        
                    # k4와 영역이 안겹침
                    else:
                        resultLine.append("False")
                    
                    # k27과 영역이 겹침
                    if (k27line[1] <= line[19] and line[19] <= k27line[2]) \
                        or (line[19] <= k27line[1] and k4line[1] <= line[20]):
                        resultLine.append("True\n")
                    else:
                        resultLine.append("False\n")
                    
                    result.writelines('\t'.join(resultLine))
                except:
                    break
        promoter.close()
        h3k4me3.close()
        h3k27me3.close()
        result.close()
        return True
    
class PromoterCounter():
    def promotercount(self):
        promoter = open('ResultChecker.txt','r')
        header=promoter.readline()
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

        return True
                