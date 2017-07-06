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


