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
            or (line[19] <= k27line[1] and k27line[1] <= line[20]):
            resultLine.append("True\n")
        else:
            resultLine.append("False\n")
        
        result.writelines('\t'.join(resultLine))