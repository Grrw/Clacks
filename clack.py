# all the code for taking text and returning clacks

def clack(txt):
    """
    Takes text and returns clacks
    """
    clacks = ""
    for ii in range(len(txt)):
        clacks += make8(ord(txt[ii])) # gives str of binary

    clacks = formatter(clacks)

    return clacks


def make8(int):
    """
    Takes an integer and returns its 8-bit value as a string
    """
    # gets binary of int without '0b' prefix
    # zfill fills with 0 in front until length is 8
    return str(bin(int)[2:].zfill(8))


def formatter(txt):
    """
    Takes text of 8-bit ascii and formats to clacks formatting
    """
    # append null char if chars are not even
    while (len(txt) /8) %2 != 0:
        txt += "00000000"

    txt = visualChange(txt)

    # formats into clacks formatting 
    clack = ""
    for i in range(len(txt)):
        
        # skips the first loop
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



