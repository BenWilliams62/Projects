#include <string>
#include <iostream>
#include <random>
#include "functions.hpp"

using namespace std;

// length query
void length_qs(){
    
    int loopCounter = 0;
    int lengthInput;
    // ask for an input, and hceck it is valid
    while (true) {
        std::cout << "how many characters does your password require?\n";   // ask for input
        std::cin >> lengthInput;
        loopCounter++;  // add one to the loop counter
        // if the input is an integer, check that it is between 8 and 150. This is to avoid passwords too long or insecure for use
        if (8 <= lengthInput) {
            if (lengthInput <=150){
                break;
            } else {
                std::cout << "Invalid input\n";
            }
            
        } else {
            std::cout << "Invalid input\n"; // if input is an invalid integer, try again
        }
        if (loopCounter > 4) {
            // if the input is an invalid type (e.g. string), or invalid integer inputed
            // more than five times, then set length to 0 to allow for ending the program
            std::cout << "incorrect value\n"; 
            lengthInput = 0;
            break;
        }
    }
    // if input is valid, call the random generator
    if (lengthInput > 0) {
        password_qs(lengthInput);        
    } else {
        // if not valid, then print a message, and close the program
        std::cout << "Values entered were not integers between 8 & 150!\n";
    };
    
};

// password query
void password_qs(int length){
    // define variables and available characters
    std::string password;
    std::string characters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789-_!";
    
    std::random_device random_device;
    std::mt19937 generator(random_device());
    std::uniform_int_distribution<> distribution(0, characters.size() - 1);
    // create a random string of values of the desired length
    for (int i = 0; i <= length; i++) {
        password += characters[distribution(generator)];
    }

    std::cout << "\nYour new password is:\n" << password << "\n\n";
    // call the function to request a whether another password is wanted
    newPassword_qs();
    
};

// ask for new password, if yes, run the length query, if not then send a message and end the program
void newPassword_qs() {
    std::string reply;

    std::cout << "Do you want to generate another password? (y/n)\n";
    std::cin >> reply;

    if (reply == "y" || reply == "Y") {
        length_qs();
    } else {
        std::cout << "\nThank you for using this password generator!\n";
    }
}
