#Minimal Tree: Given a sorted(increasing order) array with unique integer elements,
#write an algorithm to create a binary search tree with minimal length
import pdb

class Node:
    val = 0
    left = None
    right = None

def minimalTree(arr, i, j):
    if j < i:
        return None
    else:
        cut = (i + j) / 2
        root = Node()
        root.val = arr[cut]
        root.left = minimalTree(arr, i, cut - 1)
        root.right = minimalTree(arr, cut + 1, j)
        return root

def inOrderTraversal(node):
    if node.left is not None:
        inOrderTraversal(node.left)
    print node.val
    if node.right is not None:
        inOrderTraversal(node.right)


#testing
arr =[1,2,3,4,5,6,7,8,9,10,11,12]
myroot = minimalTree(arr, 0, 11)
inOrderTraversal(myroot)
