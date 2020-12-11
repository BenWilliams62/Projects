// C++ maze solver

# include <iostream>


int main() {
    std::cout << "Maze solver \n\n";
    // define maze or import maze

    double maze [10][10] = {
        {0,1,0,0,0,0,0,0,0,0},
        {0,1,0,0,1,0,1,1,1,0},
        {0,1,0,1,1,1,1,0,0,0},
        {0,1,1,0,0,0,1,0,0,0},
        {0,0,1,0,0,0,1,1,1,0},
        {0,0,1,0,0,0,1,0,0,0},
        {0,1,1,1,1,1,1,1,0,0},
        {0,1,0,1,0,1,0,1,0,0},
        {0,1,0,1,0,1,0,1,0,0},
        {0,1,0,0,0,0,0,0,0,0}
    };

    
    // calculate height and width
    int height = sizeof(maze) / sizeof(maze[0]);
    int width = sizeof(maze[0]) / sizeof(maze[0][0]);

    // change the end nodes
    for ( int i = 0; i <= width; i++) {
        if (maze[0][i] == 1) {
            maze[0][i] = 2;
        };
        if (maze[height-1][i] == 1) {
            maze[height-1][i] = 2;
        };
    };

    std::cout << "Maze\n";
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++){
            std::cout << maze[y][x] << " ";
            if (x == (width-1)) {
                std::cout << "\n";
            };
        };
    };

    std::cout << "\n\n";
    
    // while loop to repeat the dead End algorithm until no more dead ends
    int changes;
    int counter;
    while (true) {
        changes = 0;
        
        for (int i = 1; i < (width-1); i++) {
            for (int j = 1; j < (height-1); j++) {
                if (maze[j][i] == 1){
                    counter = 0;

                    if (maze[j+1][i] > 0.5){
                        counter++;
                    };
                    if (maze[j-1][i] > 0.5){
                        counter++;
                    };
                    if (maze[j][i+1] > 0.5){
                        counter++;
                    };
                    if (maze[j][i-1] > 0.5){
                        counter++;
                    };
                    if (counter == 1) {
                        maze[j][i] = 0;
                        changes++;
                    };
                };
            };
        };
        if (changes == 0){
            break;
        };
    };

    // plot the final maze
    
    std::cout << "Maze complete!\n\n";
    std::cout << "height: " << height << "\n";
    std::cout << "width: " << width << "\n";
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++){
            std::cout << maze[y][x] << " ";
            if (x == (width-1)) {
                std::cout << "\n";
            };
        };
    };
    std::cout << "\n";
    
    return 0;
}