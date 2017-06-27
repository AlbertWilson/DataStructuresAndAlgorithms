def levelOrder(root):
	currentLevel = [root]
	while currentLevel:
		nextLevel = list()
		for n in currentLevel:
			print n.data,
			if n.left is not None:
				nextLevel.append(n.left)
			if n.right is not None:
				nextLevel.append(n.right)
		currentLevel = nextLevel


