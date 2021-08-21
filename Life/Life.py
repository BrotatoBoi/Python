from random import choices
from os import system
from time import sleep


class Cell:
	def __init__(self, x, y, state):
		self.pos = (x, y)
		self.state = int(''.join(state))
		self.color = None

	def check_neighbours(self, board):
		if self.pos[0] != 0 and self.pos[1] != 0:
			yield board[self.pos[0]-1][self.pos[1]-1]
		if self.pos[0] != len(board[self.pos[0]])-1 and self.pos[1] != 0:
			yield board[self.pos[0]+1][self.pos[1]-1]
		if self.pos[0] != 0 and self.pos[1] != len(board)-1:
			yield board[self.pos[0]-1][self.pos[1]+1]
		if self.pos[0] != len(board[self.pos[0]])-1 and self.pos[1] != len(board)-1:
			yield board[self.pos[0]+1][self.pos[1]+1]
		if self.pos[1] != 0:
			yield board[self.pos[0]][self.pos[1]-1]
		if self.pos[0] != 0:
			yield board[self.pos[0]-1][self.pos[1]]
		if self.pos[0] != len(board[self.pos[0]])-1:
			yield board[self.pos[0]+1][self.pos[1]]
		if self.pos[1] != len(board)-1:
			yield board[self.pos[0]][self.pos[1]+1]

	def update(self, board):
		alive = 0

		for cell in self.check_neighbours(board):
			if cell.state:
				alive += 1

		if self.state:
			if alive == 2 or alive == 3:
				self.state = 1
			else:
				self.state = 0
		else:
			if alive == 3:
				self.state = 1

		if self.state:
			self.color = '\033[0;35;45m'
		else:
			self.color = '\033[0;34;44m'

class Main:
	def __init__(self):
		self.board = [[Cell(x, y, choices(["0", "1"], [65, 35])) for x in range(50)] for y in range(50)]

		self._isRunning = True

		self.execute()

	def show_cells(self):
		for row in self.board:
			for cell in row:
				print(f"{cell.color}{cell.state}", end=' ')

			print("\033[0;0m")

	def update_cells(self):
		for row in self.board:
			for cell in row:
				cell.update(self.board)

	def execute(self):
		while self._isRunning:
			system('clear')

			self.show_cells()
			self.update_cells()

			sleep(0.5)


if __name__ == '__main__':
	Main()
