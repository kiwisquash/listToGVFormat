import sys
from autolinebreak import *

with open('input.md') as f:
    content = f.readlines()
content = [x.strip() for x in content] 

if len(sys.argv)>1:
    width = int(sys.argv[1])
else:
    width = 10

for inputString in content:
    print(wrapText(inputString,width))
 
