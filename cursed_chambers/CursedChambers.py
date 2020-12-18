#CursedChambers.py
#Cpts 481 Python Software
#Professor Robert Lewis
#Student Anita Whyatt
#Final Project

#import all  regular modules:
import random
import math
import sys
#import pygame
import pygame
from pygame import mixer


#initialize the game
pygame.init()

#create screen size
display_width = 1000
display_height = 1000
screen = pygame.display.set_mode((display_width, display_height))


#Title & Icon & Clock
pygame.display.set_caption("Cursed Chambers")
icon = pygame.image.load('CursedIcon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

#Sounds:
player_shoot_sound = mixer.Sound('player_shot.wav')
wraith_shoot_sound = mixer.Sound('wraith_shot.wav')
gobbler_death_sound = mixer.Sound('gobbler_death.mp3')
wraith_death_sound = mixer.Sound('wraith_death.wav')
slug_death_sound = mixer.Sound('slug_death.wav')
player_damage_sound = mixer.Sound('player_damage.wav')
game_won_sound = mixer.Sound('game_won.wav')
game_over_sound = mixer.Sound('game_over.wav')
health_get_sound = mixer.Sound('health_get.wav')
power_get_sound = mixer.Sound('power_get.wav')
bigboss_hurt_sound = mixer.Sound('bigboss_hurt.wav')

dungeon_music_1 = mixer.Sound('DungeonMusic1.mp3')
dungeon_music_2 = mixer.Sound('DungeonMusic2.mp3')
dungeon_music_3 = mixer.Sound('DungeonMusic3.mp3')
curse_broken_music = mixer.Sound('UT-101-Good Night.mp3')

mixer.music.load('DungeonMusic1.mp3')
mixer.music.play(-1)


#Images:
level1Map = pygame.image.load('DungeonFloor1.png')
level2Map = pygame.image.load('DungeonFloor1.png')
level3Map = pygame.image.load('DungeonFloor1.png')

level4Map = pygame.image.load('DungeonFloor2.png')
level5Map = pygame.image.load('DungeonFloor2.png')

level6Map = pygame.image.load('DungeonFloor3.png')
level7Map = pygame.image.load('DungeonFloor3.png')

level8Map = pygame.image.load('DungeonFloor4.png')
level9Map = pygame.image.load('DungeonFloor4.png')

level10Map = pygame.image.load('DungeonFloor5.png')
level11Map = pygame.image.load('DungeonFloor5.png')

level12Map = pygame.image.load('DungeonFloor6.png')

heavenMap = pygame.image.load('HeavenlyBackdrop.png')

playerDown = pygame.image.load('CursedSpiritFront-br.png')
playerUp = pygame.image.load('CursedSpiritBack-br.png')
playerLeft = pygame.image.load('CursedSpiritLeftSide-br.png')
playerRight = pygame.image.load('CursedSpiritRightSide-br.png')
playerBullet = pygame.image.load('SacredFlameCharge.png') #player bullet texture
gobblerImageFront = pygame.image.load('GobblerFront-br.png')
gobblerImageBack = pygame.image.load('GobblerBack-br.png')
gobblerImageLeft = pygame.image.load('GobblerLeft-br.png')
gobblerImageRight = pygame.image.load('GobblerRight-br.png')
wraithImageFront = pygame.image.load('WraithFront-br.png')
wraithImageBack = pygame.image.load('WraithBack-br.png')
wraithImageLeft = pygame.image.load('WraithLeft-br.png')
wraithImageRight = pygame.image.load('WraithRight-br.png')
slugImageFront = pygame.image.load('SlugFront-br.png')
slugImageBack = pygame.image.load('SlugBack-br.png')
slugImageLeft = pygame.image.load('SlugLeft-br.png')
slugImageRight = pygame.image.load('SlugRight-br.png')
EvilBullet = pygame.image.load('EvilBullet-br.png') #evil bullet texture
PowerUpImg = pygame.image.load('PowerUp.png')
HealthUpImg = pygame.image.load('HealthUp.png')
PillarImg = pygame.image.load('Pillar-br.png')
BigbossImg = pygame.image.load('Bigboss-br.png')

#################################################
#################Helpful Classes#################
#################################################

class Level():
	def __init__(self):
		self.currentLevel = 1
		self.background = level1Map
		self.score = 0
		self.winScore = 1
		self.playerX = 500
		self.playerY = 500
		self.playerHealthSet = 1
		self.pUpX = 700
		self.pUpY = 500
		self.hUpX = 300
		self.hUpY = 500
		self.num_of_gobblers = 0
		self.num_of_wraiths = 0
		self.num_of_slugs = 0
		self.num_of_bigboss = 0
		self.gobbler_list = []
		self.wraith_list = []
		self.slug_list = []
		self.bigboss_list = []
		self.px = 0 #desired pillar x
		self.py = 0 #desired pillar y
	
	def spawn_monsters(self):
		#Declare all instances of gobblers
		self.gobbler_list = [] #will hold all instances of gobbler
		for i in range(self.num_of_gobblers):
			locX, locY = find_valid_spawn(self.playerX, self.playerY)
			gobbler = Gobbler(locX, locY)
			self.gobbler_list.append(gobbler)
		#Declare all instances of wraiths
		self.wraith_list = []
		for i in range(self.num_of_wraiths):
			locX, locY = find_valid_spawn(self.playerX, self.playerY)
			wraith = Wraith(locX, locY)
			self.wraith_list.append(wraith)
		#Declare all instances or slugs
		self.slug_list = []
		for i in range (self.num_of_slugs):
			locX, locY = find_valid_spawn(self.playerX, self.playerY)
			slug = Slug(locX, locY)
			self.slug_list.append(slug)
		self.bigboss_list = []
		for i in range(self.num_of_bigboss):
			bigboss = Bigboss()
			self.bigboss_list.append(bigboss)
	
	def load_level_1(self):
		self.background = level1Map
		self.score = 0
		self.winScore = 5
		self.playerX = 500
		self.playerY = 500
		self.playerHealthSet = 10
		self.pUpX = 500
		self.pUpY = 300
		self.hUpX = 700
		self.hUpY = 700
		self.num_of_gobblers = 5 
		self.num_of_wraiths = 0
		self.num_of_slugs = 0
		self.num_of_bigboss = 0
		self.px = 250
		self.py = 250
		self.spawn_monsters()
		return(self.px, self.py, self.pUpX, self.pUpY, self.hUpX, self.hUpY, self.px, self.py)

	def load_level_2(self):
		self.background = level2Map
		self.score = 0
		self.winScore = 5
		self.playerX = 500
		self.playerY = 500
		self.playerHealthSet = 10
		self.pUpX = 100
		self.pUpY = 800
		self.hUpX = 700
		self.hUpY = 150
		self.num_of_gobblers = 0
		self.num_of_wraiths = 5
		self.num_of_slugs = 0
		self.num_of_bigboss = 0
		self.px = 600
		self.py = 600
		self.spawn_monsters()
		
	def load_level_3(self):
		self.background = level3Map
		self.score = 0
		self.winScore = 5
		self.playerX = 500
		self.playerY = 500
		self.playerHealthSet = 10
		self.pUpX = 200
		self.pUpY = 200
		self.hUpX = 300
		self.hUpY = 850
		self.num_of_gobblers = 0
		self.num_of_wraiths = 0
		self.num_of_slugs = 5
		self.num_of_bigboss = 0
		self.px = 730
		self.py = 450
		self.spawn_monsters()
		
	def load_level_4(self):
		self.background = level4Map
		self.score = 0
		self.winScore = 9
		self.playerX = 500
		self.playerY = 500
		self.playerHealthSet = 10
		self.pUpX = 260
		self.pUpY = 400
		self.hUpX = 170
		self.hUpY = 850
		self.num_of_gobblers = 3
		self.num_of_wraiths = 3
		self.num_of_slugs = 3
		self.num_of_bigboss = 0
		self.px = 800
		self.py = 200
		self.spawn_monsters()
	
	def load_level_5(self):
		self.background = level5Map
		self.score = 0
		self.winScore = 15
		self.playerX = 500
		self.playerY = 500
		self.playerHealthSet = 10
		self.pUpX = 100
		self.pUpY = 870
		self.hUpX = 870
		self.hUpY = 100
		self.num_of_gobblers = 5
		self.num_of_wraiths = 5
		self.num_of_slugs = 5
		self.num_of_bigboss = 0
		self.px = 300
		self.py = 450
		self.spawn_monsters()
		
	def load_level_6(self):
		self.background = level6Map
		self.score = 0
		self.winScore = 15
		self.playerX = 500
		self.playerY = 500
		self.playerHealthSet = 10
		self.pUpX = 575
		self.pUpY = 575
		self.hUpX = 500
		self.hUpY = 675
		self.num_of_gobblers = 9
		self.num_of_wraiths = 3
		self.num_of_slugs = 3
		self.num_of_bigboss = 0
		self.px = 275
		self.py = 275
		self.spawn_monsters()
		
	def load_level_7(self):
		self.background = level7Map
		self.score = 0
		self.winScore = 20
		self.playerX = 500
		self.playerY = 500
		self.playerHealthSet = 10
		self.pUpX = 430
		self.pUpY = 440
		self.hUpX = 430
		self.hUpY = 560
		self.num_of_gobblers = 12
		self.num_of_wraiths = 4
		self.num_of_slugs = 4
		self.num_of_bigboss = 0
		self.px = 500
		self.py = 420
		self.spawn_monsters()
		
	def load_level_8(self):
		self.background = level8Map
		self.score = 0
		self.winScore = 15
		self.playerX = 500
		self.playerY = 500
		self.playerHealthSet = 10
		self.pUpX = 910
		self.pUpY = 860
		self.hUpX = 380
		self.hUpY = 30
		self.num_of_gobblers = 3
		self.num_of_wraiths = 9
		self.num_of_slugs = 3
		self.num_of_bigboss = 0
		self.px = 620
		self.py = 620
		self.spawn_monsters()
		
	def load_level_9(self):
		self.background = level9Map
		self.score = 0
		self.winScore = 20
		self.playerX = 500
		self.playerY = 500
		self.playerHealthSet = 10
		self.pUpX = 300
		self.pUpY = 500
		self.hUpX = 750
		self.hUpY = 500
		self.num_of_gobblers = 4
		self.num_of_wraiths = 12
		self.num_of_slugs = 4
		self.num_of_bigboss = 0
		self.px = 350
		self.py = 550
		self.spawn_monsters()
	
	def load_level_10(self):
		self.background = level10Map
		self.score = 0
		self.winScore = 15
		self.playerX = 500
		self.playerY = 500
		self.playerHealthSet = 10
		self.pUpX = 730
		self.pUpY = 50
		self.hUpX = 230
		self.hUpY = 730
		self.num_of_gobblers = 3
		self.num_of_wraiths = 3
		self.num_of_slugs = 9
		self.num_of_bigboss = 0
		self.px = 640
		self.py = 350
		self.spawn_monsters()
		
	def load_level_11(self):
		self.background = level11Map
		self.score = 0
		self.winScore = 20
		self.playerX = 500
		self.playerY = 500
		self.playerHealthSet = 10
		self.pUpX = 870
		self.pUpY = 870
		self.hUpX = 320
		self.hUpY = 830
		self.num_of_gobblers = 4
		self.num_of_wraiths = 4
		self.num_of_slugs = 12
		self.num_of_bigboss = 0
		self.px = 370
		self.py = 370
		self.spawn_monsters()
		
	def load_level_12(self):
		mixer.music.stop()
		mixer.music.load('DungeonMusic2.mp3')
		mixer.music.play(-1)
	
		self.background = level12Map
		self.score = 0
		self.winScore = 30
		self.playerX = 500
		self.playerY = 500
		self.playerHealthSet = 10
		self.pUpX = 420
		self.pUpY = 575
		self.hUpX = 420
		self.hUpY = 425
		self.num_of_gobblers = 10
		self.num_of_wraiths = 10
		self.num_of_slugs = 10
		self.num_of_bigboss = 0
		self.px = 485
		self.py = 450
		self.spawn_monsters()
		
	def load_level_13(self):
		mixer.music.stop()
		mixer.music.stop()
		mixer.music.load('DungeonMusic3.mp3')
		mixer.music.play(-1)
		
		self.background = level12Map
		self.score = 0
		self.winScore = 100
		self.playerX = 500
		self.playerY = 500
		self.playerHealthSet = 10
		self.pUpX = 350
		self.pUpY = 350
		self.hUpX = 750
		self.hUpY = 750
		self.num_of_gobblers = 0
		self.num_of_wraiths = 0
		self.num_of_slugs = 0
		self.num_of_bigboss = 1
		self.px = 1500
		self.py = 500
		self.spawn_monsters()
	
	def load_level_14(self):
		mixer.music.stop()
		mixer.music.stop()
		mixer.music.load('UT-101-Good Night.mp3')
		mixer.music.play(-1)
	
		self.background = heavenMap
		self.score = 0
		self.winScore = 1
		self.playerX = 500
		self.playerY = 900
		self.playerHealthSet = 10
		self.pUpX = 1500
		self.pUpY = 250
		self.hUpX = 1500
		self.hUpY = 500
		self.num_of_gobblers = 0
		self.num_of_wraiths = 0
		self.num_of_slugs = 0
		self.num_of_bigboss = 0
		self.px = 1500
		self.py = 750
		self.spawn_monsters()
		


	def game_over(self): #if the player loses the game
		LargeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSurf = LargeText.render("Try Again...", True, (0,0,0))
		TextRect = TextSurf.get_rect()
		TextRect.center = ((display_width/2), (display_height/2))
		screen.blit(TextSurf, TextRect)
		pygame.display.update()
		game_over_sound.play()
		pygame.time.wait(5000)
		
		if self.currentLevel == 2:
			self.load_level_2()
		elif self.currentLevel == 3:
			self.load_level_3()
		elif self.currentLevel == 4:
			self.load_level_4()
		if self.currentLevel == 5:
			self.load_level_5()
		if self.currentLevel == 6:
			self.load_level_6()
		if self.currentLevel == 7:
			self.load_level_7()
		if self.currentLevel == 8:
			self.load_level_8()
		if self.currentLevel == 9:
			self.load_level_9()
		if self.currentLevel == 10:
			self.load_level_10()
		if self.currentLevel == 11:
			self.load_level_11()
		if self.currentLevel == 12:
			self.load_level_12()
		if self.currentLevel == 13:
			self.load_level_13()
		if self.currentLevel >= 14:
			self.load_level_14()
			
		return(self.px, self.py, self.pUpX, self.pUpY, self.hUpX, self.hUpY)


	def level_won(self): #if the player wins the game
		LargeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSurf = LargeText.render("Level Clear!", True, (0,0,0))
		TextRect = TextSurf.get_rect()
		TextRect.center = ((display_width/2), (display_height/2))
		screen.blit(TextSurf, TextRect)
		pygame.display.update()
		game_won_sound.play()
		self.currentLevel += 1
		pygame.time.wait(2500)
		
		if self.currentLevel == 1:
			self.load_level_1()
		if self.currentLevel == 2:
			self.load_level_2()
		elif self.currentLevel == 3:
			self.load_level_3()
		elif self.currentLevel == 4:
			self.load_level_4()
		if self.currentLevel == 5:
			self.load_level_5()
		if self.currentLevel == 6:
			self.load_level_6()
		if self.currentLevel == 7:
			self.load_level_7()
		if self.currentLevel == 8:
			self.load_level_8()
		if self.currentLevel == 9:
			self.load_level_9()
		if self.currentLevel == 10:
			self.load_level_10()
		if self.currentLevel == 11:
			self.load_level_11()
		if self.currentLevel == 12:
			self.load_level_12()
		if self.currentLevel == 13:
			self.load_level_13()
		if self.currentLevel >= 14:
			self.load_level_14()
			
			
		return(self.px, self.py, self.pUpX, self.pUpY, self.hUpX, self.hUpY)
		
		
#Create a pillar object to serve as an obstacle
class Pillar:
	def __init__(self):
		self.X = 0
		self.Y = 0
		
	def show_pillar(self):
		screen.blit(PillarImg, (self.X, self.Y))
		
	def pillar_bullet_check(self, bulletX, bulletY):
		nearX = self.X - 24
		nearY = self.Y - 24
		farX = nearX + 80 
		farY = nearY + 230 
		if bulletX >= nearX and bulletX <= farX and bulletY >= nearY and bulletY <= farY:
			return True
		else:
			return False
	
	def pillar_person_check(self, personX, personY): #for player
		nearX = self.X - 24
		nearY = self.Y - 24
		farX = nearX + 80
		farY = nearY + 230
		#pillar's 'lid'
		if personX >= nearX and personX <= farX and personY >= nearY and personY <= nearY + 24:
			personY = nearY - 1
		#pillar's 'bottom'
		if personX >= nearX and personX <= farX and personY <= farY and personY >= farY - 24:
			personY = farY + 1
		#pillar's left edge
		if personY >= nearY and personY <= farY and personX >= nearX and personX <= nearX + 24:
			personX = nearX - 1
		#pillar's right edge
		if personY >= nearY and personY <= farY and personX <= farX and personX >= farX - 24:
			personX = farX + 1
		return(personX, personY)
	

class Bigboss(): #big bad boss monster
	def __init__ (self):
		self.X = 363
		self.Y = 50
		self.spawned = True
		self.speed = 5
		#self.health = 5	#use level.score instead
		self.chaseBehavior = True
		self.timeStore = -7500
	
	def bigboss_move_decision(self, playerX, playerY):
		timeGrab = pygame.time.get_ticks()
		if timeGrab >= self.timeStore + 7500:
			if self.chaseBehavior == False:
				self.chaseBehavior = True
			elif self.chaseBehavior == True:
				self.chaseBehavior = False
			self.timeStore = pygame.time.get_ticks()
			
		#variable declarations
		XDiff = self.X - playerX
		YDiff = self.Y - playerY
			
		#first behavior cycle 'circle'
		if self.chaseBehavior == False:
			
			if self.X <= 5 and self.Y <= 5: #upper left corner
				self.X += 1 * self.speed
				screen.blit(BigbossImg, (self.X, self.Y))
			elif self.X >= 750 and self.Y <=5: #upper right corner
				self.Y += 1 * self.speed
				screen.blit(BigbossImg, (self.X, self.Y))
			elif self.X >= 750 and self.Y >= 750: #bottom right corner
				self.X += -1 * self.speed
				screen.blit(BigbossImg, (self.X, self.Y))
			elif self.X <= 5 and self.Y >= 750: #bottom left corner
				self.Y += -1 * self.speed
				screen.blit(BigbossImg, (self.X, self.Y))
			elif self.X <= 5: #left edge
				self.Y += -1 * self.speed
				screen.blit(BigbossImg, (self.X, self.Y))
			elif self.Y <= 5: #upper edge
				self.X += 1 * self.speed
				screen.blit(BigbossImg, (self.X, self.Y))
			elif self.X >= 750: #right edge
				self.Y += 1 * self.speed
				screen.blit(BigbossImg, (self.X, self.Y))
			elif self.Y >= 750: #bottom edge
				self.X += -1 * self.speed
				screen.blit(BigbossImg, (self.X, self.Y))
			else:
				if abs(XDiff) >= abs(YDiff):
					if self.X >= playerX:
						self.X += 1 * self.speed
						screen.blit(BigbossImg, (self.X, self.Y))
					elif self.X <= playerX:
						self.X += -1 *self.speed
						screen.blit(BigbossImg, (self.X, self.Y))
				if abs(XDiff) <= abs(YDiff):
					if self.Y >= playerY:
						self.Y  += 1 * self.speed
						screen.blit(BigbossImg, (self.X, self.Y))
					elif self.Y <= playerY:
						self.Y += -1 * self.speed
						screen.blit(BigbossImg, (self.X, self.Y))

		#second behavior cycle 'chase'
		if self.chaseBehavior == True:
			centerX = self.X + 137
			centerY = self.Y + 137
			if abs(XDiff) >= abs(YDiff):
				if centerX >= playerX:
					self.X += -1 * self.speed
					screen.blit(BigbossImg, (self.X, self.Y))
				elif centerX <= playerX:
					self.X += self.speed
					screen.blit(BigbossImg, (self.X, self.Y))
			if abs(XDiff) <= abs(YDiff):
				if centerY >= playerY:
					self.Y  += -1 * self.speed
					screen.blit(BigbossImg, (self.X, self.Y))
				elif centerY <= playerY:
					self.Y += self.speed
					screen.blit(BigbossImg, (self.X, self.Y))
		

	def bullet_collision_check(self, bulletX, bulletY): #did bullet hit monster
		centerX = self.X + 137
		centerY = self.Y + 137
		distance = math.sqrt( (math.pow( (centerX-bulletX), 2 )) + (math.pow( (centerY-bulletY), 2 )) )
		if distance < 140 and self.spawned == True:
			return True
		else:
			return False
	
	def enemy_collision_check(self, playerX, playerY): #did we hit player?
		centerX = self.X + 137
		centerY = self.Y + 137
		distance = math.sqrt( (math.pow( (centerX-playerX), 2 )) + (math.pow( (centerY-playerY), 2 )) )
		if distance < 140 and self.spawned == True:
			return True
		else:
			return False








class Gobbler():
	def __init__(self, gobblerX, gobblerY):
		self.gobblerX = gobblerX
		self.gobblerY = gobblerY
		self.gobblerOrientaion = "Down"
		self.gobblerSpawned = True
		self.gobblerSpeed = 3.5
	
	def gobbler_move_decision(self, playerX, playerY): #gobbler decides what it will do
		#variable declarations
		XDiff = self.gobblerX - playerX
		YDiff = self.gobblerY - playerY
		#constrain movement to map
		self.gobblerX, self.gobblerY = constrain_movement(self.gobblerX, self.gobblerY)
	
		if abs(XDiff) >= abs(YDiff):
			if self.gobblerX >= playerX:
				self.gobblerX += -1 * self.gobblerSpeed
				self.gobblerOrientation = "Left"
				screen.blit(gobblerImageLeft, (self.gobblerX, self.gobblerY))
			elif self.gobblerX <= playerX:
				self.gobblerX += self.gobblerSpeed
				self.gobblerOrientation = "Right"
				screen.blit(gobblerImageRight, (self.gobblerX, self.gobblerY))
		if abs(XDiff) <= abs(YDiff):
			if self.gobblerY >= playerY:
				self.gobblerY  += -1 * self.gobblerSpeed
				self.gobblerOrientation = "Up"
				screen.blit(gobblerImageBack, (self.gobblerX, self.gobblerY))
			elif self.gobblerY <= playerY:
				self.gobblerY += self.gobblerSpeed
				self.gobblerOrientation = "Down"
				screen.blit(gobblerImageFront, (self.gobblerX, self.gobblerY))
	
	def enemy_collision_check(self, playerX, playerY): #did we hit player?
		distance = math.sqrt( (math.pow( (self.gobblerX-playerX), 2 )) + (math.pow( (self.gobblerY-playerY), 2 )) )
		if distance < 27 and self.gobblerSpawned == True:
			return True
		else:
			return False

	def bullet_collision_check(self, bulletX, bulletY): #did bullet hit monster?
		distance = math.sqrt( (math.pow( (self.gobblerX-bulletX), 2 )) + (math.pow( (self.gobblerY-bulletY), 2 )) )
		if distance < 27 and self.gobblerSpawned == True:
			self.gobblerSpawned = False
			return True
		else:
			return False
	


class Wraith():
	def __init__(self, wraithX, wraithY):
		self.wraithX = wraithX
		self.wraithY = wraithY
		self.wraithOrientation = "Down"
		self.wraithSpawned = True
		self.wraithSpeed = 2
		self.wraithBulletX = -100
		self.wraithBulletY = -100
		self.wraithBulletXChange = 0
		self.wraithBulletYChange = 0
		self.wraithBulletState = "ready"
		self.wraithBulletSpeed = 8
	
	def enemy_collision_check(self, playerX, playerY): #did we hit player?
		distance = math.sqrt( (math.pow( (self.wraithX-playerX), 2 )) + (math.pow( (self.wraithY-playerY), 2 )) )
		if distance < 27 and self.wraithSpawned == True:
			return True
		else:
			return False
			
	def bullet_collision_check(self, bulletX, bulletY): #did bullet his us?
		distance = math.sqrt( (math.pow( (self.wraithX-bulletX), 2 )) + (math.pow( (self.wraithY-bulletY), 2 )) )
		if distance < 27 and self.wraithSpawned == True:
			self.wraithSpawned = False
			return True
		else:
			return False
	
	def hit_player_check(self, playerX, playerY): #did our bullet hit player?
		distance = math.sqrt( (math.pow( (playerX-self.wraithBulletX), 2 )) + (math.pow( (playerY-self.wraithBulletY), 2 )) )
		if distance < 27:
			self.wraithBulletState = "ready"
			self.wraithBulletXChange = 0
			self.wraithBulletYChange = 0
			self.wraithBulletX = -100 #off screen
			self.wraithBulletY = -100 #off screen
			return True
		else:
			return False
	
	def wraith_move_decision(self, playerX, playerY): #wraith decides what it will do
		#variable declarations
		XDiff = self.wraithX - playerX
		YDiff = self.wraithY - playerY
		#constrain movement to map
		self.wraithX, self.wraithY = constrain_movement(self.wraithX, self.wraithY)
		#First we decide if we want to shoot!
		if self.wraithBulletState == "ready": #don't shoot if you've already shot
			self.wraithBulletX = self.wraithX #make sure bullet fires from wraith
			self.wraithBulletY = self.wraithY
			if abs(XDiff) <= 10 and abs(XDiff) <= abs(YDiff):
				if self.wraithY >= playerY: #wraith south of player
					self.wraithOrientation = "Up"
					self.wraithBulletYChange = -1 * (self.wraithBulletSpeed)
					self.wraithBulletState = "fired"
				elif self.wraithY <= playerY: #wraith north of player
					self.wraithOrientation = "Down"
					self.wraithBulletYChange = self.wraithBulletSpeed
					self.wraithBulletState = "fired"
			if abs(YDiff) <= 10 and abs(YDiff) <= abs(XDiff):
				if self.wraithX >= playerX: #wraith east of player
					self.wraithOrientation = "Left"
					self.wraithBulletXChange = -1 * (self.wraithBulletSpeed)
					self.wraithBulletState = "fired"
				elif self.wraithX <= playerX: #wraith west of player
					self.wraithOrientation = "Right" 
					self.wraithBulletXChange = self.wraithBulletSpeed
					self.wraithBulletState = "fired"
	
		#If we don't shoot, we move instead
		if abs(XDiff) >= abs(YDiff):
			if self.wraithX >= playerX:
				self.wraithX += -1 * self.wraithSpeed
				self.wraithOrientation = "Left"
				screen.blit(wraithImageLeft, (self.wraithX, self.wraithY))
			elif self.wraithX <= playerX:
				self.wraithX += self.wraithSpeed
				self.wraithOrientation = "Right"
				screen.blit(wraithImageRight, (self.wraithX, self.wraithY))
		if abs(XDiff) <= abs(YDiff):
			if self.wraithY >= playerY:
				self.wraithY += -1 * self.wraithSpeed
				self.wraithOrientation = "Up"
				screen.blit(wraithImageBack, (self.wraithX, self.wraithY))
			elif self.wraithY <= playerY:
				self.wraithY += self.wraithSpeed
				self.wraithOrientation = "Down"
				screen.blit(wraithImageFront, (self.wraithX, self.wraithY))
	
	def update_bullet(self): #updates the bullet
		if self.wraithBulletX <= 0 or self.wraithBulletX >= 935 or self.wraithBulletY <= 0 or self.wraithBulletY >= 935:
			self.wraithBulletState = "ready"
			self.wraithBulletXChange = 0
			self.wraithBulletYChange = 0
			self.wraithBulletX = -100 #off screen
			self.wraithBulletY = -100 #off screen
		self.wraithBulletX += self.wraithBulletXChange
		self.wraithBulletY += self.wraithBulletYChange
		screen.blit(EvilBullet, (self.wraithBulletX+16, self.wraithBulletY+16))
		

class Slug():
	def __init__(self, slugX, slugY):
		self.slugX = slugX
		self.slugY = slugY
		self.slugSpeed = 10
		self.slugOrientation = "Down"
		self.slugSpawned = True
	
	def slug_move_decision(self, playerX, playerY):
		#variable declarations
		XDiff = self.slugX - playerX
		YDiff = self.slugY - playerY
		#constrain movement to map
		self.slugX, self.slugY = constrain_movement(self.slugX, self.slugY)
		
		if self.slugX <= 35 and self.slugY <= 35: #upper left corner
			self.slugX += 1 * self.slugSpeed
			self.slugOrientation = "Right"
			screen.blit(slugImageRight, (self.slugX, self.slugY))
		elif self.slugX >= 900 and self.slugY <=35: #upper right corner
			self.slugY += 1 * self.slugSpeed
			self.slugOrientation = "Down"
			screen.blit(slugImageFront, (self.slugX, self.slugY))
		elif self.slugX >= 900 and self.slugY >= 900: #bottom right corner
			self.slugX += -1 * self.slugSpeed
			self.slugOrientation = "Left"
			screen.blit(slugImageLeft, (self.slugX, self.slugY))
		elif self.slugX <= 35 and self.slugY >= 900: #bottom left corner
			self.slugY += -1 * self.slugSpeed
			self.slugOrientation = "Up"
			screen.blit(slugImageBack, (self.slugX, self.slugY))
		elif self.slugX <= 35: #left edge
			self.slugY += -1 * self.slugSpeed
			self.slugOrientation = "Up"
			screen.blit(slugImageBack, (self.slugX, self.slugY))
		elif self.slugY <= 35: #upper edge
			self.slugX += 1 * self.slugSpeed
			self.slugOrientation = "Right"
			screen.blit(slugImageRight, (self.slugX, self.slugY))
		elif self.slugX >= 900: #right edge
			self.slugY += 1 * self.slugSpeed
			self.slugOrientation = "Down"
			screen.blit(slugImageFront, (self.slugX, self.slugY))
		elif self.slugY >= 900: #bottom edge
			self.slugX += -1 * self.slugSpeed
			self.slugOrientation = "Left"
			screen.blit(slugImageLeft, (self.slugX, self.slugY))
		else:
			if abs(XDiff) >= abs(YDiff):
				if self.slugX >= playerX:
					self.slugX += 1 * self.slugSpeed
					self.slugOrientation = "Right"
					screen.blit(slugImageRight, (self.slugX, self.slugY))
				elif self.slugX <= playerX:
					self.slugX += -1 *self.slugSpeed
					self.slugOrientation = "Left"
					screen.blit(slugImageLeft, (self.slugX, self.slugY))
			if abs(XDiff) <= abs(YDiff):
				if self.slugY >= playerY:
					self.slugY  += 1 * self.slugSpeed
					self.slugOrientation = "Down"
					screen.blit(slugImageFront, (self.slugX, self.slugY))
				elif self.slugY <= playerY:
					self.slugY += -1 * self.slugSpeed
					self.slugOrientation = "Up"
					screen.blit(slugImageBack, (self.slugX, self.slugY))
		
	def bullet_collision_check(self, bulletX, bulletY): #did bullet his us?
		distance = math.sqrt( (math.pow( (self.slugX-bulletX), 2 )) + (math.pow( (self.slugY-bulletY), 2 )) )
		if distance < 27 and self.slugSpawned == True:
			self.slugSpawned = False
			return True
		else:
			return False
	
	def enemy_collision_check(self, playerX, playerY): #did we hit player?
		distance = math.sqrt( (math.pow( (self.slugX-playerX), 2 )) + (math.pow( (self.slugY-playerY), 2 )) )
		if distance < 27 and self.slugSpawned == True:
			return True
		else:
			return False

num_of_left_diag_bullets = 10
num_of_right_diag_bullets = 10
num_of_bullets = 10 #how many bullets can you have at once
class Bullet(): #manages player bullets (regular)
	def __init__(self):
		self.bulletX = -100
		self.bulletY = -100
		self.bulletXChange = 0
		self.bulletYChange = 0
		self.bulletState = "ready"
		self.bulletSpeed = 15
	
	def fire_bullet(self, playerX, playerY, playerOrientation):
		self.bulletX = playerX
		self.bulletY = playerY
		self.bulletState = "fired"
		if playerOrientation == "Left":
			self.bulletYChange = 0
			self.bulletXChange = -1 * self.bulletSpeed
		if playerOrientation == "Right":
			self.bulletYChange = 0
			self.bulletXChange = self.bulletSpeed
		if playerOrientation == "Up":
			self.bulletYChange = -1 * self.bulletSpeed
			self.bulletXChange = 0
		if playerOrientation == "Down":
			self.bulletYChange = self.bulletSpeed
			self.bulletXChange = 0 
		screen.blit(playerBullet, (self.bulletX+16, self.bulletY+16)) #display bullet
		
	def fire_left_diag_bullet(self, playerX, playerY, playerOrientation):
		self.bulletX = playerX
		self.bulletY = playerY
		self.bulletState = "fired"
		if playerOrientation == "Left":
			self.bulletYChange = 2
			self.bulletXChange = -1 * self.bulletSpeed
		if playerOrientation == "Right":
			self.bulletYChange = -2
			self.bulletXChange = self.bulletSpeed
		if playerOrientation == "Up":
			self.bulletYChange = -1 * self.bulletSpeed
			self.bulletXChange = -2
		if playerOrientation == "Down":
			self.bulletYChange = self.bulletSpeed
			self.bulletXChange = 2
		screen.blit(playerBullet, (self.bulletX+16, self.bulletY+16)) #display bullet
	
	def fire_right_diag_bullet(self, playerX, playerY, playerOrientation):
		self.bulletX = playerX
		self.bulletY = playerY
		self.bulletState = "fired"
		if playerOrientation == "Left":
			self.bulletYChange = -2
			self.bulletXChange = -1 * self.bulletSpeed
		if playerOrientation == "Right":
			self.bulletYChange = 2
			self.bulletXChange = self.bulletSpeed
		if playerOrientation == "Up":
			self.bulletYChange = -1 * self.bulletSpeed
			self.bulletXChange = 2
		if playerOrientation == "Down":
			self.bulletYChange = self.bulletSpeed
			self.bulletXChange = -2 
		screen.blit(playerBullet, (self.bulletX+16, self.bulletY+16)) #display bullet
	
	
	def update_bullet(self):
		if self.bulletX <= -20 or self.bulletX >= 955 or self.bulletY <= -20 or self.bulletY >= 955:
			self.bulletState = "ready"
			self.bulletXChange = 0
			self.bulletYChange = 0
			self.bulletX = -100 #off screen
			self.bulletY = -100 #off screen
		self.bulletX += self.bulletXChange
		self.bulletY += self.bulletYChange
		screen.blit(playerBullet, (self.bulletX+16, self.bulletY+16)) #display bullet
		
class Player():
	def __init__(self):
		self.X = 500
		self.Y = 500
		self.XChange = 0
		self.YChange = 0
		self.speed = 9
		self.Orientation = "Down"
		self.invincible = False
		self.health = 10
		self.score = 0
	
	def move_left(self):
		self.XChange = -1 * self.speed
		self.Orientation = "Left"
	
	def move_right(self):
		self.XChange = self.speed
		self.Orientation = "Right"
	
	def move_up(self):
		self.YChange = -1 * self.speed
		self.Orientation = "Up"
	
	def move_down(self):
		self.YChange = self.speed
		self.Orientation = "Down"
		
	def keyup_leftright(self):
		self.XChange = 0
		
	def keyup_updown(self):
		self.YChange = 0

	def update_player(self):
		self.X += self.XChange
		self.Y += self.YChange
		self.X, self.Y = constrain_movement(self.X, self.Y)
		if self.Orientation == "Down":
			screen.blit(playerDown, (self.X, self.Y))
		elif self.Orientation == "Up":
			screen.blit(playerUp, (self.X, self.Y))
		elif self.Orientation == "Left":
			screen.blit(playerLeft, (self.X, self.Y))
		elif self.Orientation == "Right":
			screen.blit(playerRight, (self.X, self.Y))

class Powerup(): #A neat powerup the player can grab!
	def __init__(self):
		self.pUpX = 500
		self.pUpY = 700
		self.pUpSpawned = True
		self.pUpActive = False #is powerup in effect?
		self.timeActivated = -7500
	
	
	def update_powerup(self, playerX, playerY):
		distance = math.sqrt( (math.pow( (playerX-self.pUpX), 2 )) + (math.pow( (playerY-self.pUpY), 2 )) )
		if distance < 50 and self.pUpSpawned == True and self.pUpActive == False:
			self.pUpActive = True
			self.pUpSpawned = False
			self.timeActivated = pygame.time.get_ticks()
			power_get_sound.play()
		
		get_time = pygame.time.get_ticks()
		if get_time >= self.timeActivated + 7500:
			self.pUpActive = False
			
		if self.pUpSpawned == True:
			screen.blit(PowerUpImg, (self.pUpX, self.pUpY))

class Healthup(): #handy health pack for player
	def __init__(self):
		self.hUpX = 800
		self.hUpY = 800
		self.hUpSpawned = True
		
	def update_healthup(self, playerX, playerY): #if returns True player has stepped on health up
		if self.hUpSpawned == True:
			screen.blit(HealthUpImg, (self.hUpX, self.hUpY))
		distance = math.sqrt( (math.pow( (playerX-self.hUpX), 2 )) + (math.pow( (playerY-self.hUpY), 2 )) )
		if distance < 50 and self.hUpSpawned == True:
			self.hUpSpawned = False
			health_get_sound.play()
			return True
		else:
			return False
						
		
#################################################
#################Functions Phase#################
#################################################
#spawn somewhere that isn't on top of the player
def find_valid_spawn(playerX, playerY):
	while True:
		enemyX = random.randint(0, 935)
		enemyY = random.randint(0, 935)
		distance = math.sqrt( (math.pow( (enemyX-playerX), 2 )) + (math.pow( (enemyY-playerY), 2 )) )
		if distance >= 100:
			return(enemyX, enemyY)
			break

def constrain_movement(x, y): #stay on map, should change with level
	#if level == 1
	if x <= 0:
		x = 0
	if x >= 935:
		x = 935
	if y <= 0:
		y = 0
	if y >= 935:
		y = 935
	return(x, y)

def display_player_score(player_score):
	font = pygame.font.SysFont(None, 40)
	text = font.render("Score: " +str(player_score), True, (255,255,255))
	screen.blit(text, (300, 0))

def display_player_health(player_health):
	font = pygame.font.SysFont(None, 40)
	text = font.render("Health: " +str(player_health), True, (255,255,255))
	screen.blit(text, (0,0))


	


	
	



#################################################
#################Game Loop Phase#################
#################################################
def game_start():
	
	#Create our global instance of level
	level = Level()
	
	player = Player()
	#Player bullet creation:
	bullet_list_left_diag = []
	bullet_list_right_diag = []
	bullet_list = []
	for i in range(num_of_bullets):
		bullet = Bullet()
		bullet_list.append(bullet)
	for i in range(num_of_left_diag_bullets):
		bullet = Bullet()
		bullet_list_left_diag.append(bullet)
	for i in range(num_of_right_diag_bullets):
		bullet = Bullet()
		bullet_list_right_diag.append(bullet)
	#powerup creation
	powerup = Powerup()
	healthup = Healthup()
	#create pillar obstacle
	pillar = Pillar()
	
	#After all level/player/bullet creations:
	pillar.X, pillar.Y, powerup.pUpX, powerup.pUpX, healthup.hUpX, healthup.hUpy, pillar.X, pillar.Y = level.load_level_1()
	
	



	#################################################
	#################Game Loop Phase#################
	#################################################

	running = True
	while running == True:
	
		
	
		#Background:
		screen.blit(level.background, (0,0))
	
		
		
		#######EVENT LOOP#######
		for event in pygame.event.get():
			if event.type == pygame.QUIT: #Quit Option
				running = False
				#ensure sucessful quit
				pygame.quit()
				quit()
		
			#Take Key Input:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.move_left()
				if event.key == pygame.K_RIGHT:
					player.move_right()
				if event.key == pygame.K_UP:
					player.move_up()
				if event.key == pygame.K_DOWN:
					player.move_down()
				if event.key == pygame.K_SPACE:
					bulletFound = False #have we found a bullet?
					for bullet in bullet_list:
						if bullet.bulletState == "ready" and bulletFound == False:
							player_shoot_sound.play()
							bullet.fire_bullet(player.X, player.Y, player.Orientation)
							bulletFound = True
					bulletFound = False
					if powerup.pUpActive == True:
						for bullet in bullet_list_left_diag:
							if bullet.bulletState == "ready" and bulletFound == False:
								bullet.fire_left_diag_bullet(player.X, player.Y, player.Orientation)
								bulletFound = True
						bulletFound = False
						for bullet in bullet_list_right_diag:
							if bullet.bulletState == "ready" and bulletFound == False:
								bullet.fire_right_diag_bullet(player.X, player.Y, player.Orientation)
								bulletFound = True
					
						
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					player.keyup_leftright()
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					player.keyup_updown()
		
		
		#update visual display of pillar obstacle
		pillar.show_pillar()
		#Power up update
		powerup.update_powerup(player.X, player.Y)
		if powerup.pUpActive == True:
			player.speed = 11
		else:
			player.speed = 9
		heal_player = healthup.update_healthup(player.X, player.Y)
		if heal_player == True:
			player.health += 5
		
		#Player Update
		player.X, player.Y = pillar.pillar_person_check(player.X, player.Y)
		player.update_player()
		#Player Bullet Updates
		for bullet in bullet_list:
			if bullet.bulletState == "fired":
				bullet.update_bullet()
		for bullet in bullet_list_left_diag:
			if bullet.bulletState == "fired":
				bullet.update_bullet()
		for bullet in bullet_list_right_diag:
			if bullet.bulletState == "fired":
				bullet.update_bullet()
		#Enemy 'Bigboss' Update:
		for monster in level.bigboss_list:
			if monster.spawned == True:
				monster.bigboss_move_decision(player.X, player.Y)
		
		
		#Enemy 'Gobbler' Update:
		for monster in level.gobbler_list:
			if monster.gobblerSpawned == True:
				monster.gobbler_move_decision(player.X, player.Y)
			monster.gobblerX, monster.gobblerY = pillar.pillar_person_check(monster.gobblerX, monster.gobblerY)
		#Enemy 'Wraith' Update:
		for monster in level.wraith_list:
			if monster.wraithSpawned == True:
				monster.wraith_move_decision(player.X, player.Y)
			if monster.wraithBulletState == "fired":
				monster.update_bullet()
			monster.wraithX, monster.wraithY = pillar.pillar_person_check(monster.wraithX, monster.wraithY)
		#Enemy 'Slug' Update:
		for monster in level.slug_list:
			if monster.slugSpawned == True:
				monster.slug_move_decision(player.X, player.Y)
			monster.slugX, monster.slugY = pillar.pillar_person_check(monster.slugX, monster.slugY)
				
		
		#Player bullet collision checks with monsters (and pillar)
		for bullet in bullet_list:
			was_there_collision = pillar.pillar_bullet_check(bullet.bulletX, bullet.bulletY)
			if was_there_collision == True:
				bullet.bulletState = "ready"
				bullet.bulletX = -100
				bullet.bulletY = -100
				bullet.bulletXChange = 0
				bullet.bulletYChange = 0
			for monster in level.gobbler_list:
				was_there_collision = monster.bullet_collision_check(bullet.bulletX, bullet.bulletY)
				if was_there_collision == True:
					level.score += 1
					bullet.bulletState = "ready"
					bullet.bulletX = -100
					bullet.bulletY = -100
					bullet.bulletXChange = 0
					bullet.bulletYChange = 0
					gobbler_death_sound.play()		
			for monster in level.wraith_list:
				was_there_collision = monster.bullet_collision_check(bullet.bulletX, bullet.bulletY)
				if was_there_collision == True:
					level.score += 1
					bullet.bulletState = "ready"
					bullet.bulletX = -100
					bullet.bulletY = -100
					bullet.bulletXChange = 0
					bullet.bulletYChange = 0
					wraith_death_sound.play()
			for monster in level.slug_list:
				was_there_collision = monster.bullet_collision_check(bullet.bulletX, bullet.bulletY)
				if was_there_collision == True:
					level.score += 1
					bullet.bulletState = "ready"
					bullet.bulletX = -100
					bullet.bulletY = -100
					bullet.bulletXChange = 0
					bullet.bulletYChange = 0
					slug_death_sound.play()
			for monster in level.bigboss_list:
				was_there_collision = monster.bullet_collision_check(bullet.bulletX, bullet.bulletY)
				if was_there_collision == True:
					level.score += 1
					bullet.bulletState = "ready"
					bullet.bulletX = -100
					bullet.bulletY = -100
					bullet.bulletXChange = 0
					bullet.bulletYChange = 0
					bigboss_hurt_sound.play()
					
					
		#Check the left diag bullet list for monster collision			
		for bullet in bullet_list_left_diag:
			was_there_collision = pillar.pillar_bullet_check(bullet.bulletX, bullet.bulletY)
			if was_there_collision == True:
				level.score += 1
				bullet.bulletState = "ready"
				bullet.bulletX = -100
				bullet.bulletY = -100
				bullet.bulletXChange = 0
				bullet.bulletYChange = 0
			for monster in level.gobbler_list:
				was_there_collision = monster.bullet_collision_check(bullet.bulletX, bullet.bulletY)
				if was_there_collision == True:
					level.score += 1
					bullet.bulletState = "ready"
					bullet.bulletX = -100
					bullet.bulletY = -100
					bullet.bulletXChange = 0
					bullet.bulletYChange = 0
					gobbler_death_sound.play()	
			for monster in level.wraith_list:
				was_there_collision = monster.bullet_collision_check(bullet.bulletX, bullet.bulletY)
				if was_there_collision == True:
					level.score += 1
					bullet.bulletState = "ready"
					bullet.bulletX = -100
					bullet.bulletY = -100
					bullet.bulletXChange = 0
					bullet.bulletYChange = 0
					wraith_death_sound.play()
			for monster in level.slug_list:
				was_there_collision = monster.bullet_collision_check(bullet.bulletX, bullet.bulletY)
				if was_there_collision == True:
					level.score += 1
					bullet.bulletState = "ready"
					bullet.bulletX = -100
					bullet.bulletY = -100
					bullet.bulletXChange = 0
					bullet.bulletYChange = 0
					slug_death_sound.play()
			for monster in level.bigboss_list:
				was_there_collision = monster.bullet_collision_check(bullet.bulletX, bullet.bulletY)
				if was_there_collision == True:
					level.score += 1
					bullet.bulletState = "ready"
					bullet.bulletX = -100
					bullet.bulletY = -100
					bullet.bulletXChange = 0
					bullet.bulletYChange = 0
					bigboss_hurt_sound.play()
		#check the right diag bullet list for collision with monster
		for bullet in bullet_list_right_diag:
			was_there_collision = pillar.pillar_bullet_check(bullet.bulletX, bullet.bulletY)
			if was_there_collision == True:
				bullet.bulletState = "ready"
				bullet.bulletX = -100
				bullet.bulletY = -100
				bullet.bulletXChange = 0
				bullet.bulletYChange = 0
			for monster in level.gobbler_list:
				was_there_collision = monster.bullet_collision_check(bullet.bulletX, bullet.bulletY)
				if was_there_collision == True:
					level.score += 1
					bullet.bulletState = "ready"
					bullet.bulletX = -100
					bullet.bulletY = -100
					bullet.bulletXChange = 0
					bullet.bulletYChange = 0
					gobbler_death_sound.play()	
			for monster in level.wraith_list:
				was_there_collision = monster.bullet_collision_check(bullet.bulletX, bullet.bulletY)
				if was_there_collision == True:
					level.score += 1
					bullet.bulletState = "ready"
					bullet.bulletX = -100
					bullet.bulletY = -100
					bullet.bulletXChange = 0
					bullet.bulletYChange = 0
					wraith_death_sound.play()
			for monster in level.slug_list:
				was_there_collision = monster.bullet_collision_check(bullet.bulletX, bullet.bulletY)
				if was_there_collision == True:
					level.score += 1
					bullet.bulletState = "ready"
					bullet.bulletX = -100
					bullet.bulletY = -100
					bullet.bulletXChange = 0
					bullet.bulletYChange = 0
					slug_death_sound.play()
			for monster in level.bigboss_list:
				was_there_collision = monster.bullet_collision_check(bullet.bulletX, bullet.bulletY)
				if was_there_collision == True:
					level.score += 1
					bullet.bulletState = "ready"
					bullet.bulletX = -100
					bullet.bulletY = -100
					bullet.bulletXChange = 0
					bullet.bulletYChange = 0
					bigboss_hurt_sound.play()
				
				
				
				
				
		#check for gobbler collisions with player & pillar
		for monster in level.gobbler_list:
			was_there_collision = monster.enemy_collision_check(player.X, player.Y)
			if was_there_collision == True:
				if player.invincible == False:
					time_struck = pygame.time.get_ticks()
					player.health -= 1
					player.invincible = True
					player_damage_sound.play()


					
		#check for wraith collisions with player
		for monster in level.wraith_list:
			was_there_collision = monster.enemy_collision_check(player.X, player.Y)
			if was_there_collision == True:
				if player.invincible == False:
					time_struck = pygame.time.get_ticks()
					player.health -= 1
					player.invincible = True
					player_damage_sound.play()
	
			#check for collision of wraith bullet with player:
			was_there_collision = monster.hit_player_check(player.X, player.Y)
			if was_there_collision == True:
				if player.invincible == False:
					time_struck = pygame.time.get_ticks()
					player.health -= 1
					player.invincible = True
					player_damage_sound.play()
			was_there_collision = pillar.pillar_bullet_check(monster.wraithBulletX, monster.wraithBulletY)
			if was_there_collision == True:
				monster.wraithBulletState = "ready"
				monster.wraithBulletX = -100
				monster.wraithBulletY = -100
				monster.wraithBulletXChange = 0
				monster.wraithBulletYChange = 0
		
		#Check for slug collision with player
		for monster in level.slug_list:
			was_there_collision = monster.enemy_collision_check(player.X, player.Y)
			if was_there_collision == True:
				if player.invincible == False:
					time_struck = pygame.time.get_ticks()
					player.health -= 1
					player.invincible = True
					player_damage_sound.play()
					
		for monster in level.bigboss_list:
			was_there_collision = monster.enemy_collision_check(player.X, player.Y)
			if was_there_collision == True:
				if player.invincible == False:
					time_struck = pygame.time.get_ticks()
					player.health -= 1
					player.invincible = True
					player_damage_sound.play()

					
		
		#check to see if player is still invincible
		if player.invincible == True:
			get_time = pygame.time.get_ticks()
			if get_time >= time_struck + 200:
				player.invincible = False
	
	
		if player.health <= 0:
			powerup.pUpSpawned = True
			powerup.pUpActive = False
			healthup.hUpSpawned = True
			player.X = 500
			player.Y = 500
			player.health = 10
			pillar.X, pillar.Y, powerup.pUpX, powerup.pUpY, healthup.hUpX, healthup.hUpY = level.game_over()
			
			
		if level.score >= level.winScore:
			powerup.pUpSpawned = True
			powerup.pUpActive = False
			healthup.hUpSpawned = True
			player.X = 500
			player.Y = 500
			player.health = 10
			pillar.X, pillar.Y, powerup.pUpX, powerup.pUpY, healthup.hUpX, healthup.hUpY = level.level_won()
	
	
		display_player_health(player.health)
		display_player_score(level.score)
		pygame.display.update()#update the screen
		clock.tick(60)

#run the game loop
game_start()
pygame.quit()
quit()
















