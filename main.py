"""
Clacks main file.\n
If you have imported this file, you have undoubtedly done something wrong.
"""
from random import randint
import sys, time
import clack, back


###
def main():
    filename = sys.argv[-1] # just take the last argument

    # this is not the right way to do flags
    if filename == '--no-file' or filename == "-n":
        noFile()

    elif filename == '-h' or filename == '--help' or filename == 'main.py':
        help()
        
    elif filename == '--view-overhead':
        overhead()

    # any other flag
    else:
        suffix = filename[-4:] # the last flag
        if filename[0] == '-':
            print('Invalid flag.\nRun with -h for help.')
            return
        elif suffix != '.txt':
            print('Invalid filetype.\nRun with -h for help.')
            return

        # if it's a .txt, go here:
        with open(filename) as givenFile:
            translate = givenFile.read()
            print(type(translate))
            if translate.find('●') !=-1 or translate.find('○') !=-1: # if a clack
                decoded = open("result.txt", "w+")
                # why is there an invalid charcter that need to be removed when decoding?
                decoded.write(back.back(translate))#[:-1])
                decoded.close()
            else: # if not a clack
                encoded = open("result.txt", "w+")
                encoded.write(clack.clack(translate, False))
                encoded.close


###
def help():
    val = randint(1,5)
    overhead = ' '
    if val % 2 == 1:
        overhead = "\n  --view-clacks-overhead     View Overhead Messages"
    print('The Grand Trunk Semaphore Company Proudly Presents:')
    print('The CLI Clacks System!'.center(42))
    print('\n  -h, --help                 Display help screen' +
        '\n  -n, --no-file              Use real-time clacking' +
        '\n  -g                         Make into a GIF (NYI)' +
        overhead +
        '\n\npython3 main.py [filename or argument]' +
        '\n\nTakes a txt file of either clacks or text as input, translates, and creates' +
        "\na new file of the translation with the name of 'result.txt'.")


###
def noFile():
    selLoop = True # selection loop
    while selLoop:
        print("Type 'done' on a new line when finished typing message\n")

        translate = ''
        while True: 
            # continue adding text until user types
            # 'done' on a new line
            tmpTxt = input()
            if tmpTxt == 'done':
                break
            translate += tmpTxt


        if translate.find('●') !=-1 or translate.find('○') !=-1:
            print('\nResults:\n' + '"' +back.back(translate)+ '"')
            selLoop = False

        elif translate == '':
            selLoop = False

        else:
            print('\nResult:' +clack.clack(translate, False))
            selLoop = False


### Clacks Overhead
def overhead():
    locations = ['Genua', 'Lancre', 'Uberwald', 'Ankh-Morpork', 'Sto Lat']
    toFrom = ['to ', 'from ']
    msg = randint(0,5)
    print('OVERHEAD MESSAGE:')

    if msg == 0:
        print('GNU John Dearheart')
    elif msg == 1:
        print('GNU Terry Pratchett')
    elif msg == 2:
        ranClack = randint(24,78)
        print('Tower ' + str(ranClack) + ' is temporarily down for repairs.')
        print('Reroute clacks messages through Tower ' +str(ranClack-randint(-15,15))+ '.')
    elif msg == 3:
        ranClack = randint(1,78)
        print('Tower ' + str(ranClack) + ' has resumed service.')
    elif msg == 4:
        ranClack = randint(0,len(locations)-1)
        print('Messages ' +toFrom[ranClack%2] +locations[ranClack]+ ' are high priority until further notice.')
    elif msg == 5:
        ranClack = randint(0,len(locations))
        print('Messages ' +toFrom[ranClack%2] +locations[ranClack]+ ' are no longer high priority.')


# EOF
main()


