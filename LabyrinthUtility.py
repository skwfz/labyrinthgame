import numpy as np


class Cell:
	def __init__(self,x,y,maxx,maxy):
		self.pathRight = False
		self.pathLeft = False
		self.pathUp = False
		self.pathDown = False
		self.x = x
		self.y = y
		self.neighbors = set()
		if x > 0:
			self.neighbors.add((x-1,y))
		if x < maxx-1:
			self.neighbors.add((x+1,y))
		if y > 0:
			self.neighbors.add((x,y-1))
		if y < maxy-1:
			self.neighbors.add((x,y+1))
	def removeWall(self,dest):
		if (dest.x,dest.y) in self.neighbors:
			if dest.x == self.x + 1:
				self.pathRight = True
				dest.pathLeft = True
			elif dest.x == self.x - 1:
				self.pathLeft = True
				dest.pathRight = True
			elif dest.y == self.y + 1:
				self.pathDown = True
				dest.pathUp = True
			elif dest.y == self.y - 1:
				self.pathUp = True
				dest.pathDown = True
	def hasPath(self,dest):
		if (dest.x,dest.y) in self.neighbors:
			if dest.x == self.x + 1 and self.pathRight:
				return True
			elif dest.x == self.x - 1 and self.pathLeft:
				return True
			elif dest.y == self.y + 1 and self.pathDown:
				return True
			elif dest.y == self.y - 1 and self.pathUp:
				return True
			else:
				return False
		else:
			return False
	def createWall(self,dest):
		if (dest.x,dest.y) in self.neighbors:
			if dest.x == self.x + 1:
				self.pathRight = False
				dest.pathLeft = False
			elif dest.x == self.x - 1:
				self.pathLeft = False
				dest.pathRight = False
			elif dest.y == self.y + 1:
				self.pathDown = False
				dest.pathUp = False
			elif dest.y == self.y - 1:
				self.pathUp = False
				dest.pathDown = False
	
			
class Labyrinth:
	def __init__(self,xsize,ysize):
		self.xsize = xsize
		self.ysize = ysize
		self.array = np.empty((xsize,ysize),dtype=Cell)
		self.characters = []
		for x in range(xsize):
			for y in range(ysize):
				self.array[x,y] = Cell(x,y,xsize,ysize)


class Character:
	def __init__(self,labyrinth,x,y):
		self.x = x
		self.y = y
		self.labyrinth = labyrinth
	def moveRight(self):
		if self.labyrinth.array[self.x,self.y].pathRight:
			self.x = self.x + 1
	def moveLeft(self):
		if self.labyrinth.array[self.x,self.y].pathLeft:
			self.x = self.x - 1
	def moveUp(self):
		if self.labyrinth.array[self.x,self.y].pathUp:
			self.y = self.y - 1
	def moveDown(self):
		if self.labyrinth.array[self.x,self.y].pathDown:
			self.y = self.y + 1

class Player(Character):
	pass
