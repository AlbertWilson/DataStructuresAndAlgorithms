def wordCount(word):
	words = 1
	for i in range(len(word)):
		if word[i].isupper():
			words+=1
	print words


wordCount("saveChangesInTheEditor")