from multiprocessing import Pool

'''
#   #   #   #   #   #   #   #   #
# object definistion for node   #
#   #   #   #   #   #   #   #   #
'''

class Node:

    # initialise
    def __init__(self, nodeName,x ,y):

        self.rootName = nodeName

        # nodes in each direction
        self.left = None
        self.left_path = None
        self.right = None
        self.right_path = None
        self.up = None
        self.up_path = None
        self.down = None
        self.down_path = None
        self.x_pos = x
        self.y_pos = y

        # for djikstra
        self.previous = None
        self.distance = 1000000000
        
    # funciton to add left node
    def add_left_node(self, node, length):

        self.left = node
        self.left_path = length

        node.right = self
        node.right_path = length


    # funciton to add left node
    def add_right_node(self, node, length):

        self.right = node
        self.right_path = length

        node.left = self
        node.left_path = length
    

    # funciton to add up node
    def add_up_node(self, node, length):

        self.up = node
        self.up_path = length

        node.down = self
        node.down_path = length
    

    # funciton to add down node
    def add_down_node(self, node, length):

        self.down = node
        self.down_path = length

        node.up = self
        node.up_path = length

    def get_node(self):
        return self.rootName

    def add_previous(self, node):
        self.previous = node
    
    def get_previous(self):
        return self.previous
    
    def get_up(self):
        return self.up.get_node()

    def get_down(self):
        return self.down.get_node()

    def get_left(self):
        return self.left.get_node()

    def get_right(self):
        return self.right.get_node()

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos

    def change_distance(self, length):
        self.distance = length



'''
#   #   #   #   #   #
# find all nodes    #
#   #   #   #   #   #
'''

def node_parse(height, width, maze):

    # define start and end node
    for i in range(width):
        if maze[0][i] == 1:
            start = Node("start", i, 0)
            start.change_distance(0)
            maze[0][i] = 4
        if maze[-1][i] == 1:
            end = Node("end", i, height - 1)
            maze[-1][i] = 4

    # add nodes to list
    nodes = [
        start,
        end
    ]
    node_name = 1

    for j in range(1, height - 1):
        for i in range(1, width - 1):

            # check if position is white
            if maze[j][i] == 1:

                # check if position is a node
                if (maze[j-1][i] >= 1 or maze[j+1][i] >= 1) and (maze[j][i+1] >= 1 or maze[j][i-1] >=1):
                    nodes.append(Node(str(node_name), i, j))
                    node_name += 1
    
    return maze, nodes



'''
#   #   #   #   #   #   #   #
# check up for connections  #
#   #   #   #   #   #   #   #
'''

def check_up(nodes, maze, height):
    # for every node, check up for another node
    for node in  nodes:
        x = node.get_x_pos()
        y = node.get_y_pos()
        path = 0
        
        # while y is in the range of height of the maze, check if the next
        # position is a 1, if it is, check for a node, if no node, continue. if a node
        # break, and add edge to current node and found node
        while y > 0:
            breaking = 0
            if maze[y-1][x] >= 1:
                y -= 1
                path += 1
                for node_searched in nodes:
                    if node_searched.get_x_pos() == x and node_searched.get_y_pos() == y:
                        node.add_up_node(node_searched, path)
                        breaking = 1
                        break
                if breaking == 1:
                    break
            else:
                break


'''
#   #   #   #   #   #   #   #   #
# check left for connections    #
#   #   #   #   #   #   #   #   #
'''

def check_left(nodes, maze, width):
    # for every node, check left for another node
    for node in  nodes:
        x = node.get_x_pos()
        y = node.get_y_pos()
        path = 0

        while x > 0:
            breaking = 0
            if maze[y][x-1] >= 1:
                x -= 1
                path += 1
                for node_searched in nodes:
                    if node_searched.get_x_pos() == x and node_searched.get_y_pos() == y:
                        node.add_left_node(node_searched, path)
                        breaking = 1
                        break
                if breaking == 1:
                    break
            else:
                break
                


'''
#   #   #   #   #   #   #   #   #   #
# check connections between nodes   #
#   #   #   #   #   #   #   #   #   #
'''


def connection_parse(nodes, maze, width, height):
    
    # split between two cores for faster processing
    with Pool(2) as pool:
        pool.imap(check_up(nodes,maze,height), nodes)
    #check_up(nodes,maze,height) # dont need to check down, because it will have been connected in the up check
        pool.imap(check_left(nodes,maze,width), nodes) # dont need to check right, because connections were made on the left check



'''
#   #   #   #   #   #   #
# dijkstra's algorithm  #
#   #   #   #   #   #   #
'''

def djikstra(nodes):

    # created a set of unvisited nodes
    unvisited_set = set(nodes)
    current_node = None

    # while loop to implement dijkstra's algorithm for every node
    while True:
        # get the node with the shortest distance
        test = 1000000000

        current_node = None
        for node in unvisited_set:
            if node.distance < test:
                current_node = node
                test = current_node.distance
                test_path = test
        
        # check for neighbour nodes
        # check up
        if current_node.up in unvisited_set:
            if current_node.up_path + test_path < current_node.up.distance:
                current_node.up.change_distance(current_node.up_path + test_path)
                current_node.up.add_previous(current_node)
                
        
        # check down
        if current_node.down in unvisited_set:
            if current_node.down_path + test_path < current_node.down.distance:
                current_node.down.change_distance(current_node.down_path + test_path)
                current_node.down.add_previous(current_node)


        # check left
        if current_node.left in unvisited_set:
            if current_node.left_path + test_path < current_node.left.distance:
                current_node.left.change_distance(current_node.left_path + test_path)
                current_node.left.add_previous(current_node)
                

        # check right
        if current_node.right in unvisited_set:
            if current_node.right_path + test_path < current_node.right.distance:
                current_node.right.change_distance(current_node.right_path + test_path)
                current_node.right.add_previous(current_node)


        # remove node or exit
        if current_node.get_node() == "end":
            break
        
        unvisited_set.remove(current_node)
        nodes.remove(current_node)
    
    # return the list of nodes visited
    return_list = []

    print("total length: ", current_node.distance)

    while True:
        if current_node.previous != None:
            return_list.append(current_node)
            previous = current_node.previous
            current_node = previous
        else:
            return_list.append(current_node)
            break
    
    unvisited_set.clear()
    nodes.clear
    
    return return_list[::-1]


'''
#   #   #   #   #   #   #   #   #   #   #
# dijkstra's algorithm colouring maze   #
#   #   #   #   #   #   #   #   #   #   #
'''

def colour_maze(nodes, maze):
    for i in range(len(nodes)-1):
        # get x and y position for node and next node
        x_1 = nodes[i].get_x_pos()
        y_1 = nodes[i].get_y_pos()

        x_2 = nodes[i+1].get_x_pos()
        y_2 = nodes[i+1].get_y_pos()

        # if in x plane
        if y_1 == y_2:
            if x_1 > x_2:
                x_1, x_2 = x_2, x_1
            for j in range(x_1, x_2+1):
                maze[y_1][j] = 2
        if x_1 == x_2:
            if y_1 > y_2:
                y_1, y_2 = y_2, y_1
            for j in range(y_1, y_2+1):
                maze[j][x_1] = 2
        
    return maze

'''
#   #   #   #   #   #
# dead end blocking #
#   #   #   #   #   #
'''

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