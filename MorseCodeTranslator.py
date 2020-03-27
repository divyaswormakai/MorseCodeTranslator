from Tree import TreeDeclaration

mainTree = TreeDeclaration()

def ChangeToEnglish(string):
	parts = string.split('  ')
	finalStr = ''
	for part in parts:
		words = part.split(' ')
		for word in words:
			currNode = mainTree.root
			for elem in word:
				if elem == '.' and currNode.left.value!= '_':
					currNode = currNode.left
				elif elem == '-' and currNode.right.value!= '_':
					currNode = currNode.right
			finalStr += currNode.value
		finalStr+=" "
	print(finalStr)

def ChangeToMorseCode(string):
	parts = string.split(' ')
	finalCode = ''
	for part in parts:
		currMorse = ''
		for letter in part:
			rootNode = mainTree.root
			currMorse = SearchInTree(letter.lower())
			finalCode += currMorse+' '
		finalCode += '\n'
	print(finalCode)
	return finalCode

def SearchInTree(letter):
	currNode = mainTree.root
	totalList = list()
	currMorse = ''
	totalList.append([currNode,currMorse])
	complete = False
	counter = 0

	#A Simple BFS of the tree to the find the coorect morse code for the alphabet
	while not complete:
		currNode = totalList[counter]
		currMorse = currNode[1]
		if currNode[0].value == letter:
			complete = True
			break

		if currNode[0].left!=None:
			temp = currMorse
			temp += '.'
			totalList.append([currNode[0].left,temp])

		if currNode[0].right!= None:
			temp = currMorse
			temp +='-'
			totalList.append([currNode[0].right,temp])
		counter+=1
	return currMorse

if __name__ == '__main__':
	ChangeToEnglish('.... ..- --- ..-.')
	ChangeToMorseCode('huof huo')
