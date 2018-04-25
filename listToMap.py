import sys
import re
from autolinebreak import *

with open('input.md') as f:
    content = f.readlines()
content = list(filter(None,[x.strip() for x in content])) 

if len(sys.argv)>1:
    width = int(sys.argv[1])
else:
    width = 20

digraphStr = ""
digraphStr += "digraph map "
digraphStr += "{"
digraphStr += "\n"
index = 1
for inputString in content:
    digraphStr += "\t"
    if inputString.find(":")==-1:
        digraphStr += "A"+str(index)+" "
    else:
        prefix = inputString[:inputString.find(":")]
        if prefix.find(" ")!=-1:
            prefix = prefix[prefix.find(" ")+1:] 
        prefix = re.sub(r'\W+','',prefix) 
        digraphStr += prefix + " "
    digraphStr += "[label = "
    digraphStr += wrapText(inputString[inputString.find(" ")+1:],width)
    digraphStr += "];\n"
    index+=1
digraphStr += "}"

print(digraphStr)
