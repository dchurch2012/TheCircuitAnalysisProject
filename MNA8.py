from __future__ import annotations

import DataStructures
import DataEntry

from enum import Enum
	
global row
global col

row = 0
col = 0

global dataEntry

def main():
	#IMPORT USED HERE:
	
	global circuit_topology_list
	global node_list
	
	dataEntry = DataEntry.DataEntry()
	dataEntry.UseTestData()
	
	circuit_topology_list = dataEntry.get_circuit_topology_list()
	node_list = dataEntry.get_node_list()
	
	#----------------------------------------------------------------------------	
	# Summary
	#----------------------------------------------------------------------------	
	print()
	#----------------------------------------------------------------------------	

	#----------------------------------------------------------------------------	
	#IN DEVELOPMENT
	#----------------------------------------------------------------------------	
	for circuit in circuit_topology_list:
		circuit.Branches.sort(key=lambda x: x.EndNode, reverse=False)

	print("----------------------------------------------------------------------------------")
	for circuit in circuit_topology_list:
		print(circuit.Node.Name)
		for branches in circuit.Branches:
			print(branches.EndNode,"\t",branches.Name,"\t",branches.Value,"\t",branches.Polarity)
		print("------------------------------------------------------------------------")

	print("--------------------Processing Diagonal Elements----------------------------------------------------------------")
	ProcessDiagonalElements(dataEntry)
	
	print("--------------------Processing Off Diagonal Elements------------------------------------------------------------")
	ProcessOffDiagonalElements(dataEntry)
	
	print("Sum Matrix : ",dataEntry.Sum)
	
def ProcessDiagonalElements(dataEntry):
	Sum = dataEntry.get_sum()
	
	for i in range(len(circuit_topology_list)):
		node = circuit_topology_list[i].Node.Name
		
		print("Node[",i,"]", "Name : ",node)

		for branch in circuit_topology_list[i].Branches:
			index = FindNode(branch.EndNode)
			print(branch.EndNode," thru ",branch.Name,"\t","col : ",col,"\t","Node[",i,"]","\t","Value :",branch.Value)


			if branch.Type == DataStructures.Type.RESISTOR:
				Sum[i][i] = Sum[i][i] + branch.Value

def ProcessOffDiagonalElements(dataEntry):
	index = 0
	Sum = dataEntry.get_sum()
	
	for i in range(len(circuit_topology_list)):
			
		node = circuit_topology_list[i].Node.Name
		
		print("Node ",node," Connects to ")
		
		for branch in circuit_topology_list[i].Branches:
			index = FindNode(branch.EndNode)
		
			if index != -1:
				print(branch.EndNode," thru ",branch.Name,"\t","Node[",i,"]","\t","Value :",branch.Value,"index : ",index)
			
			if index != 3:
				if branch.Type == DataStructures.Type.RESISTOR:
					Sum[i][index] = Sum[i][index] + branch.Value
		
def FindNode(nodeName):
	for i in range(len(node_list)):
		if node_list[i] == nodeName:
			return i
	return -1
	
if __name__=="__main__":
	main()