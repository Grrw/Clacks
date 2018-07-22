# all the code for taking clacks and returning text

def back(clack):
    """
    Takes clacks and returns text
    """
    txt = ''
    pass


def makeBase10(givenInt):
    """
    Takes an 8-bit value as a string and returns it as an integer
    """
    pass


def deformatter(clack):
    """
    Takes clacks, removes whitespaces and replaces newlines with commas 
    """
    result = ''
    for ii in range(len(clack)):

        if clack[ii] == '\n':
            result += ','

        if clack[ii] != ' ':
            result += clack[ii]
    
    return result


def visualChange(txt):
    pass



