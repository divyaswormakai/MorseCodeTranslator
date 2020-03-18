from string import ascii_lowercase

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
	mainTree.root = Root

	# Declaration of the Nodes
	di = {}		#di = dictionary
	# For a-z
	for ch in ascii_lowercase:
		node = mainTree.Node(ch)
		di[ch] = node
	# # For 0 to 9
	# for i in range(10):
	# 	node = mainTree.Node(str(i))
	# 	di[str(i)] = node

	# print(di['1'].value)

	Root.left = di['e']
	Root.right = di['t']

	di['e'].left = di['i']
	di['e'].right = di['a']

	di['t'].left = di['n']
	di['t'].right = di['m']

	di['i'].left = di['s']
	di['i'].right = di['u']

	di['a'].left = di['r']
	di['a'].right = di['w']

	di['n'].left = di['d']
	di['n'].right = di['k']

	di['m'].left = di['g']
	di['m'].right = di['o']

	di['s'].left = di['h']
	di['s'].right = di['f']

	di['u'].left = di['f']
	di['u'].right = None

	di['r'].left = di['l']
	di['r'].right = None

	di['w'].left = di['p']
	di['w'].right = di['j']

	di['d'].left = di['b']
	di['d'].right = di['x']

	di['k'].left = di['c']
	di['k'].right = di['y']

	di['g'].left = di['z']
	di['g'].right = di['q']

	di['o'].left = None
	di['o'].right = None

	# print(mainTree.root.left.left.value)
	return mainTree


TreeDeclaration()