import DataStructures


class DataEntry:
	circuit_topology_list = []	

	node_list = []

	node_list.append("V1")
	node_list.append("V2")
	node_list.append("V3")
	node_list.append("GND")

	Sum = [[0,0,0],[0,0,0],[0,0,0]]	

	R1 = 1000
	R2 = 3000
	R3 = 1500
	R4 = 4700
	R5 = 800
	R6 = 1500
	R7 = 5000
	
	V_1 = 12
	V_2 = 9

	# getter method 
	def get_circuit_topology_list(self): 
		return self.circuit_topology_list

	# getter method 
	def get_node_list(self): 
		return self.node_list

	# setter method 
	def set_sum(self,sum): 
		self.Sum = sum

	# getter method 
	def get_sum(self): 
		return self.Sum

	def UseTestData(self):
		#----------------------------------------------------------------------------	
		#Add Node V1
		#----------------------------------------------------------------------------	
		node = DataStructures.Node("V1")

		circuitTopo = DataStructures.CircuitTopology()
		circuitTopo.add_node(node)

		#----------------------------------------------------------------------------	
		# Add V_1 Branch to Node V1
		#----------------------------------------------------------------------------	
		branch = DataStructures.Branch("V_1",DataStructures.Type.VOLTAGE_SOURCE,self.V_1,"GND","+")
		circuitTopo.add_branch(branch)

		#----------------------------------------------------------------------------	
		# Add R1 Branch to Node V1
		#----------------------------------------------------------------------------	
		branch = DataStructures.Branch("R1",DataStructures.Type.RESISTOR,self.R1,"GND","*")
		circuitTopo.add_branch(branch)

		#----------------------------------------------------------------------------	
		# Add R2 Branch to Node V1
		#----------------------------------------------------------------------------	
		branch = DataStructures.Branch("R2",DataStructures.Type.RESISTOR,self.R2,"V2","*")
		circuitTopo.add_branch(branch)

		#----------------------------------------------------------------------------	
		# Add R3 Branch to Node V1
		#----------------------------------------------------------------------------	
		branch = DataStructures.Branch("R3",DataStructures.Type.RESISTOR,self.R3,"V2","*")
		circuitTopo.add_branch(branch)

		self.circuit_topology_list.append(circuitTopo)
		
		#----------------------------------------------------------------------------	
		#Add Node V2
		#----------------------------------------------------------------------------	
		node = DataStructures.Node("V2")

		circuitTopo = DataStructures.CircuitTopology()
		circuitTopo.add_node(node)

		#----------------------------------------------------------------------------	
		# Add R2 Branch to Node V2
		#----------------------------------------------------------------------------	
		branch = DataStructures.Branch("R2",DataStructures.Type.RESISTOR,self.R3,"V1","*")
		circuitTopo.add_branch(branch)
		
		#----------------------------------------------------------------------------	
		# Add R3 Branch to Node V2
		#----------------------------------------------------------------------------	
		branch = DataStructures.Branch("R3",DataStructures.Type.RESISTOR,self.R2,"V1","*")
		circuitTopo.add_branch(branch)

		#----------------------------------------------------------------------------	
		# Add R4 Branch to Node V2
		#----------------------------------------------------------------------------	
		branch = DataStructures.Branch("R4",DataStructures.Type.RESISTOR,self.R4,"GND","*")
		circuitTopo.add_branch(branch)

		#----------------------------------------------------------------------------	
		# Add V_2 Branch to Node V2
		#----------------------------------------------------------------------------	
		branch = DataStructures.Branch("V_2",DataStructures.Type.VOLTAGE_SOURCE,self.V_2,"V3","+")
		circuitTopo.add_branch(branch)

		self.circuit_topology_list.append(circuitTopo)
		#----------------------------------------------------------------------------	
		# Add Node V3
		#----------------------------------------------------------------------------	
		node = DataStructures.Node("V3")
		circuitTopo = DataStructures.CircuitTopology()
		circuitTopo.add_node(node)
		
		#----------------------------------------------------------------------------	
		# Add V_2 Branch to Node V3
		#----------------------------------------------------------------------------	
		branch = DataStructures.Branch("V_2",DataStructures.Type.VOLTAGE_SOURCE,self.V_2,"V2","-")
		circuitTopo.add_branch(branch)
		
		#----------------------------------------------------------------------------	
		# Add R5 Branch to Node V3
		#----------------------------------------------------------------------------	
		branch = DataStructures.Branch("R5",DataStructures.Type.RESISTOR,self.R5,"GND","*")
		circuitTopo.add_branch(branch)
		
		#----------------------------------------------------------------------------	
		# Add R6 Branch to Node V3
		#----------------------------------------------------------------------------	
		branch = DataStructures.Branch("R6",DataStructures.Type.RESISTOR,self.R6,"GND","*")
		circuitTopo.add_branch(branch)

		#----------------------------------------------------------------------------	
		# Add R7 Branch to Node V3
		#----------------------------------------------------------------------------	
		branch = DataStructures.Branch("R7",DataStructures.Type.RESISTOR,self.R7,"GND","*")
		circuitTopo.add_branch(branch)

		self.circuit_topology_list.append(circuitTopo)	
		
		
		def RedData(self):
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
				