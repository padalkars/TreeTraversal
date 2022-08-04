class Tree():
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value
		
	def get_root(self):
		return self
		
class BST(Tree):
	def __init__(self, arr):
		self.arr = arr #Initialize the array
	
	def create_tree(self, root, value):
		if(root == None):
			tree_obj = Tree(value) #Initialize a root object
			root = tree_obj.get_root()
			
			return root
			
		if(value<=root.value):
			#Go to left
			root.left = self.create_tree(root.left, value)
		
		if(value > root.value):
			#Go to right
			root.right = self.create_tree(root.right, value)
			
		return root
					
	def inOrder(self, root):
		if(root):
			self.inOrder(root.left)
			print(root.value)
			self.inOrder(root.right)
	
	def preOrder(self, root):
		if(root):
			print(root.value)
			self.preOrder(root.left)
			self.preOrder(root.right)
			
	def postOrder(self, root):
		if(root):
			self.postOrder(root.left)
			self.postOrder(root.right)
			print(root.value)
	
	def get_height(self, root):
		if(not root):
			return 0
			
		if(root.left):
			left_height = 1 + self.get_height(root.left)
		
		if(root.right):
			right_height = 1 + self.get_height(root.right)
			
		return max(left_height, right_height)
	
	def levelOrder(self, root):
		height_of_tree = self.get_height(root)
		
	
	def driver(self):
		#Insert nodes at the respective positions in the tree
		root=None
		for value in self.arr:
			root = self.create_tree(root, value)
		
		#Inorder Traversal
		print("In-order traversal")
		self.inOrder(root)
		
		print("Pre-order traversal")
		self.preOrder(root)
		
		print("Post-order traversal")
		self.postOrder(root)

#Start
n = int(input("Enter the number of entries in the array:- "))
arr = list(map(int, input().split()))

arr = arr[:n]

#Create the object of BST and call the driver
bst_obj = BST(arr)
bst_obj.driver()
		
