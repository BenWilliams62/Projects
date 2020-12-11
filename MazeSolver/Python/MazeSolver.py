import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# add function to import mazes
mazePath = os.path.join(os.path.dirname(os.path.realpath(__file__)),"../Mazes/")
for file in os.listdir(mazePath):
    print(file)

# ask for input
mazeInput = str(input("\nWhich maze would you like solved?\n(type the name without the extension)\n"))
image = Image.open(str(mazePath)+'/'+mazeInput+'.png')
width, height = image.size
maze = np.array(image)

# calculate the dimensions of the maze



# define start and end nodes
def endNodes(maze, width):
    for i in range(width):
            if maze[0][i] == 1:
                maze[0][i] = 3
            if maze[-1][i] == 1:
                maze[-1][i] = 2
    return maze

# create function for dead end block algorithm
def deadEndBlocking(maze, width, height):
    changes = 0
    for i in range(1, width-1):
        for j in range(1, height-1):
            if maze[j][i] == 1:
                counter = 0

                if maze[j+1][i] > 0.75:
                    counter += 1
                if maze[j-1][i] > 0.75:
                    counter += 1
                if maze[j][i+1] > 0.75:
                    counter += 1
                if maze[j][i-1] > 0.75:
                    counter += 1
                
                if counter  == 1:
                    maze[j][i] = 0.75
                    changes += 1
                    
                
    return maze, changes

# define the start and end points clearly in the maze
mazeNodes = endNodes(maze, width)

# search the original dead ends
solution, changes = deadEndBlocking(mazeNodes, width, height)

loop = 1
while True:
    solution, changes = deadEndBlocking(solution, width, height)
    loop += 1
    if changes == 0:
        print(loop)
        break

###
# can choose to apply djikstras algorithm here, knowing the possible solutions

# display the solved maze
plt.figure('maze solution')
plt.clf()
plt.imshow(solution)
plt.colorbar()
plt.show()