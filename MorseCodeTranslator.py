from Tree import TreeDeclaration

mainTree = TreeDeclaration()

string = '..-. ..- -.-. -.-  -.-- --- ..-'
parts = string.split('  ')
finalStr = ''
for part in parts:
	words = part.split(' ')
	for word in words:
		currNode = mainTree.root
		for elem in word:
			if(elem == '.'):
				currNode = currNode.left
			elif(elem == '-'):
				currNode = currNode.right
		finalStr+=currNode.value
	finalStr+=" "

print(finalStr)

