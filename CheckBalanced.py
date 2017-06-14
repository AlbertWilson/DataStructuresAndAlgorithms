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

node1.left = node2
node1.right = node3

node2.left = node4
node4.left = node10

print checkBalanced(node1)
