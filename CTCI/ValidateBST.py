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


