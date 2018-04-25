import sys
from autolinebreak import *

with open('input.md') as f:
    content = f.readlines()
content = [x.strip() for x in content] 

if len(sys.argv)>1:
    width = int(sys.argv[1])
else:
    width = 10

digraphStr = ""
digraphStr += "digraph map "
digraphStr += "{"
digraphStr += "\n"
index = 1
for inputString in content:
    digraphStr += "\t"
    if inputString.find(":")!=-1:
        digraphStr += "A"+str(index)+" "
    else:
        skillCode = inputString[inputString.find(" ")+1:inputString.find(":")]
        digraphStr += skillCode 
    digraphStr += "[label = "
    digraphStr += wrapText(inputString,width)
    digraphStr += "];\n"
    index+=1
digraphStr += "}"

print(digraphStr)
