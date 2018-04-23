inputString = "Hello, World! My name is Ki."

# Find the blank that appears just before the width.

def findBlankIndex(inputString,width):
    index = inputString.find(" ")
    if (index < width):
        while (inputString.find(" ") > 0):
            if (index >= width):
                inputString = inputString[index+1:]
            index += inputString.find(" ")+1
    return index

for width in range(len(inputString)):
    blankIndex = findBlankIndex(inputString, width)
    print(blankIndex)
    print(inputString[blankIndex])
    print(inputString[:blankIndex]+"\n"+inputString[blankIndex+1:])
