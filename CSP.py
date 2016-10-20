import sys

class Sudoku:
	grid = []
	numRemainingSquares = 81

	def __init__(self, filename):
		with open(filename, 'r') as f:			
			for line in f:
				row = []
				for c in line:
					tempdict = {}
					tempdict['text'] = c
					tempdict['domain'] = []
					row.append(tempdict)
				self.grid.append(row)
				
	def printGrid(self):
		for i in range(len(self.grid)):
			line = ""
			for j in range(len(self.grid)):
				line += self.grid[i][j]['text']
			print(line)

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

	def updateDomain(self):
		#iterate through grid
		for i in range(len(self.grid)):
			for j in range(len(self.grid)):
				#check empty squares
				if self.grid[i][j]['text'] == '-':
					#empty domain list
					del self.grid[i][j]['domain'][:]
					#test domain values, add to domain list
					for testDomainVal in range(1,10):
						testDomainVal = str(testDomainVal)
						if self.checkHorizontal(i,j,testDomainVal) and \
						self.checkVertical(i,j,testDomainVal) and \
						self.checkGroup(i,j,testDomainVal):
							self.grid[i][j]['domain'].append(testDomainVal)

	def recursiveBacktrackSolve(self):
		print("recurssiveBacktrackSolve skeleton call")
	
	def getNextVariable(self):
		print("getNextVariable skeleton call")


def main(argc, argv):
	filename = argv[1]
	#basic input validation
	if argc != 2:
		sys.exit()
	sudoku = Sudoku(filename)
	sudoku.updateDomain()
	sudoku.printGrid()
	print(sudoku.grid[1][7]['domain'])


	#sudoku = recursiveBacktrackSolve()
	#sudoku.printGrid()

if __name__ == '__main__':
	main(len(sys.argv), sys.argv)