import pygame
from pygame.locals import *
from numpy import loadtxt
import time
import random 

#Constants for the game
WIDTH, HEIGHT = (32, 32)
WALL_COLOR = pygame.Color(0, 191, 255, 255) # SKYBLUE
PACMAN_COLOR = pygame.Color(255, 255, 0, 255) #YELLOW
COIN_COLOR = pygame.Color(255, 255, 255, 255) #WHITE
DOWN = (0,1)
RIGHT = (1,0)
TOP = (0,-1)
LEFT = (-1,0)
move_direction= (0,0)
list_of_visited_pos=[]
strt=0



#Draws a rectangle for the wall
def draw_wall(screen, pos):
	pixels = pixels_from_points(pos)
	pygame.draw.rect(screen, WALL_COLOR, [pixels, (WIDTH, HEIGHT)])

#Draws a rectangle for the player
def draw_pacman(screen, pos): 
	pixels = pixels_from_points(pos)
	circo=(pixels[0]+16,pixels[1]+16)
	pygame.draw.circle(screen,PACMAN_COLOR,circo,20) #Making pacman larger 

#Draws a rectangle for the coin
def draw_coin(screen, pos):
	pixels = pixels_from_points(pos)
	circo=(pixels[0]+16,pixels[1]+16)
	pygame.draw.circle(screen,COIN_COLOR,circo,8) #Making coin size smaller


#Uitlity functions
def add_to_pos(pos, pos2):
	return (pos[0]+pos2[0] , pos[1]+pos2[1])

def pixels_from_points(pos):
	return (pos[0]*WIDTH, pos[1]*HEIGHT)


#Initializing pygame
pygame.init()
screen = pygame.display.set_mode((640,640), 0, 32)
background = pygame.surface.Surface((640,640)).convert()


#Initializing variables
layout = loadtxt('layout.txt', dtype=str)
rows, cols = layout.shape
pacman_position = (1,1)
background.fill((0,0,0))
list_of_visited_pos.append(pacman_position)

# Main game loop 
while True:
	score=0
	strt+=0.2 #This counts the number of cycles the game has gone through 
	sec = strt % 60
	minu = strt // 60
	minu = minu % 60
	hours = strt // 3600
	hours = hours % 60
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				move_direction = LEFT
			if event.key == K_RIGHT:
				move_direction = RIGHT
			if event.key == K_UP:
				move_direction = TOP
			if event.key == K_DOWN:
				move_direction = DOWN


	screen.blit(background, (0,0))

	#Draw board from the 2d layout array.
  #In the board, '.' denote the empty space, 'w' are the walls, 'c' are the coinsvalue = layout[row][col]
	#If c is present in list of visited places then it shouldnot be colored like a coin. 
	for col in range(cols):
		for row in range(rows):
			value = layout[row][col]
			pos = (col, row)
			if value == 'w':
				draw_wall(screen, pos)
			elif value == 'c':
				if pos not in list_of_visited_pos:
					draw_coin(screen, pos)
				else:
					score+=1

	#Draw the player
	draw_pacman(screen, pacman_position)

	

	#Update player position based on movement.
	row=add_to_pos(pacman_position, move_direction)[1]
	col=add_to_pos(pacman_position, move_direction)[0]
	value = layout[row][col]
	if value== 'w':
		pacman_position = pacman_position
	else:
		pacman_position = add_to_pos(pacman_position, move_direction)
	count_coins = 0
	list_of_visited_pos.append(pacman_position)

	
	font = pygame.font.SysFont(None, 33)
	message	= font.render("Time: " + str(int(hours//1)) + ':' + str(int(minu//1)) + ':' + str(int(sec//1)), True, (0,0,0))
	screen.blit(message, (320,0))
	message	= font.render("score: " + str(score), True, (0,0,0))
	screen.blit(message, (0,0))

	#TODO: Check if player ate any coin, or collided with the wall by using the layout array.
	# player should stop when colliding with a wall
	# coin should dissapear when eating, i.e update the layout array

	#Update the display
	pygame.display.update()

	#Wait for a while, computers are very fast.
	time.sleep(0.2) 
