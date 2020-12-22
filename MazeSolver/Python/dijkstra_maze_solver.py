import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from functions import Node, djikstra, node_parse, connection_parse, colour_maze, deadEndBlocking
import datetime as datetime


def main():

    # ask for image input
    mazePath = os.path.join(os.path.dirname(os.path.realpath(__file__)),"../Mazes/")
    for file in os.listdir(mazePath):
        print(file)

    # ask for input
    mazeInput = str(input("\nWhich maze would you like solved?\n(type the name without the extension)\n"))
    
    # start timer
    start_time = datetime.datetime.now()

    # turn image into array
    image = Image.open(str(mazePath)+'/'+mazeInput+'.png')
    width, height = image.size
    maze = np.array(image)

    # block off all deadends - slower project but better memory management
    changes = 1
    while changes > 0:
        maze, changes = deadEndBlocking(maze,width,height)



    # parse maze for nodes
    maze, nodes = node_parse(height, width, maze)
    
    # parse nodes for edges
    connection_parse(nodes, maze, width, height)


    # with nodes connected, find path
    route = djikstra(nodes)
    nodes.clear()
    print("route:")
    route_list = []
    for node in route:
        route_list.append(node.get_node())
    
    print(route_list)

    # to present the maze, use an un altered maze
    image = Image.open(str(mazePath)+'/'+mazeInput+'.png')
    width, height = image.size
    maze = np.array(image)
    solution = colour_maze(route, maze)

    # finish and print timing
    end_time = datetime.datetime.now()
    run_time = end_time - start_time
    print("runtime is: ", run_time)

    print()
    plt.figure("final maze")
    plt.clf()
    plt.imshow(solution)
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    main()