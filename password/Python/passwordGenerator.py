# password generator

import random

# set characters
upperCase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
lowerCase = 'qwertyuiopasdfghjklzxcvbnm'
numbers = '0123456789'
symbols = '-_!'

characters = upperCase + lowerCase + numbers + symbols

# ask for an input, if within valid range. then continue
def length_qs():
    # password length
    loopCounter = 0
    while True:
        lengthInput = str(input('how many characters does your password need?\n(between 8 and 150)\n'))
        loopCounter += 1
        try:
            length = int(lengthInput)
            # if a valid input is entered, continue to the next stage
            if 7 < length < 150:
                break
        except:
            # if too many incorrect values were entereed, then continue to close the program
            if loopCounter > 4:
                length = 0
                break
    # if length is valid, then run the random generator, otherwise close the program
    if length != 0:
        password_qs(length)
    else:
        print('incorrect value')

# generate a random string of characters of given length
def password_qs(length):
    password = ''
    # add a random character for each iteration in the given length
    for _ in range(length):
        password += random.choice(characters)
    print('\nYour new password is:\n'+password+'\n')

    # run the function to query whether you are finished
    newPassword_qs()



# query whether a further password is wanted
def newPassword_qs():
    reply = str(input('\n\nDo you want to generate another password?\n(y/n)\n'))
    # if input is yes, then run the length query, otherwise, end the program
    if reply == 'y' or reply == 'Y':
        length_qs()
    else:
        print('\nThank you for using this password generator!\n')


length_qs()


