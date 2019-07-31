import pygame as pg
from LabyrinthUtility import *
from LabyrinthGenerator import *

pg.init()
endGame = False
clock = pg.time.Clock()
(xsize, ysize) = (40,40)
labyrinth = Labyrinth(xsize,ysize)
scale = 20 #pixels per cell in labyrinth
screen = pg.display.set_mode((xsize*scale,ysize*scale))
wallwidth = 2

def drawLabyrinth(labyrinth):
	screen.fill((255,255,255))
	for x in range(labyrinth.xsize):
		for y in range(labyrinth.ysize):
			cell = labyrinth.array[x,y]
			if not (cell.pathLeft or cell.pathRight or cell.pathUp or cell.pathDown):
				pg.draw.rect(screen, (0,0,0), pg.Rect(x*scale,y*scale,scale,scale))
			if cell.pathLeft == False:
				pg.draw.line(screen, (0,0,0),(x*scale,y*scale),(x*scale,(y+1)*scale-1),wallwidth)
			if cell.pathRight == False:
				pg.draw.line(screen, (0,0,0),((x+1)*scale-1,y*scale),((x+1)*scale-1,(y+1)*scale-1),wallwidth)
			if cell.pathUp == False:
				pg.draw.line(screen, (0,0,0),(x*scale,y*scale),((x+1)*scale-1,y*scale),wallwidth)
			if cell.pathDown == False:
				pg.draw.line(screen, (0,0,0),(x*scale,(y+1)*scale-1),((x+1)*scale-1,(y+1)*scale-1),wallwidth)
(startx,starty) = (9,9)
visited_cells = set()
stack = [(startx,starty)]
visited_cells.add((startx,starty))
neighbors = list(labyrinth.array[startx,starty].neighbors)
random.shuffle(neighbors)
datastack = [neighbors]

while not endGame:
	for event in pg.event.get():
		if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
			endGame = True
	if len(stack) > 0:
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
	drawLabyrinth(labyrinth)
	#pg.draw.circle(screen,(255,0,0),(int(c.x*scale+scale/2),int(c.y*scale+scale/2)),int(scale/2-wallwidth))#jos jotenkin tälleen sais piirrettyä missä kohtaa "kaivaja" menee
	pg.display.flip()
	clock.tick(100)
