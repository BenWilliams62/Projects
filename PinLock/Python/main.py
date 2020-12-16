from lock_system import codes, lock


def main():

    # hard code for admin users
    admin = codes(12341234, "Alice")
    p1 = codes(00000000, "Bob")

    # editing codes: enter these to change a user's info
    delete_user_code = 335383
    add_user_code = 23308737


    # add users to list
    users = [
        admin,
        p1,
    ]

    # initialise lock
    door = lock()

    while True:


        print("\n")
        code = input("Please enter your code to unlock\n")

        # validate pin type
        try:
            code = int(code)
        except ValueError:
            print("That's not a valid code format")
            continue
        

        # add admin code to add more users
        if code == add_user_code:

            # ask for name and code
            name = str(input("Enter the name for the new user\n"))
            new_code = input("Thank you! Please enter their passcode\n")

            # validate the new code
            try:
                new_code = int(new_code)
            except ValueError:
                print("Invalid code format")
                continue
            
            # set parameter for code length
            if len(str(new_code)) != 8:
                print("Invalid password length")
                continue

            # add name and code to databse
            user = codes(new_code, name)
            users.append(user)

        
        
        # code to delete user
        elif code == delete_user_code:

            # ask for pin
            deletion_code = input("Please enter your code to delete\n")

            # validate pin type
            try:
                deletion_code = int(deletion_code)
            except ValueError:
                print("That's not a valid code format")
                continue

            # find this number
            for user in users:
                if user.pin == deletion_code:
                    # send goodbye message
                    username = user.id
                    print("GoodBye {}!".format(username))
                    # find which element they are
                    it = users.index(user)

                    # delete them from system
                    del users[it]
                    break
        
       

        # if no adjustment is necessary, then proceed to attempt unlock
        else:
            # request the unlock
            unlockCode = door.requestUnlock(code, users)

            # if unlock is valid, unlock door, else keep it locked
            if unlockCode == 0:
                """
                add Code to suit your lock's method for unlocking
                """
                print("success")    # remove this line after API is tested
            else:
                """
                assuming your locks default is closed,
                no code needs to be put here
                """
                print("incorrect pin, try again")
    
        print("\n")

if __name__ == "__main__":
    main()

