"""
Multiline formatting

Author: Pit
"""

#BOX: (generates a box around a string)
#takes string to add box around, and parameters for width, justification, border, and padding
#returns formatted string
def box(toFormat, width = 0, justify = "c", boxChar = '#', isPadded = True):
    #Check each line to see if it has a greater width than the user defined width
    #If it does, update the width
    for line in toFormat.splitlines():
        if isPadded:
            if len(line) + 4 > width:
                width = len(line) + 4
        elif len(line) + 2 > width:
            width = len(line) + 2

    #Format the box
    #Add the top border (with padding if applicable)
    formattedStr = boxChar * width
    if isPadded:
        formattedStr += "\n" + boxChar + " ".center(width - 2) + boxChar

    #Format each line individually
    for line in toFormat.splitlines():
        formattedStr += "\n" + boxChar

        funcDict = {
            "c" : line.center,
            "l" : line.ljust,
            "r" : line.rjust
        }
        if isPadded:
            formattedStr += " " + funcDict[justify](width - 4) + " "
        else:
            formattedStr += funcDict[justify](width - 2)
        
        formattedStr += boxChar

    #Add bottom border (with padding if applicable)
    if isPadded:
        formattedStr += "\n" + boxChar + " ".center(width - 2) + boxChar
    formattedStr += "\n" + boxChar * width

    return formattedStr

#COLUMN - FORMATS MULTILINE INTO COLUMNS
def col(toFormat, colWidth = "auto", just = "c", colChar = "|"):
    
    #Check for widest word to set column width
    try:
        maxWidth = int(colWidth)
    except:
        maxWidth = 0
        
    if colWidth == "auto":
        
        #Check length of each word againt maxWidth
        for word in toFormat.split():
            if len(word) > maxWidth:
                maxWidth = len(word)

    #Format the columns
    formattedStr = ""
    for line in toFormat.splitlines():
        formattedStr += "\n"
        for word in line.split():
            formattedStr += colChar + word.center(maxWidth)
        formattedStr += colChar

    print(formattedStr)
