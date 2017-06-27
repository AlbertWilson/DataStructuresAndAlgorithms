def topView(root):
  leftTraversal(root)
  if root.right is not None:
  	rightTraversal(root.right)

def leftTraversal(root):
	if root is not None:
		leftTraversal(root.left)
		print root.data,

def rightTraversal(root):
	if root is not None:
		print root.data,
		rightTraversal(root.right)