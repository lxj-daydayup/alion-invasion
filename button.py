import pygame.font
class Button():
	def __init__(self,screen,ai_setting,msg):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		#设置按钮大小和颜色
		self.width,self.height=200,50
		self.button_color=(0,255,0)
		self.text_color=(255,255,255)
		#从pygame.font模块中创建一个font实例
		self.font=pygame.font.SysFont('arial',36)
		#创建按钮矩形对象，设置按钮位置
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=self.screen_rect.center
		#在按钮上加载文字图像（创建按钮标签），通过prep_msg()完成
		self.prep_msg(msg)
		
	def prep_msg(self,msg):
		#通过访问font实例的render(文字，反锯齿布尔参数，文字颜色，图像背景颜色)方法创建文字图像
		self.msg_image=self.font.render(msg,True,self.text_color,self)
		self.msg_image_rect=self.msg_image.get_rect()
		self.msg_image_rect.center=self.rect.center
		
	def draw_button(self):
		#绘制一个颜色填充的按钮，再绘制文字图像
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)
		
		
		
		
		
		
		
		
