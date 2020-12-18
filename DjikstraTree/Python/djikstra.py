# an implementation of djikstras algorithm

# node_list is a list of all nodes in a graph

def djikstra(node_list):
    
    # create a set of unvisited nodes
    unvisited_set = set(node_list)

    # create a current node variable
    current_node = None

    # all tentative distances are 1000000000 by default
    # find start node and set distance to 0
    for node in unvisited_set:
        if node.rootName == "start":
            node.distance = 0
            # current_node = node
            node.previous = None
            break
    
    # set test_path = 0
    test_path = 0

    # while loop to go through all the nodes
    while True:

        # find the node with the lowest tentative distance
        test = 1000000000
        for node in unvisited_set:
            if node.distance < test:
                current_node = node
                test = current_node.distance
            
        # checking for neighbour nodes
        # check up
        if current_node.up in unvisited_set:
            if (current_node.up_path + test_path) < current_node.up.distance:
                current_node.up.distance = current_node.up_path + test_path
                current_node.up.previous = current_node
        
        # check down
        if current_node.down in unvisited_set:
            if (current_node.down_path + test_path) < current_node.down.distance :
                current_node.down.distance = test_path
                current_node.down.previous = current_node
                print("success")
    

        # check left
        if current_node.left in unvisited_set:
            if (current_node.left_path + test_path) < current_node.left.distance:
                current_node.left.distance = current_node.left_path+ test_path
                current_node.left.previous = current_node

        # check right
        if current_node.right in unvisited_set:
            if (current_node.right_path + test_path) < current_node.right.distance:
                current_node.right.distance = current_node.right_path+ test_path
                current_node.right.previous = current_node
        

        # remove this node from the set
        unvisited_set.remove(current_node)
        test_path += current_node.distance

        # if the final node isnt in the set, then end
        if current_node.rootName == "end":
            break



    # create path to be returned
    returnpath = []

    # loop through nodes to append previous node
    while True:
        # append the current node
        returnpath.append(current_node)

        # if current node is start, then end, if not find next previous
        if current_node.rootName == "start":
            break
        else:
            # find the previous node
            previous = current_node.previous
            current_node = previous

    # return the path. N.B. list is in reverse, so might have to be flipped later
    return returnpath





        
        