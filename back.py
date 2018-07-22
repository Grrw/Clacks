# all the code for taking clacks and returning text

def back(clack):
    """
    Takes clacks and returns text
    """
    clack = deformatter(clack)

    ordList = makeBase10(clack)

    # charList
    charList = ''
    for ii in range(len(ordList)):
        charList += chr(int(ordList[ii], 2))

    return charList


def makeBase10(givenStr):
    """
    Takes a string of 1s and 0s seperated by commas.
    Returns it as a list of strings using ord(), splitting at the commas
    """
    strAsList = givenStr.split(',')

    return strAsList


def deformatter(clack):
    """
    Takes clacks, removes whitespaces and adds commas every 8 characters
    """
    clack = visualChange(clack)

    # adds commas every 8 chars
    tmpClack = ''
    for ii in range(len(clack)):
        if ii %8 == 0:
            tmpClack += ','
        tmpClack += clack[ii]
    clack = tmpClack[1:] # remove leading comma

    return clack


def visualChange(txt):
    """
    Takes text of clacks, changes ● to 0 and ○ to 1 and removes whitespace
    """
    asNums = ''
    for ii in range(len(txt)):
        if txt[ii] == '●':
            asNums += "0"
        elif txt[ii] == '○':
            asNums += "1"

    return asNums



