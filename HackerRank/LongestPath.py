maxHeight = -1

def height(root):
	DFS(root, -1)
	global maxHeight
	return maxHeight


def DFS(root, currentHeight):
	if root is not None:
		currentHeight+=1
		global maxHeight
		if currentHeight > maxHeight:
			maxHeight = currentHeight
		DFS(root.left, currentHeight)
		DFS(root.right, currentHeight)

