// fizzbang in c++
# include <iostream>
# include <string>

int main() {
    
    std::cout << "Welcome to a game of fizzbang! \n\n";

    int fizz;
    int bang;

    std::cout << "Please pick an integer for fizz\n(between 2 and 999\n";
    std::cin >> fizz;

    std::cout << "\nPlease pick an integer for bang\n(between 2 and 999\n";
    std::cin >> bang;

    std::cout << "\n\nFizzbang:\n\n";

    for (int i=1; i<=1000; i++) {
        std::string output = "";
        if (i%fizz == 0) {
            output += "Fizz";
        }
        if (i%bang == 0) {
            output += "Bang";
        }
        if (i%fizz != 0 && i%bang != 0) {
            output = std::to_string(i);
        }
        std::cout << output << "\n";
    }
    
    std::cout << "Thank you for testing!\n";

    return 0;
}