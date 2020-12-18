from Graph import Node
from djikstra import djikstra

'''
create a graph such as:

start
|
|
|
a-------b
|       |
|       |
|       |
c-------d-----end
'''


def main():
    print("\n\n")
    
    # create nodes
    start = Node("start")
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    end = Node("end")


    # join nodes
    start.add_down_node(a, 3)
    a.add_right_node(b,7)
    a.add_down_node(c,3)
    d.add_up_node(b,3)
    c.add_right_node(d, 7)
    d.add_right_node(end,5)

    # create list of nodes
    node_list = [
        start,
        a,
        b,
        c,
        d,
        end
    ]

    path = djikstra(node_list)

    final_path = path[::-1]
    for node in final_path:
        print(node.get_node())

    

if __name__ == "__main__":
    main()