import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
	'''创建管理子弹的类'''
	def __init__(self,ai_setting,screen,ship):
		super().__init__()
		self.screen=screen
		
		#在（0，0）处创建一个子弹
		self.rect=pygame.Rect(0,0,ai_setting.bullet_width,
		ai_setting.bullet_height)
		self.rect.centerx=ship.rect.centerx
		self.rect.bottom=ship.rect.top
		
		#用小数存储子弹位置
		self.y=float(self.rect.y)
		#给子弹的颜色和速度赋值
		self.color=ai_setting.bullet_color
		self.speed_factor=ai_setting.bullet_speed_factor
		
	def update(self):
		'''向右移动子弹'''
		self.y-=self.speed_factor
		self.rect.y=self.y
	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
		

		
