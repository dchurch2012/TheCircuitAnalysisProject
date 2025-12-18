from enum import Enum

# DataStructures.py
if __name__ == "__main__":
    print("This is the DataStructures.py file.")
	
	
class Type(Enum):
	VOLTAGE_SOURCE = 0
	RESISTOR = 1
	CAPACITOR = 2
	CURRENT_SOURCE = 3
	
class Node:
	# define a property
	Name = ""
	
	def __init__(self,name):
		self.Name = name

class CircuitTopology:
	def clear_branches(self):
		self.Branches.clear()
	
	def add_node(self, node):
		self.Node = node
	
	def add_branch(self, branch):
		self.Branches.append(branch)
		
	def __init__(self):
		self._my_unique = object()
		self.Branches = []
		self.Node = None

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
		