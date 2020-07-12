import pygame
class Ship():
	
	def __init__(self,ai_setting,screen):
		'''初始化飞船并设置其初始位置'''
		self.screen=screen
		self.ai_setting=ai_setting
		#加载飞船图像并获取其外接矩形
		self.image=pygame.image.load(r'D:\python\alion\images\ship.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.height=self.rect.height
		#将飞船放在屏幕底部中央
		self.rect.bottom=self.screen_rect.bottom
		self.rect.centerx=self.screen_rect.centerx
		
		#定义移动标志并初始化
		self.moving_right=False
		self.moving_left=False
		self.moving_up=False
		self.moving_down=False
		#在属性center中存储飞船中心横坐标位置的小数值
		self.centerx=float(self.rect.centerx)
		self.centery=float(self.rect.centery)
		self.bottom=float(self.rect.bottom)
	    
	def update(self):
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.centerx+=self.ai_setting.ship_speed_factor
		if self.moving_left and self.rect.left>0:
			self.centerx-=self.ai_setting.ship_speed_factor
		
		if self.moving_up and self.rect.top>0:
			self.centery-=self.ai_setting.ship_speed_factor
		if self.moving_down and self.rect.bottom<600:
			self.centery+=self.ai_setting.ship_speed_factor
		self.rect.centery=self.centery
		self.rect.centerx=self.centerx
		
	def ship_center(self):
		
		self.centerx=self.screen_rect.centerx
		self.rect.centerx=self.centerx
		self.centery=self.screen_rect.bottom-self.rect.height/2
		
	
	def blitme(self):
		'''在指定位置绘制飞船'''
		self.screen.blit(self.image,self.rect)


