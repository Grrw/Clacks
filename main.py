# main file

import sys
import clack, back

def main():
    filename = sys.argv[-1]

    if filename == 'main.py':
        oldMain()

    else:
        suf = filename[-4:]
        if suf != '.txt':
            print('Invalid filetype.')
            return

        print('Not yet implemented')

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


main()


