from string import ascii_lowercase
import copy

class tree:
	def __init__(self):
		self.root = None

	class Node:
		def __init__(self,value):
			self.value = value
			self.left = None
			self.right = None
			self.depth = None

def TreeDeclaration():
	# Tree declaration
	mainTree = tree()
	Root = mainTree.Node('_')
	Temporary = mainTree.Node('_')
	Empty = mainTree.Node('/')

	mainTree.root = Root

	# Declaration of the Nodes
	di = {}		#di = dictionary
	# For a-z
	for ch in ascii_lowercase:
		node = mainTree.Node(ch)
		di[ch] = node
	# For 0 to 9
	for i in range(10):
		node = mainTree.Node(str(i))
		di[str(i)] = node

	# print(di['1'].value)

	Root.left = di['e']
	Root.right = di['t']
	Root.depth = 0

	di['e'].left = di['i']
	di['e'].right = di['a']
	di['e'].depth = 1

	di['t'].left = di['n']
	di['t'].right = di['m']
	di['t'].depth = 1

	di['i'].left = di['s']
	di['i'].right = di['u']
	di['i'].depth = 2

	di['a'].left = di['r']
	di['a'].right = di['w']
	di['a'].depth = 2

	di['n'].left = di['d']
	di['n'].right = di['k']
	di['n'].depth = 2

	di['m'].left = di['g']
	di['m'].right = di['o']
	di['m'].depth = 2

	di['s'].left = di['h']
	di['s'].right = di['v']
	di['s'].depth = 3

	di['u'].left = di['f']
	di['u'].right = copy.deepcopy(Temporary)
	di['u'].depth = 3

	di['r'].left = di['l']
	di['r'].right = copy.deepcopy(Temporary)
	di['r'].depth = 3

	di['w'].left = di['p']
	di['w'].right = di['j']
	di['w'].depth = 3

	di['d'].left = di['b']
	di['d'].right = di['x']
	di['d'].depth = 3

	di['k'].left = di['c']
	di['k'].right = di['y']
	di['k'].depth = 3

	di['g'].left = di['z']
	di['g'].right = di['q']
	di['g'].depth = 3

	di['o'].left = copy.deepcopy(Temporary)
	di['o'].right = copy.deepcopy(Temporary)
	di['o'].depth = 3

	# di['h'].left = di['5']
	# di['h'].right = di['4']
	# di['h'].depth = 4

	# di['v'].left = copy.deepcopy(Empty)
	# di['v'].right = di['3']
	# di['v'].depth = 4

	# di['f'].left = copy.deepcopy(Empty)
	# di['f'].right = copy.deepcopy(Empty)
	# di['f'].depth = 4

	# di['o'].left = copy.deepcopy(Empty)
	# di['o'].right = copy.deepcopy(Empty)
	# di['o'].depth = 4

	# di['o'].left = copy.deepcopy(Empty)
	# di['o'].right = copy.deepcopy(Empty)
	# di['o'].depth = 4

	# di['o'].left = copy.deepcopy(Empty)
	# di['o'].right = copy.deepcopy(Empty)
	# di['o'].depth = 4

	# di['o'].left = copy.deepcopy(Empty)
	# di['o'].right = copy.deepcopy(Empty)
	# di['o'].depth = 4

	# di['o'].left = copy.deepcopy(Empty)
	# di['o'].right = copy.deepcopy(Empty)
	# di['o'].depth = 4

	# di['o'].left = copy.deepcopy(Empty)
	# di['o'].right = copy.deepcopy(Empty)
	# di['o'].depth = 4

	# di['o'].left = copy.deepcopy(Empty)
	# di['o'].right = copy.deepcopy(Empty)
	# di['o'].depth = 4

	# di['o'].left = copy.deepcopy(Empty)
	# di['o'].right = copy.deepcopy(Empty)
	# di['o'].depth = 4

	# di['o'].left = copy.deepcopy(Empty)
	# di['o'].right = copy.deepcopy(Empty)
	# di['o'].depth = 4

	# di['o'].left = copy.deepcopy(Empty)
	# di['o'].right = copy.deepcopy(Empty)
	# di['o'].depth = 4

	# di['o'].left = copy.deepcopy(Empty)
	# di['o'].right = copy.deepcopy(Empty)
	# di['o'].depth = 4

	# di['o'].left = copy.deepcopy(Empty)
	# di['o'].right = copy.deepcopy(Empty)
	# di['o'].depth = 4

	# di['o'].left = copy.deepcopy(Empty)
	# di['o'].right = copy.deepcopy(Empty)
	# di['o'].depth = 4

	# print(mainTree.root.left.left.value)
	# for x in di:
	# 	if di[x].left != None and di[x].right !=None:
	# 		print(di[x].value,di[x].left.value,di[x].right.value)

	return mainTree


TreeDeclaration()