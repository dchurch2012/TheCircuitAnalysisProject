
class Branch:
	Name = ""
	Type = 0
	Value = 0
	EndNode = ""
	Polarity = "*"
	
	def __init__(self,name,type,value,node,polarity):
		self.Name = name
		self.Value = value
		self.Type = type
		self.EndNode = node
		self._my_unique = object()
		self.Polarity = polarity

while True:
	user_input = input("Enter Component Name: ")

	if user_input == "":
		break

	# Enter Component Name
	Name = user_input

	print("Compnent Name:", user_input)

	# Enter Component Value
	user_input = input("Enter Component Value: ")

	Value = user_input
	print("Compnent Value:", Value)

	# Enter Component Start Node
	user_input = input("Enter Component Start Node: ")

	startNode = user_input
	print("Compnent Start Node:", startNode)

	# Enter Component End Node
	user_input = input("Enter Component End  Node: ")

	endNode = user_input
	print("Compnent End Node:", endNode)

	# Enter Component Polarity : +,- or *
	user_input = input("Enter Component Polarity: ")

	polarity = user_input
	print("Compnent Polarity:", polarity)
	
	Type = 1
	
	branch = Branch(Name,Value,Type,endNode,polarity)

	
#while True:
#	try:
#		number = int(input("Please enter a number: "))
#		break  # Exit the loop if input is valid
#	except ValueError:
#		print("That's not a valid number. Please try again.")

	
	