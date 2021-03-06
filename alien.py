import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	'''创建外星人类'''
	def __init__(self,screen,ai_setting):
		super().__init__()
		self.screen=screen
		self.ai_setting=ai_setting
		self.image=pygame.image.load(r'D:\python\alion\images\alien.bmp')
		self.rect=self.image.get_rect()
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		self.x=float(self.rect.x)
		
	def check_alien_edge(self):
		screen_rect=self.screen.get_rect()
		if self.rect.right>=screen_rect.right:
			return True
		elif self.rect.left<=0:
			return True
	
	def update(self):
		
		self.x+=self.ai_setting.alien_speed_factor*self.ai_setting.fleet_direction
		self.rect.x=self.x
	
	def blitme(self):
		self.screen.blit(self.image,self.rect)
	
	

