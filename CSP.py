import sys

class Sudoku:
	board = []
	numRemainingSquares = 81

	def __init__(self, filename):
		with open(filename, 'r') as f:			
			for line in f:
				row = []
				for c in line:
					tempdict = {}
					tempdict['text'] = c
					tempdict['availableMoves'] = {}
					row.append(tempdict)
				self.board.append(row)
				
	def printGrid(self):
		for i in range(len(self.board)):
			line = ""
			for j in range(len(self.board)):
				line += self.board[i][j]['text']
			print(line)

	def checkVertical(self, row, col, val):

	def checkHorizontal(self, row, col, val):

	def checkGroup(self, row, col, val):


def main(argc, argv):
	filename = argv[1]
	#basic input validation
	if argc != 2:
		sys.exit()
	sudoku = Sudoku(filename)
	sudoku.printGrid()


if __name__ == '__main__':
	main(len(sys.argv), sys.argv)