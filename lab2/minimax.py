# Author: Jinjin Shao
# Oct. 14, 2015
# Run this code, just type: python minimax.py in terminal
# This code shows the minimax values of the first move of X in tic-tac-toe game. 
# And the optimal play of two players. 

import sys

class State:
	def __init__(self, inputStr, player):
		self.state = inputStr
		self.player = player

	def terminal_test(self):
		result = False
		for x in xrange(3):
			if self.state[x] == self.state[x + 3] == self.state[x + 6]:
				if not self.state[x] == ".":
					result = True

			if self.state[x*3] == self.state[x*3 + 1] == self.state[x*3 + 2]:
				if not self.state[x*3] == ".":
					result = True

		if self.state[0] == self.state[4] == self.state[8]:
			if not self.state[0] == ".":
				result = True

		if self.state[2] == self.state[4] == self.state[6]:
			if not self.state[2] == ".":
				result = True

		blank = '.'
		if not blank in self.state:
			result = True

		return result

	def evalUtility(self):
		utility = 0

		for x in xrange(3):
			if self.state[x] == self.state[x + 3] == self.state[x + 6]:
				if self.state[x] == 'o':
					utility = -10
				else:
					utility = 10

				break;

			if self.state[x*3] == self.state[x*3 + 1] == self.state[x*3 + 2]:
				if self.state[x*3] == 'o':
					utility = -10
				else:
					utility = 10

				break;

		if utility == 0:
			if self.state[0] == self.state[4] == self.state[8] or self.state[2] == self.state[4] == self.state[6]:
				if self.state[4] == 'o':
					utility = -10
				else:
					utility = 10

		return utility

	def resultState(self, action):
		a = str()
		nextPlayer = str()
		if self.player == "X":
			nextPlayer = "O"
			a = "x"
		else:
			nextPlayer = "X"
			a = "o"

		index = action[0] * 3 + action[1]
		tempStr = self.state[0:index] + a + self.state[(index+1):len(self.state)]
		newState = State(tempStr, nextPlayer)

		return newState

	def printState(self):
		temp = str(self.state)
		temp = temp.replace("o", "O")
		temp = temp.replace("x", "X")
		temp = temp.replace(".", "!")

		for x in xrange(3):
			print temp[x*3] + " " + temp[x*3 + 1] + " " + temp[x*3 + 2]

		print "\n"

def min_value(current_state):
	if current_state.terminal_test():
		return current_state.evalUtility()

	mValue = 20
	for i in xrange(3):
		for j in xrange(3):
			if current_state.state[i*3 + j] == ".":
				temp = max_value(current_state.resultState(list([i, j])))
				if temp < mValue:
					mValue = temp

	return mValue

def max_value(current_state):
	if current_state.terminal_test():
		return current_state.evalUtility()

	mValue = -20
	for i in xrange(3):
		for j in xrange(3):
			if current_state.state[i*3 + j] == ".":
				temp = min_value(current_state.resultState(list([i, j])))
				if temp > mValue:
					mValue = temp

	return mValue

# Take a state and evaluate all possible actions according to the final utility value
# Return a action based on the input state.
def minimax_decision(current_state):
	selectedAction = [-1, -1]

	if current_state.player == "X":
		mValue = -20
		for i in xrange(3):
			for j in xrange(3):
				if current_state.state[i*3 + j] == ".":
					temp = min_value(current_state.resultState(list([i, j])))
					if temp > mValue:
						selectedAction = [i, j]
						mValue = temp

	if current_state.player == "O":
		mValue = 20
		for i in xrange(3):
			for j in xrange(3):
				if current_state.state[i*3 + j] == ".":
					temp = max_value(current_state.resultState(list([i, j])))
					if temp < mValue:
						selectedAction = [i, j]
						mValue = temp

	return selectedAction

def printFirstMinimaxValue(current_state):
	if current_state.player == "X":
		for i in xrange(3):
			for j in xrange(3):
				temp = min_value(current_state.resultState(list([i, j])))
				sys.stdout.write(str(temp) + ' ')

			print ""

	if current_state.player == "O":
		for i in xrange(3):
			for j in xrange(3):
				temp = max_value(current_state.resultState(list([i, j])))
				sys.stdout.write(str(temp) + ' ')

			print ""

	print "\n"

def main(argv):
	initialState = State(".........", "X")

	print "\n------- minimax values for the first move -------"
	printFirstMinimaxValue(initialState)


	#Evaluate the optimal action for each state
	nextState = initialState
	print "\n------------------- Optimal Play -------------------"
	while not nextState.terminal_test():
		action = minimax_decision(nextState)

		newState = nextState.resultState(action)
		newState.printState()

		nextState = newState

if __name__ == "__main__":
	main(sys.argv)
