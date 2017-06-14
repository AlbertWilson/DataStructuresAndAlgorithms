#Successor: Write an algorithm to find the "next" node(i.e in-order successor) of a given node in a binary search tree.
#You can assume that each node has a link to its parent.

import pdb

class Node:
    left = None
    right = None
    val = 0

def successor(root, node):
    arr = []
    arr = inOrderList(root, arr)
    for index in range(len(arr)):
        if arr[index].val == node.val and index < len(arr) - 1:
            return arr[index + 1].val

    print "The node does not have a next node"


def inOrderList(root, arr):
    if root.left is not None:
        inOrderList(root.left, arr)
    arr.append(root)
    if root.right is not None:
        inOrderList(root.right, arr)
    return arr

node1 = Node()
node1.val = 1
node2 = Node()
node2.val = 2
node3 = Node()
node3.val = 3
node4 = Node()
node4.val = 4
node5 = Node()
node5.val = 5
node6 = Node()
node6.val = 6
node7 = Node()
node7.val = 7
node8 = Node()
node8.val = 8
node9 = Node()
node9.val = 9
node10 = Node()
node10.val = 10

node5.left = node2
node5.right = node7

node2.left = node1
node2.right = node3

node7.left = node6
node7.right = node8

print successor(node5, node8)
