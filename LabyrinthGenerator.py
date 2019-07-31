from LabyrinthUtility import *
import random
import numpy as np

def depthFirst(labyrinth, startx, starty):
	"""Creates a maze with recursive depth-first search algorithm"""
	visited_cells = set()
	def inner(x,y):
		visited_cells.add((x,y))
		neighbors = list(labyrinth.array[x,y].neighbors)
		random.shuffle(neighbors)
		for n in neighbors:
			if not n in visited_cells:
				labyrinth.array[x,y].removeWall(labyrinth.array[n[0],n[1]])
				inner(n[0],n[1])
	inner(startx,starty)

def depthFirstNoRec(labyrinth,startx,starty):
	"""Creates a maze with nonrecursive depth-first search algorithm"""
	visited_cells = set()
	stack = [(startx,starty)]
	visited_cells.add((startx,starty))
	neighbors = list(labyrinth.array[startx,starty].neighbors)
	random.shuffle(neighbors)
	datastack = [neighbors]
	while len(stack) > 0:
		current = stack[-1]
		nextcell = (-1,-1)
		if len(datastack[-1]) > 0:
			nextcell = datastack[-1].pop()
			if not nextcell in visited_cells:
				stack.append(nextcell)
				newneighbors = list(labyrinth.array[nextcell[0],nextcell[1]].neighbors)
				random.shuffle(newneighbors)
				datastack.append(newneighbors)
				labyrinth.array[current[0],current[1]].removeWall(labyrinth.array[nextcell[0],nextcell[1]])
				visited_cells.add(nextcell)
		else:
			datastack.pop()
			stack.pop()

def braid(labyrinth):
	"""Tries to create a braid maze"""
	for x in range(labyrinth.xsize):
		for y in range(labyrinth.ysize):
			cell = labyrinth.array[x,y]
			openneighbors = {n for n in labyrinth.array[x,y].neighbors if cell.hasPath(labyrinth.array[n[0],n[1]])}
			neighbors = list(labyrinth.array[x,y].neighbors)
			closedneighbors = list(labyrinth.array[x,y].neighbors - openneighbors)
			random.shuffle(closedneighbors)
			numOfNeighbors = 1#max(random.randint(0,len(neighbors)),2)
			amount = max(0,numOfNeighbors-len(openneighbors))
			for i in range(amount):
				labyrinth.array[x,y].removeWall(labyrinth.array[closedneighbors[i][0],closedneighbors[i][1]])

			
def kruskal(labyrinth):
	"""Creates a mze with thee kruskal algorithm"""
	xsize,ysize = labyrinth.xsize, labyrinth.ysize
	numOfConnections = (xsize - 1)*ysize + (ysize - 1)*xsize
	weights = [(i,random.random()) for i in range(numOfConnections)]
	weights.sort(key = lambda k: k[1])
	setLib = dict()#replace
	for x in range(xsize):
		for y in range(ysize):
				setLib[(x,y)] = set((x,y))#replace
	for (c, w) in weights:
		#The numbering logic concerning the connections is the following: First the horizontal connections from
		#the top left to bottom right, row by row, and then the vertical connections from top left to bottom right, column by column
		if(c < (xsize - 1)*ysize):
			x1 = c%(xsize - 1)
			x2 = x1 + 1
			y1 = c//(xsize - 1)
			y2 = y1
		else:
			k = c - (xsize - 1)*ysize
			y1 = k%(ysize - 1)
			y2 = y1 + 1
			x1 = k//(ysize - 1)
			x2 = x1
		labyrinth.array[x1,y1].removeWall(labyrinth.array[x2,y2])
		###TODO: Code a disjoint-set data structure