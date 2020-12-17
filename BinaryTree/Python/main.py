from Tree import binaryTree, print_tree, node
# create a tree of 
'''
root
|   \
|    \
|     \
a      b
|\
| \
|  \
c   d
'''

def main():

    # longer method
    root = binaryTree('root')
    a = root.insert_left_node("a")
    b = root.insert_right_node("b")
    c = a.insert_left_node("c")
    d = a.insert_right_node("d")

    print_tree(root)


    # shorter method
    root2 = node("root2")
    a2 = node("a2")
    b2 = node("b2")
    c2 = node("c2")
    d2 = node("d2")

    root2.left = a2
    root2.right = b2

    a2.left = c2
    a2.right = d2



if __name__ == "__main__":
    main()
