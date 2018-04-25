inputString = "Hello, World! My name is Ki."

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

def findBlankIndex(inputString,width):
    return findLast(inputString[:width]," ")

def wrapFirstLine(inputString, width):
    output = ""
    firstBlankIndex = inputString.find(" ")
    blankIndex = findBlankIndex(inputString, width)
    if firstBlankIndex == -1:
        output = inputString
    else:
        if blankIndex == -1:
            output+=inputString[:firstBlankIndex]
            output+="\n"
            output+=inputString[firstBlankIndex+1:]
        elif width < len(inputString):
            output+=inputString[:blankIndex]
            output+="\n"
            output+=inputString[blankIndex+1:]
        else:
            output=inputString
    return output

# for width in range(len(inputString)+1):
#     print(width)
#     print(wrapFirstLine(inputString,width))
