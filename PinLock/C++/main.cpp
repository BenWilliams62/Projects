#include <iostream>
#include <vector>

#include "functions.hpp"

/*
// create object
    className objectName;

    objectName.function();
*/


int main() {

    // hardcoded admin codes
    codes admin;
    admin.add_name("admin");
    admin.add_pin(12341234);

    codes guest;
    guest.add_name("guest");
    guest.add_pin(00000000);

    // create list of all users
    std::vector<codes> users;

    users.push_back(admin);
    users.push_back(guest);

    // create codes for editing a user
    int delete_user_code = 335383;
    int add_user_code = 23308737;

    // initialise door lock
    lock door;

    // while loop to ask for codes
    while (true)
    {

        std::cout << "\n";

        // ask for input
        int code;
        std::cout << "Please enter your code to unlock this door\n";
        std::cin >> code;

        // validate pin

        // autehenticate user, add new user, or remove user
        if (code == add_user_code)
        {
            std::string new_name;
            int new_code;
            
            // ask for name and code
            std::cout << "Please enter your name\n";
            std::cin >> new_name;

            std::cout << "Thank you, "<< new_name << ", Please enter your pin\n";
            std::cin >> new_code;

            // add new user object
            codes user;
            user.add_name(new_name);
            user.add_pin(new_code);

            // add to vector
            users.push_back(user);
        
        
        }
        else if (code == delete_user_code)
        {
            int deletion_code;

            // ask for the pin of the user tp be deleted
            std::cout << "Please enter the code you wish to delete\n";
            std::cin >> deletion_code;
            std::cout << "\n";

            // loop to find this pin
            for (int i = 0; i <= users.size(); i++){
                if (users[i].get_pin() == deletion_code){

                    // if user in system, send goodbye message
                    std::string name = users[i].get_name();
                    std::cout << "Gooddbye " << name << std::endl;

                    // delete from list
                    users.erase (users.begin()+i);

                    // break the loop and return a success value
                    break;
                };
            };
            
        }
        else
        {
            // request unlock
            int exitCode = door.request_unlock(code, users);

            // if unlock successful, open door, else dont
            if (exitCode == 0)
            {
                /*
                add code to suit particular lock and API
                once added, you can delete the line that prints the success message
                */
               std::cout << "success\n";

            }
            else
            {
                std::cout << "Incorrect pin, try again\n";
            };
            



        };
        
        

    };
    return 0;
};