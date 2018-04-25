# inputString = "Hello, World! My name is Ki."
# inputString = "a aa aaa aaaa aaaaa aaaaaa"

# Find the blank that appears just before the width.

def findLast(inputString,char):
    index = inputString.find(char)
    output = index
    while (index >= 0):
        inputString = inputString[index+1:]
        index = inputString.find(char)
        output += index+1
    return output

# testWords = ["I am a fish.", "I am a quick brown fox.", "Foxes are great."]
# for testWord in testWords:
#     print(findLast(testWord," "))

def wrapFirstLine(inputString, width):
    outputString = ""
    firstBlankIndex = inputString.find(" ")
    blankIndex = findLast(inputString[:width]," ") 
    if firstBlankIndex == -1:
        outputString += inputString
        outputIndex = firstBlankIndex
    else:
        if blankIndex == -1:
            outputString+=inputString[:firstBlankIndex]
            outputString+="\n"
            # outputString+=inputString[firstBlankIndex+1:]
            outputIndex = firstBlankIndex
        elif width < len(inputString):
            outputString+=inputString[:blankIndex]
            outputString+="\n"
            # outputString+=inputString[blankIndex+1:]
            outputIndex = blankIndex
        else:
            outputString=inputString
            outputIndex = len(inputString)
    return outputString, outputIndex

# for width in range(len(inputString)+1):
#     print(width)
#     print(wrapFirstLine(inputString,width))

def wrapText(inputString, width):
    output = ""
    blankIndex = inputString.find(" ")
    while blankIndex > -1:
        temp = wrapFirstLine(inputString,width)
        output += temp[0]
        blankIndex = temp[1]
        inputString = inputString[blankIndex+1:]
    return repr(output)
