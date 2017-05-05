#Route between nodes: Given a directed graph, design an algorithm to find out whether there
#is a route between nodes
import pdb

class Node:
    val = 0
    nodes = []

def DFS (root, myNode):
    if root is None:
        return None
    elif root.val == myNode.val:
        return root
    else:
        for node in root.nodes:
            if node.val == myNode.val:
                return node
            else:
                DFS(node, myNode)

def isRoute (node1, node2):
    route1 = DFS(node1, node2)
    route2 = DFS(node2, node1)
    if route1 is not None or route2 is not None:
        return True
    else:
        return False

#testing
node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node5 = Node()
node6 = Node()
node7 = Node()
node8 = Node()
node9 = Node()
node10 = Node()

node1 = 1
node2 = 2
node3 = 3
node4 = 4
node5 = 5
node6 = 6
node7 = 7
node8 = 8
node9 = 9
node10 = 10

node1 = 1
node2 = 2
node3 = 3
node4 = 4
node5 = 5
node6 = 6
node7 = 7
node8 = 8
node9 = 9
node10 = 10


print isRoute (node2, node4)
