"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
class Node():
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

def preOrder(root):
    if root is not None:
    	print root.data,
    	preOrder(root.left)
    	preOrder(root.right)

def postOrder(root):
	if root is not None:
		postOrder(root.left)
		postOrder(root.right)
		print root.data,

def inOrder(root):
	if root is not None:
		inOrder(root.left)
		print root.data,
		inOrder(root.right)