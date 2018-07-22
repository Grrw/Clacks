"""
Clacks main file.\n
If you have imported this file, you have undoubtedly done something wrong.
"""

import sys, random, time
import clack, back


###
def main():
    filename = sys.argv[-1] # just take the last argument

    # this is not the right way to do flags
    if filename == '--no-file-mode':
        oldMain()

    elif filename == '-h' or filename == '--help' or filename == 'main.py':
        help()
        
    elif filename == '--view-overhead':
        overhead()

    else:
        suf = filename[-4:]
        if filename[0] == '-':
            print('Invalid flag.')
            time.sleep(1)
            help()
            return
        elif suf != '.txt':
            print('Invalid filetype.')
            return

        print('Not yet implemented.')



###
def help():
    print('The Grand Trunk Semaphore Company Proudly Presents:')
    print('The Clacks System!'.center(45))
    print('\n  -h, --help                 Display this screen' +
        '\n  --no-file-mode             Use real-time clacking' +
        '\n\npython3 main.py [filename or argument]' +
        '\n\nTakes a file* of either clacks or text as input, translates, and creates' +
        "\na new file of the translation with the name of 'result.txt'." +
        '\n\n*Only compatible with .txt files')


###
def oldMain():
    selLoop = True
    while selLoop:
        selection = input("Type 'q' to Quit.\nEncode or Decode? (e/d)\n")

        if selection == 'e':
            user = input('Input Message:\n')
            print('\nResult:' +clack.clack(user))
            selLoop = False

        elif selection == 'd':
            user = ''
            print("Input Message:\n(type 'done' on a new line to stop)")
            
            while True:
                tmpTxt = input()
                if tmpTxt == 'done':
                    break
                user += tmpTxt

            print('\nResult:\n' + '"' +back.back(user)+ '"')
            selLoop = False

        elif selection == 'q':
            selLoop = False


### Clacks Overhead
def overhead():
    locations = ['Genua', 'Lancre', 'Uberwald', 'Ankh-Morpork', 'Sto Lat']
    toFrom = ['to ', 'from ']
    msg = random.randint(0,5)
    print('OVERHEAD MESSAGE:')

    if msg == 0:
        print('GNU John Dearheart')
    elif msg == 1:
        print('GNU Terry Pratchett')
    elif msg == 2:
        ranClack = random.randint(24,78)
        print('Tower ' + str(ranClack) + ' is temporarily down for repairs.')
        print('Reroute clacks messages through Tower ' +str(ranClack-random.randint(-15,15))+ '.')
    elif msg == 3:
        ranClack = random.randint(1,78)
        print('Tower ' + str(ranClack) + ' has resumed service.')
    elif msg == 4:
        ranClack = random.randint(0,len(locations)-1)
        print('Messages ' +toFrom[ranClack%2] +locations[ranClack]+ ' are high priority until further notice.')
    elif msg == 5:
        ranClack = random.randint(0,len(locations))
        print('Messages ' +toFrom[ranClack%2] +locations[ranClack]+ ' are no longer high priority.')


# EOF
main()


