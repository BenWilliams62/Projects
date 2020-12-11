'''
A simple game of fizz-bang, where the user can enter
for which multiples they want 'fizz' and for which 
they want 'bang'. This will play the game for the 
numbers 1 - 1000.
'''

# verify input function
def verify():
    loopCounter = 0
    while True:
        integer = input('pick an integer between 2 and 999\n')
        loopCounter += 1
        try:
            integer = int(integer)
            # if a valid input is entered, continue to the next stage
            if 7 < integer < 150:
                break
        except:
            # if too many incorrect values were entereed, then continue to close the program
            if loopCounter > 4:
                integer = int(0)
                break
    # if length is valid, then run the random generator, otherwise close the program
    if 2 <= integer <= 999:
        return integer
    else:
        print('incorrect value')



# ask for and verify inputs
print('\nPlease pick your integer for Fizz\n')
fizz = verify()

print('\nPlease pick your integer for Bang\n')
bang = verify()



# loop: check if a multiple and print accordingly
print("\nFizz-Bang:\n\n")
for i in range(1,1001):
    output = ''
    if i % fizz == 0:
        output += 'Fizz'

    if i % bang == 0:
        output += 'Bang'
    
    if i % fizz != 0 and i % bang != 0:
        output = i
    
    print(output)
