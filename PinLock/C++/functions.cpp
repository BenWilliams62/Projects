#include <iostream>
#include <vector>

#include "functions.hpp"

// define functions for the classes such as:
/*
type class_name::function_name(type input){
    normal function body
};
*/

// classes

// add pin to codes object
void codes::add_pin(int code){
    pin = code;
};

// add name to codes object
void codes::add_name(std::string name){
    id = name;
};

// get pin and get name from codes object
int codes::get_pin(){
    return pin;
};

std::string codes::get_name(){
    return id;
};

// authenticate code
int lock::request_unlock(int code, std::vector<codes> users){
    
    // by default the lock should be locked
    int returnValue = -1;

    // loop through codes objects to find code
    for (int i = 0; i <= users.size(); i++){
        if (users[i].get_pin() == code){

            // if user in system, send welcome message
            std::string name = users[i].get_name();
            std::cout << "Welcome " << name << std::endl;

            // break the loop and return a success value
            returnValue = 0;
            break;
        };
    };



    return returnValue;
};