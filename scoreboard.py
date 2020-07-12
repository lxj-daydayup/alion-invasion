import pygame.font
class Scoreboard():
	def __init__(self,screen,stats,ai_setting):
		self.screen=screen
		self.ai_setting=ai_setting
		self.screen_rect=self.screen.get_rect()
		self.stats=stats
		#设置分数字体和颜色
		self.score_color=(30,30,30)
		#创建SysFont的一个实例并初始化字体
		self.font=pygame.font.SysFont('arial',36)
		#准备初始得分图像
		self.prep_score()
	
	def prep_score(self):
		rounded_score=int(round(self.stats.score,-1))
		
		score_str="{:,}".format(rounded_score)
		#访问SysFont类的render方法，该方法返回一个surface图像
		self.image=self.font.render(score_str,True,
		self.score_color,self.ai_setting.bg_color)
		self.image_rect=self.image.get_rect()
		#将得分放在屏幕右上角
		self.image_rect.right=self.screen_rect.right-10
		self.image_rect.top=20
	
	def draw_score(self):
		self.screen.blit(self.image,self.image_rect)
	
	
