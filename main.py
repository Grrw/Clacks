""" TODO
[X] convert from text to clacks
[ ] convert from clacks to text
[ ] take txt and return results in txt
"""

# REMEMBER: Make this work with ascii
# clack.JSON is only there to remind

import clack, back
selLoop = True
while selLoop:
    selection = input("Press 'q' to Quit.\nEncode or Decode? (e/d)\n")

    if selection == 'e':
        user = input('Input Message:\n')
        print(clack.clack(user))
        selLoop = False

    elif selection == 'd':
        user = ''
        print("Input Message:\n(type 'done' on a new line to stop)")
        while True:
            tmpTxt = input()
            if tmpTxt == 'done':
                break
            user += tmpTxt

        print(back.back(user))
        selLoop = False

    elif selection == 'q':
        selLoop = False




