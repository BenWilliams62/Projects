# this sscript contains the necessary methods

class lock:
    # initialis lock
    def __init__(self):
        self.foo = 0
    
    # define the unlock function
    def requestUnlock(self, code, users):

        returnValue = -1
        # find the pins for all users, and check against the inputted code
        for user in users:
            if user.pin == code:
                # send welcome message
                name = user.id
                print("Welcome {}!".format(name))

                # break the loop once code found
                returnValue = 0
                break
            
        return returnValue



class codes:
    
    # initialise users
    def __init__(self, code, name):
        self.pin = code
        self.id = name
    
    def change_name(self, name):
        self.id = name


    
