import os
import sys
import time
import json
import pygame
import PySimpleGUI as sg
from pygame.locals import *
from settings import *
from level import Level

# Game Screen
pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load("music.mpe")
# pygame.mixer.music.play(-1)


# variables
BGC = (255,255,255)
FPS = 60
MAX_BULLETS = 6
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
WIDTH, HEIGHT = 500, 800
gui_font = pygame.font.SysFont('comicsans', 30)
# YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets/player', 'spaceship_yellow.png')).convert_alpha()
BACKGROUND_IMAGE1 = pygame.image.load(os.path.join('Assets/background', 'Space-Background-1.jpeg'))
BACKGROUND_IMAGE2 = pygame.image.load(os.path.join('Assets/background', 'Space-Background-2.jpeg'))
# YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 0)
data_in = {

}


Screenlevel = [
  "intro",
  "main_game"
]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
myFont = pygame.font.SysFont('Calibri', 14)


SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
clock = pygame.time.Clock()

player_health = 10
player_bullets = []

end_text = ""

# with open('data24.txt', 'w') as data24_file:
#     json.dump(data_in, data24_file)
#     
try:
    with open('data24.txt') as data24_file:
        data_out = json.load(data24_file)
        for entry in data_out.items():
            print(entry)
except:
  print('An exception occurred')



class GameState:
    def __init__(self):
        self.state = "intro"
        
    def Intro(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
                sys.exit('exit')
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "main_game"
        # drawing
        Drew_Window(self.state, player_health, player_bullets)
        
    def Main_game(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
                sys.exit('exit')
                
        # drawing
        Drew_Window(self.state, player_health, player_bullets)
        
    def state_manager(self, state):
        if self.state == "intro":
            self.Intro()
        jls_extract_var = True
        if self.state == "main_game" or state == jls_extract_var:
        # if self.state == "main_game":
            self.Main_game()

GameState = GameState()

State23 = "gfff"

def Main():
    
    prev_time = time.time()
    run = True
    while run:
        dt = time.time() - prev_time
        prev_time = time.time()
        GameState.state_manager(State23)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)

buttons = []
class Button(pygame.sprite.Sprite):
	def __init__(self,text,translation,width,height,pos,elevation):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]
        
		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'
		self.translation = translation
		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#354B5E'
		#text
		self.text = text
		self.text_surf = gui_font.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
		buttons.append(self)
		self.draw()
 
	def change_text(self, newtext):
		self.text_surf = gui_font.render(newtext, True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
 
	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 
 
		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
 
		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()
 
	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if event.type == pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
				self.change_text(f"{self.translation}")
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					print('click')
					self.pressed = False
					self.change_text(self.text)
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'
   
class Player():
    def __init__(self):
        x, y = pygame.mouse.get_pos()

    def draw(self):
        x, y = pygame.mouse.get_pos()
        YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets/player', 'spaceship_yellow.png')).convert_alpha()
        yellow = pygame.Rect(x, y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 0)
        screen.blit(YELLOW_SPACESHIP, (yellow.x - (SPACESHIP_WIDTH/2), yellow.y - (SPACESHIP_HEIGHT/2) ))
        
def draw_game_over(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    screen.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    draw_loser(text)
    pygame.display.update()
    pygame.time.delay(5000)
    
def Drew_Window(state, player_health, player_bullets):
    x,y = pygame.mouse.get_pos()
    if state == "intro":
        screen.blit(BACKGROUND_IMAGE1,(0, 0))
        button = Button('play',0, 130, 70, (200,200), 5)
        pygame.mouse.set_visible(True)
        button.draw()
    elif state == "main_game":
        screen.blit(BACKGROUND_IMAGE2,(0, 0))
        pygame.mouse.set_visible(False)
        # label = myFont.render("Winner", False, 'Green')
        (Player()).draw()

# controls

# x,y = pygame.mouse.get_pos()

# def yellow_handle_movement(keys_pressed, yellow):
#     if keys_pressed[pygame.K_a, pygame.K_LEFT] and yellow.x - VEL > 0:  # LEFT
#         yellow.x -= VEL
#     if keys_pressed[pygame.K_d, pygame.K_RIGHT] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
#         yellow.x += VEL
#     if keys_pressed[pygame.K_w, pygame.K_UP] and yellow.y - VEL > 0:  # UP
#         yellow.y -= VEL
#     if keys_pressed[pygame.K_s, pygame.K_DOWN] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
#         yellow.y += VEL


class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Zelda')
		self.clock = pygame.time.Clock()

		self.level = Level()
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()