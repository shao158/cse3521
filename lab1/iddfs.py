# Author: Jinjin Shao
# Sep. 22, 2015
# Run this code, python iddfs.py
# This code solves 8-puzzle problem using IDDFS search algorithm

import sys
import Queue as Q

# a class defined for state
class Puzzle:
	def __init__(self, numList):
        #Check if the input is valid to create a state
		if not (len(numList) == 9 and set(numList) == set([0, 1, 2, 3, 4, 5, 6, 7, 8])):
			print "Please input a list containing exactly 0~9 into puzzle! \n"
			sys.exit()

		else:
			self.nums = numList

    # Check if the action is valid for the current state
	def actionValid(self, action):
		p = self.positionOf(0)
		if action == 'up' and p[0] == 1:
			return False
		if action == 'down' and p[0] == 3:
			return False
		if action == 'left' and p[1] == 1:
			return False
	 	if action == 'right' and p[1] == 3:
	 		return False

	 	return True

    # Execute the action to the state
	def executeAction(self, action):
		newState = Puzzle(list(self.nums))

		if action == 'up':
			newState.moveUp()
		elif action == 'down':
			newState.moveDown()
		elif action == 'left':
			newState.moveLeft()
		elif action == 'right':
			newState.moveRight()

		return newState

    # Four actions 
	def moveUp(self):
		index0 = self.nums.index(0)
		index1 = index0 - 3

		self.nums[index0] = self.nums[index1]
		self.nums[index1] = 0

	def moveDown(self):
		index0 = self.nums.index(0)
		index1 = index0 + 3

		self.nums[index0] = self.nums[index1]
		self.nums[index1] = 0

	def moveLeft(self):
		index0 = self.nums.index(0)
		index1 = index0 - 1

		self.nums[index0] = self.nums[index1]
		self.nums[index1] = 0

	def moveRight(self):
		index0 = self.nums.index(0)
		index1 = index0 + 1

		self.nums[index0] = self.nums[index1]
		self.nums[index1] = 0

    # function to print state
	def printState(self):
		print self.nums

    # function help find the location of a number in Puzzle
	def positionOf(self, num):
		numIndex = self.nums.index(num)
		row = numIndex / 3 + 1
		column = numIndex % 3 + 1

		position = [row, column]

		return position


# This class is defined for each node, which including state, parent node, the action executed to create this node, 
# the path cost to this node, the depth of this node, and how far to go until goal state.
class MyNode:
	def __init__(self, state, parentNode, action, pathCost, depth, cost2go):
		self.state = state
		self.parent = parentNode
		self.action = action
		self.pathCost = pathCost
		self.depth = depth
		self.costToGo = cost2go

    # Define the priority of node. 
	def __cmp__(self, other):
		if cmp(other.state.nums, self.state.nums) == 0:
			return 0

		if cmp(other.depth, self.depth) >= 0:
			return -1
		else:
			return 1

# function help to calculate how far from the current state to goal state
def costToGo(goal, s):
	totalCost = 0

	for n in range(0, 9):
		totalCost += abs(goal.positionOf(n)[0] - s.positionOf(n)[0])
		totalCost += abs(goal.positionOf(n)[1] - s.positionOf(n)[1])

	return totalCost

# function help to create child node from current node and action 
def childNode(node, action, goal):
	child = None
	currentState = node.state

	if currentState.actionValid(action):
		newState = currentState.executeAction(action)
		child = MyNode(newState, node, action, node.pathCost + 1, node.depth + 1, costToGo(goal, newState))
	
	return child


# Check goal state
def goalCheck(s):
	return cmp(s.nums, goalState.nums) == 0

# Function to print out solution from the current node 
def solution(node):
	sequenceNode = list()

	temp = node
	while(temp):
		sequenceNode.insert(0, temp)
		temp = temp.parent

	count = 0
	for item in sequenceNode:
		a = item.action
		numList = item.state.nums
		if not a: 
			a = "None"
		print "Step " + str(count) + ": " + a
		print str(numList[0]) + " " + str(numList[1]) + " " + str(numList[2])
		print str(numList[3]) + " " + str(numList[4]) + " " + str(numList[5])
		print str(numList[6]) + " " + str(numList[7]) + " " + str(numList[8])

		count = count + 1


# define initial State, actions, and goalState here
initialState = Puzzle([0, 8, 5, 4, 2, 7, 6, 3, 1])
actions = ['up', 'down', 'left', 'right']
goalState = Puzzle([0, 1, 2, 3, 4, 5, 6, 7, 8])

# depth-limit-search
def dls(initialState, goalState, cutoff):
	explored = Q.PriorityQueue()
	frontier = Q.PriorityQueue()
	initialNode = MyNode(initialState, None, None, 0, 0, costToGo(goalState, initialState))

	if goalCheck(initialState):
		return [initialState]

	if cutoff == 0:
		return None

	frontier.put(initialNode)

	while not frontier.empty():
		temp = frontier.get()
			
		if temp not in explored.queue:
			explored.put(temp)

		for a in actions:
			child = childNode(temp, a, goalState)

			if child and (child not in frontier.queue):
                # Sometimes, even node is explored but its depth is not optimal.
                # If encounter a node already in explored set but this time 
                # there is a smaller depth to this node, update the depth of 
                # this state in explored set. 
				f = False
				if child in explored.queue:
					for item in explored.queue:
						if child == item:
							if child.depth < item.depth:
								f = True
								item.depth = child.depth

				if (child not in explored.queue) or f:
					if child.depth <= cutoff:
						if goalCheck(child.state):
							return child
						frontier.put(child)

	return None


def main(argv):
	s = None
    # from depth 0 to depth 20
	for cut in range(0, 21):
		s = dls(initialState, goalState, cut)
		if s:
			solution(s)
			break

	if not s:
		print "Failed"

if __name__ == "__main__":
	main(sys.argv)
