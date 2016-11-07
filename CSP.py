import sys

class Sudoku:
	grid = []
	numRemainingSquares = 0

	def __init__(self, filename):
		with open(filename, 'r') as f:			
			for line in f:
				row = []
				for c in line:
					if c !='\n':
						tempdict = {}
						tempdict['text'] = c
						tempdict['domain'] = []
						row.append(tempdict)
						if c == '-':
							self.numRemainingSquares += 1
				self.grid.append(row)

	def isComplete(self):
		return self.numRemainingSquares == 0

	def printGrid(self):
		printstr = ""
		for i in range(len(self.grid)):
			for j in range(len(self.grid)):
				printstr += self.grid[i][j]['text']
			if i != len(self.grid) - 1:
				printstr += '\n'
		print(printstr)

	def checkCol(self, row, col, val):
		isValid = True
		#start at top, look down
		for i in range(len(self.grid)):
			if self.grid[i][col]['text'] == val:
				isValid = False
		return isValid		

	def checkRow(self, row, col, val):
		isValid = True
		#start at left, look right
		for i in range(len(self.grid)):
			if self.grid[row][i]['text'] == val:
				isValid = False
		return isValid

	def checkGroup(self, row, col, val):
		#start looking in top left position of group, iterate
		startRow = row - row % 3
		startCol = col - col % 3
		isValid = True
		for i in range(startRow, startRow + 3):
			for j in range(startCol, startCol + 3):
				if self.grid[i][j]['text'] == val:
					isValid = False
		return isValid

		#a bit more efficient
	def updateDomainAdd(self, row, col, val):
		#clear domain for variable
		del self.grid[row][col]['domain'][:]
		#row
		for i in range(len(self.grid)):
			if val in self.grid[row][i]['domain']:
				self.grid[row][i]['domain'].remove(val)
		#col
		for i in range(len(self.grid)):
			if val in self.grid[i][col]['domain']:
				self.grid[i][col]['domain'].remove(val)
		#group
		startRow = row - row % 3
		startCol = col - col % 3
		for i in range(startRow, startRow + 3):
			for j in range(startCol, startCol + 3):
				if val in self.grid[i][j]['domain']:
					self.grid[i][j]['domain'].remove(val)
												 
	def updateDomain(self):
		#iterate through grid
		for i in range(len(self.grid)):
			for j in range(len(self.grid)):
				del self.grid[i][j]['domain'][:]	
				if self.grid[i][j]['text'] == '-':
						#empty domain list
						#test domain values, add to domain list
						for testDomainVal in range(1,10):
							testDomainVal = str(testDomainVal)
							if self.checkRow(i,j,testDomainVal) and \
								self.checkCol(i,j,testDomainVal) and \
								self.checkGroup(i,j,testDomainVal):
									self.grid[i][j]['domain'].append(testDomainVal)
				
	def getNextVar(self):
		#select variable with smallest nonempty domain
		minDomainLen = float('inf')
		minDomainRow = 0
		minDomainCol = 0
		for i in range(len(self.grid)):
			for j in range(len(self.grid)):
				testDomainLen = len(self.grid[i][j]['domain']) 
				if testDomainLen != 0 and testDomainLen < minDomainLen:
					minDomainLen = testDomainLen
					minDomainRow = i
					minDomainCol = j
		return minDomainRow, minDomainCol

	def recursiveBacktrackSolve(self):
		#base case
		if self.isComplete():
			return True
		#select unsolved variable with smallest domain
		row, col = self.getNextVar()
		domain = list(self.grid[row][col]['domain'])
		#try each value in variable's domain
		for val in domain:
			self.grid[row][col]['text'] = val
			self.updateDomainAdd(row, col, val)
			self.numRemainingSquares -= 1
			result = self.recursiveBacktrackSolve()
			if result:
				return result
			#remove value after reaching a dead end from this assignment
			self.grid[row][col]['text'] = '-'
			self.updateDomain()
			self.numRemainingSquares += 1
		#dead end
		return False

def main(argc, argv):
	filename = argv[1]
	#basic input validation
	if argc != 2:
		sys.exit()
	sudoku = Sudoku(filename)
	sudoku.updateDomain()
	result = sudoku.recursiveBacktrackSolve()
	if result:
		sudoku.printGrid()
	else:
		print("unsolvable puzzle")

if __name__ == '__main__':
	main(len(sys.argv), sys.argv)