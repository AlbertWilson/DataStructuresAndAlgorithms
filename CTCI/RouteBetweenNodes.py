#Route between nodes: Given a directed graph, design an algorithm to find out whether there
#is a route between nodes
#Correct!
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

