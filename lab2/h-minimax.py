# Author: Jinjin Shao
# Oct. 14, 2015
# Run this code, just type: python h-minimax.py in terminal
# This code shows the h-minimax values of the first move of X in tic-tac-toe game. 
# And the optimal play of two players. 
# cutoff here is set to 4. 

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

	def eval(self):
		twoX, oneX, twoO, oneO = 0, 0, 0, 0

		possibleLine = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

		for line in possibleLine:
			countX = 0
			countO = 0

			for index in line:
				if self.state[index] == 'o':
					countO += 1
				
				if self.state[index] == 'x':
					countX += 1

			if countO == 0:
				if countX == 1:
					oneX += 1
				if countX == 2:
					twoX += 1

			if countX == 0:
				if countO == 1:
					oneO += 1
				if countO == 2:
					twoO += 1

		result = 3 * twoX + oneX - (3 * twoO + oneO)

		return result

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

def h_min_value(current_state, depth, cutoff):
	if current_state.terminal_test():
		return current_state.evalUtility()

	if depth == cutoff:
		return current_state.eval()

	mValue = 20
	for i in xrange(3):
		for j in xrange(3):
			if current_state.state[i*3 + j] == ".":
				temp = h_max_value(current_state.resultState(list([i, j])), depth + 1, cutoff)
				if temp < mValue:
					mValue = temp

	return mValue

def h_max_value(current_state, depth, cutoff):
	if current_state.terminal_test():
		return current_state.evalUtility()

	if depth == cutoff:
		return current_state.eval()

	mValue = -20
	for i in xrange(3):
		for j in xrange(3):
			if current_state.state[i*3 + j] == ".":
				temp = h_min_value(current_state.resultState(list([i, j])), depth + 1, cutoff)
				if temp > mValue:
					mValue = temp

	return mValue

def h_minimax_decision(current_state, cutoff):
	selectedAction = [-1, -1]

	if current_state.player == "X":
		mValue = -20
		for i in xrange(3):
			for j in xrange(3):
				if current_state.state[i*3 + j] == ".":
					temp = h_min_value(current_state.resultState(list([i, j])), 1, cutoff)
					if temp > mValue:
						selectedAction = [i, j]
						mValue = temp

	if current_state.player == "O":
		mValue = 20
		for i in xrange(3):
			for j in xrange(3):
				if current_state.state[i*3 + j] == ".":
					temp = h_max_value(current_state.resultState(list([i, j])), 1, cutoff)
					if temp < mValue:
						selectedAction = [i, j]
						mValue = temp

	return selectedAction

# Take a state and a cutoff value. 
# Evaluate all possible actions according to the final utility value or cutoff value. 
# Return a action based on the input state.
def h_minimax(current_state, cutoff):
	nextState = current_state

	if cutoff < 1:
		print "Invalid cutoff: the value of accept cutoff should be positive "
		sys.exit(0)

	while not nextState.terminal_test():
		action = h_minimax_decision(nextState, cutoff)

		newState = nextState.resultState(action)
		newState.printState()

		nextState = newState

def printFirstMinimaxValue(current_state, cutoff):
	if current_state.player == "X":
		for i in xrange(3):
			for j in xrange(3):
				temp = h_min_value(current_state.resultState(list([i, j])), 1, cutoff)
				sys.stdout.write(str(temp) + ' ')

			print ""

	if current_state.player == "O":
		for i in xrange(3):
			for j in xrange(3):
				temp = h_max_value(current_state.resultState(list([i, j])), 1, cutoff)
				sys.stdout.write(str(temp) + ' ')

			print ""

	print "\n"

def main(argv):
	initialState = State(".........", "X")
	cutoff = 4

	print "\n------- h-minimax values for the first move -------"
	printFirstMinimaxValue(initialState, cutoff)

	print "\n------------------- Optimal Play -------------------"
	h_minimax(initialState, cutoff)

if __name__ == "__main__":
	main(sys.argv)
