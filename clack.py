"""
Code that handles anything related to transcription of clacks
"""
def clack(txt, arSwitch):
    """
    Takes text and a boolean.\n
    If the boolean is False then it returns clacks as text\n
    If the boolean is True then it returns clacks as an array
    """
    clacks = ""
    for ii in range(len(txt)):
        clacks += makeBase2(ord(txt[ii])) # gives str of binary

    if (arSwitch):
        pass
    else:
        clacks = formatter(clacks)

    return clacks


def makeBase2(givenInt):
    """
    Takes an integer and returns its 8-bit value as a string
    """
    # gets binary of int without '0b' prefix
    # zfill fills with 0 in front until length is 8
    return str(bin(givenInt)[2:].zfill(8))


def formatter(txt):
    """
    Takes text of 8-bit ascii and formats to clacks formatting
    """
    # append a space if chars are not even
    # space is removed upon translation back
    while (len(txt) /8) %2 != 0:
        txt += "00100000"

    txt = visualChange(txt)

    # formats into clacks formatting 
    clack = ""
    for i in range(len(txt)):
        
        # adds spaces between each dot
        if i != 0:
            clack += " "

        # split to rows of 4 
        if i %4 == 0:
            clack += "\n"

        # split into 4x4
        if (i /8) %2 == 0:
            clack += "\n"

        clack += txt[i]
        
    return clack


def visualChange(txt):
    """
    Takes text of 8-bit ascii and changes 0 to ● and 1 to ○ 
    """
    asDots = ""
    for ii in range(len(txt)):
        if txt[ii] == '0':
            asDots += "●"
        else:
            asDots += "○"

    return asDots



