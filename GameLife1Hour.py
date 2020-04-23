#!/usr/bin/env python

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import sys, pygame
import numpy as np
import time


def render(fnt, what, color, where):
    "Renders the fonts as passed from display_fps"
    text_to_show = fnt.render(what, 0, pygame.Color(color))
    screen.blit(text_to_show, where)

pygame.init()
pygame.display.set_caption('Game of Life')
clock = pygame.time.Clock()

size = width, height = 820, 620
border = 10
speed = [2, 2]
BLACK = 0, 0, 0
WHITE = 255, 255, 255

nXc = 200
nYc = 150

cell_w = int( (width - 2*border) / nXc );
cell_h = int( (height - 2*border) / nYc );

screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("Arial", 14)

#state = np.zeros( (nXc,nYc) )
state = np.random.randint(0, 2, (nXc,nYc) )

c = 0
run = True
while 1:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_TAB or event.key == pygame.K_ESCAPE :
				state = np.zeros( (nXc,nYc) )
			if event.key == pygame.K_SPACE:
				run = not run
				c = 0
		if event.type == pygame.MOUSEBUTTONDOWN :
			run = False
		if event.type == pygame.MOUSEBUTTONUP :
			pos = pygame.mouse.get_pos()
			print( pos )
			i = int(( pos[0] - border ) / cell_w)
			j = int(( pos[1] - border ) / cell_h)
			
			if state[i][j] == 0 :
				state[i][j] = 1
			else :
				state[i][j] = 0
			
	screen.fill(BLACK)

	if run :
		newstate = np.zeros( (nXc,nYc) )
		for i in range(0, nXc) :
			for j in range(0, nYc ):
				sum = state[(i-1)%nXc][(j-1)%nYc] + state[(i)%nXc][(j-1)%nYc] + state[(i+1)%nXc][(j-1)%nYc] + 	\
						state[(i-1)%nXc][(j)%nYc] + state[(i+1)%nXc][(j)%nYc] + 					\
						state[(i-1)%nXc][(j+1)%nYc] + state[(i)%nXc][(j+1)%nYc] + state[(i+1)%nXc][(j+1)%nYc]
				if sum == 3 and state[i][j] == 0:
					newstate[i][j] = 1
				elif (sum == 2 or sum == 3) and state[i][j] == 1 :
					newstate[i][j] = 1
				else :
					newstate[i][j] = 0
		state = newstate
		
	for i in range(0, nXc) :
		for j in range(0, nYc ):
			s = 0
			#if state[i,j] == 0 : s = 1
			if state[i,j] == 1 : pygame.draw.rect( screen, WHITE, ( i*cell_w + border, j*cell_h + border, cell_w, cell_h ), s )

	pygame.image.save(screen, "screenshots/%s.jpg" % str(c).zfill(4))
	c = c + 1

	render(font, str(int(clock.get_fps())), "white", (0, 0))
	#time.sleep(0.05)
	clock.tick(60)
	pygame.display.flip()

 
