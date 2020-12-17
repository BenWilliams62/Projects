class binaryTree:

    # initiate
    def __init__(self, rootId):
        self.left = None
        self.right = None
        self.rootId = rootId
    
    # get left child
    def get_left_child(self):
        return self.left
    
    # get right child
    def get_right_child(self):
        return self.right

    # change node value
    def set_node_value(self, value):
        self.rootId = value
    
    # return node value
    def get_node_value(self):
        return self.rootId

    # add new nodes
    
    # add right node
    def insert_right_node(self, nodeValue):
        if self.right == None:
            self.right = binaryTree(nodeValue)
            return self.right
        else:
            tree = binaryTree(nodeValue)
            tree.right = self.right
            self.right = tree
            return self.right
    
    # add left node
    def insert_left_node(self, nodeValue):
        if self.left == None:
            self.left = binaryTree(nodeValue)
            return self.left
        else:
            tree = binaryTree(nodeValue)
            tree.right = self.right
            self.right = tree
            return self.left
    
def print_tree(tree):
    if tree != None:
        print(tree.get_node_value())
        print_tree(tree.get_left_child())
        print_tree(tree.get_right_child())
        print()

class node:

    # initialise
    def __init__(self, value):
        self.rootId = value
        self.left = None
        self.right = None

