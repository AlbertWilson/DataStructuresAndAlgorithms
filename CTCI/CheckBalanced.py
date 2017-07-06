#Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes
#of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees
#of any node never differ by more than one
#Correct!

import pdb

class Node:
    left = None
    right = None
    val = 0

def depthCount(root):
    if root is None:
        return 0

    return 1 + max(depthCount(root.left), depthCount(root.right))

def checkBalanced(root):

    if root is None:
        return True

    leftCount = depthCount(root.left)
    rightCount = depthCount(root.right)

    if abs(leftCount - rightCount) <= 1 and checkBalanced(root.left) and checkBalanced(root.right):
        return True

    return False

