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
	def checkVertical(self, row, col, val):
		isValid = True
		#start at top, look down
		for i in range(len(self.grid)):
			if self.grid[i][col]['text'] == val:
				isValid = False
		return isValid		

	def checkHorizontal(self, row, col, val):
		isValid = True
		#start at left, look right
		for i in range(len(self.grid)):
			if self.grid[row][i]['text'] == val:
				isValid = False
		return isValid

	def checkGroup(self, row, col, val):
		#start looking in top left position of group
		startRow = row - row % 3
		startCol = col - col % 3
		isValid = True
		#iterate through group
		for i in range(startRow, startRow + 3):
			for j in range(startCol, startCol + 3):
				if self.grid[i][j]['text'] == val:
					isValid = False
		return isValid

	def debug(self):
		for i in range(len(self.grid)):
			print(self.grid[i])

	def updateDomain(self):
		#iterate through grid
		for i in range(len(self.grid)):
			for j in range(len(self.grid)):
				#reset domain
				del self.grid[i][j]['domain'][:]	
				if self.grid[i][j]['text'] == '-':
					#empty domain list
					#test domain values, add to domain list
					for testDomainVal in range(1,10):
						testDomainVal = str(testDomainVal)
						if self.checkHorizontal(i,j,testDomainVal) and \
						self.checkVertical(i,j,testDomainVal) and \
						self.checkGroup(i,j,testDomainVal):
							self.grid[i][j]['domain'].append(testDomainVal)
	def selectUnassignedVar(self):
		#select smallest nonempty domain
		#if none exists, return error
		minDomainLen = float('inf')
		minDomainRow = 0
		minDomainCol = 0
		for i in range(len(self.grid)):
			for j in range(len(self.grid)):
				testDomainLen = len(self.grid[i][j]['domain']) 
				#is tie an issue?
				if testDomainLen != 0 and testDomainLen < minDomainLen:
					minDomain = testDomainLen
					minDomainRow = i
					minDomainCol = j
		return minDomainRow, minDomainCol

	def recursiveBacktrackSolve(self):
		if self.isComplete():
			return True
		row, col = self.selectUnassignedVar()
		domain = list(self.grid[row][col]['domain'])
		for val in domain:
			# print("adding %s to %d %d" % (val, row, col))
			self.grid[row][col]['text'] = val
			self.updateDomain()
			self.numRemainingSquares -= 1
			result = self.recursiveBacktrackSolve()
			if result:
				return True
			#remove value after reaching a dead end from this assignment
			# print("removing %s to %d %d" % (val, row, col))
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
	# sudoku.printGrid()
	sudoku.updateDomain()
	result = sudoku.recursiveBacktrackSolve()
	if result:
		sudoku.printGrid()
	else:
		print("unsolvable puzzle")

if __name__ == '__main__':
	main(len(sys.argv), sys.argv)