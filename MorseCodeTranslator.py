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
			currMorse = SearchInTree(letter)

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
			print(currMorse)
			break

		if currNode[0].depth<=4:
			if currNode[0].left!=None:
				temp = currMorse
				temp += '.'
				totalList.append([currNode[0].left,temp])

			if currNode[0].right!= None:
				temp = currMorse
				temp +='-'
				totalList.append([currNode[0].right,temp])
		counter+=1

if __name__ == '__main__':
	ChangeToEnglish('.... ..- ---')
	ChangeToMorseCode('huo')
