"""
goal is to obtain the cheapest cost in the tree. 
this needs a dfs
"""

class Node():
    def __init__(self, cost, children=[]):
        self.cost = cost
        self.children = children

    def __repr__(self):
        return "{}".format(self.cost)
    
class TreeOfNodes():
    def __init__(self, start=Node(0), cheapest_cost=None, cheapest_path=[]):
        self.cheapest_cost = cheapest_cost
        self.cheapest_path = cheapest_path
        self.start = start

        def find_cheapest_cost(self):
            root = self.start
            path = []

            def helper(current, path, path_cost):
                path.append(current)
                path_cost += current.cost

                if not current.children:
                    if not self.cheapest_cost or self.cheapest_cost > path_cost:
                        self.cheapest_cost = int(path_cost)
                        self.cheapest_path = list(path)
                else:
                    for n in current.children:
                        helper(n,path,path_cost)
                path.pop()
                path_cost -= current.cost

        
            helper(root, path, root.cost)
            return 
        find_cheapest_cost(self)



root = Node(0,
    [
        Node(5,[
            Node(4)]),
        Node(3,[
            Node(2,[
                Node(1,[
                    Node(1)])]),
            Node(0,[
                Node(10)])
            ]),
        Node(6,[
            Node(1),
            Node(5)
            ])

    ])

tree = TreeOfNodes(root)
print(tree.cheapest_path)
