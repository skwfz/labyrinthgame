import pygame as pg
from LabyrinthUtility import *
from LabyrinthGenerator import *
import random as rand

pg.init()
endGame = False
clock = pg.time.Clock()
(xsize, ysize) = (100,50)
labyrinth = Labyrinth(xsize,ysize)
scale = 15 #pixels per cell in labyrinth
screen = pg.display.set_mode((xsize*scale,ysize*scale))
wallwidth = 3

depthFirstNoRec(labyrinth,rand.randint(0,xsize-1),rand.randint(0,ysize-1))

player = Player(labyrinth,0,0)
labyrinth.characters.append(player)

def drawLabyrinth(labyrinth):
	screen.fill((255,255,255))
	for x in range(labyrinth.xsize):
		for y in range(labyrinth.ysize):
			if labyrinth.array[x,y].pathLeft == False:
				pg.draw.line(screen, (0,0,0),(x*scale,y*scale),(x*scale,(y+1)*scale-1),wallwidth)
			if labyrinth.array[x,y].pathRight == False:
				pg.draw.line(screen, (0,0,0),((x+1)*scale-1,y*scale),((x+1)*scale-1,(y+1)*scale-1),wallwidth)
			if labyrinth.array[x,y].pathUp == False:
				pg.draw.line(screen, (0,0,0),(x*scale,y*scale),((x+1)*scale-1,y*scale),wallwidth)
			if labyrinth.array[x,y].pathDown == False:
				pg.draw.line(screen, (0,0,0),(x*scale,(y+1)*scale-1),((x+1)*scale-1,(y+1)*scale-1),wallwidth)
	for c in labyrinth.characters:
		pg.draw.circle(screen,(255,0,0),(int(c.x*scale+scale/2),int(c.y*scale+scale/2)),int(scale/2-wallwidth))

moveCountDown = 0
while not endGame:
	for event in pg.event.get():
		if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
			endGame = True
	pressed = pg.key.get_pressed()
	if (pressed[pg.K_UP] or pressed[pg.K_DOWN] or pressed[pg.K_LEFT] or pressed[pg.K_RIGHT]) and moveCountDown == 0:
		moveCountDown = 7
		if pressed[pg.K_UP]: player.moveUp()
		if pressed[pg.K_DOWN]: player.moveDown()
		if pressed[pg.K_LEFT]: player.moveLeft()
		if pressed[pg.K_RIGHT]: player.moveRight()
	if moveCountDown > 0:
		moveCountDown -= 1
	drawLabyrinth(labyrinth)
	pg.display.flip()
	clock.tick(60)
