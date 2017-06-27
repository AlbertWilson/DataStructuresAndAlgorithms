#Validate BST: Implement a function to check if a binary tree is a Binary Search tree
#Correct! But it would be nice to remove the isBST global variable
import pdb

class Node:
    val = 0
    left = None
    right = None

isBST = True #try and remove the global variable at some point

def validateBST(root):
    if root is None:
        return True

    if root.left is not None:
        if root.left.val < root.val:
            validateBST(root.left)
        else:
            global isBST
            isBST = False

    if root.right is not None:
        if root.right.val > root.val:
            validateBST(root.right)
        else:
            global isBST
            isBST = False

    return isBST

def validateBSTbyTraversal(root):
    arr = []
    arr = inOrderTraversal(root, arr)
    for index in range(len(arr) - 1):
        if arr[index] > arr[index + 1]:
            return False

    return True


def inOrderTraversal(root, arr):
    if root.left is not None:
        inOrderTraversal(root.left, arr)

    arr.append(root.val)

    if root.right is not None:
        inOrderTraversal(root.right, arr)

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

node8.right = node4

#print validateBST(node5)
print validateBSTbyTraversal(node5)
