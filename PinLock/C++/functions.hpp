// header files
#include <string>


class codes {

    // attributes
    int pin;
    std::string id;

    // public functions
    public:
    void add_pin(int code);
    void add_name(std::string name);
    int get_pin();
    std::string get_name();

};

class lock {

    // attributes

    //public functions
    public:

        // authenticate
        int request_unlock(int code, std::vector<codes> users);


    // private functions
    private:

};