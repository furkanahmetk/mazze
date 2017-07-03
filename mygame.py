import os
import random
import pygame
import sys

class Screen(object):
	
	def __init__(self, width, height):
		pygame.display.set_caption("Go exit!")	
		self.screen = pygame.display.set_mode((width, height))
		self.screen.fill((0, 0, 0))
	
class Player(object):
	
	def __init__(self, pos):
		
		self.rect=pygame.Rect(pos[0], pos[1], 8, 8,)
		
	def drawplayer(self):
		
		pygame.draw.rect(screen.screen, (255, 200, 0), me.rect)
	
	def move(self, dx, dy):
			
		if dx != 0:
			self.move_single_axix(dx,0)
			screen.screen.fill((0, 0, 0))
		if dy != 0:
			self.move_single_axix(0,dy)
			screen.screen.fill((0, 0, 0))
	def move_single_axix(self, dx, dy):
		
		self.rect.x += dx
		self.rect.y += dy
		
		for wall in walls:
			if self.rect.colliderect(wall.rect):
				if dx<0:
					self.rect.left= wall.rect.right
				if dx>0:
					self.rect.right= wall.rect.left
				if dy<0:
					self.rect.top= wall.rect.bottom
				if dy>0:
					self.rect.bottom= wall.rect.top

class Wall(object):

	def __init__(self, pos):
		
		walls.append(self)
		self.rect = pygame.Rect(pos[0], pos[1], 8, 8)
	
	def drawwall(self):
		
		for wall in walls:
			pygame.draw.rect(screen.screen, (255, 255, 255), wall.rect)		

class Exit(object):
	
	def __init__(self, pos):
		self.rect = pygame.Rect(pos[0], pos[1], 8, 8)
	
	def drawexit(self):
		pygame.draw.rect(screen.screen, (255, 0, 0), exit)

os.environ["SDL_VIDEO_CENTERED"]= "1"
pygame.init()


speed = pygame.time.Clock()
walls = []

screen = Screen(160, 160)
level=[
"WWWWWWWWWWWWWWWWWWWW",
"W       WWW        W",
"W P                W",
"W   WWWWW WWWWWWW WW",
"W  WW     W     W WW",
"W  W  WWW W WWW W WW",
"W WW WW   W W W   WW",
"W  W W    W W W W WW",
"W       W W W W W  W",
"W  W W  W   W W WWWW",
"W  W   WW WWW W    W",
"W WWW WWW W W WWWW W",
"W W   W   W W    W W",
"W W W W WWW WWWW   W",
"W W W   W   W   WWWW",
"W     W W W W W    W",
"W WWWW    W W W WW W",
"W W    WW WWW W W  W",
"W   WWWW      W W EW",
"WWWWWWWWWWWWWWWWWWWW",
]

x=y=0
 
for su in level:
	for ko in su:
		if ko=="W":
			wall=Wall((x,y))
		if ko=="E":
			exit = Exit((x,y))
		if ko=="P":
			me = Player((x,y))
		x += 8
	y += 8
	x = 0

mainrun=1

while mainrun:
	
	speed.tick(180)
	
	for evnt in pygame.event.get():
		if evnt.type == pygame.QUIT:
			mainrun=0 #pygame.quit()
			print "See You Later"
			#sys.exit()
		'''if evnt.type == pygame.KEYDOWN and evnt.key == pygame.K_ESCAPE:
			pygame.quit()
			print "See you Later"
			sys.exit()'''
	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT]:
		me.move(-1, 0)
	if key[pygame.K_RIGHT]:
		me.move(1, 0)
	if key[pygame.K_UP]:
		me.move(0, -1)
	if key[pygame.K_DOWN]:
		me.move(0, 1)
	if me.rect.colliderect(exit):
		mainrun=0 #raise SystemExit, "Good Job!"
		print "Good Job"
	exit.drawexit()
	wall.drawwall()
	me.drawplayer()
	pygame.display.flip() # pygame.display.update()
