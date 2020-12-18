class Node:

    # initialise
    def __init__(self, nodeName):

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
