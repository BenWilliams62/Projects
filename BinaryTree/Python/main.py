from Tree import binaryTree, print_tree
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
    root = binaryTree('root')
    a = root.insert_left_node("a")
    b = root.insert_right_node("b")
    c = a.insert_left_node("c")
    d = a.insert_right_node("d")

    print_tree(root)


if __name__ == "__main__":
    main()
