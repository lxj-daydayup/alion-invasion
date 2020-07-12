class Settings():
	def __init__(self):
		#屏幕设置
		self.screen_width=1200
		self.screen_height=600
		self.bg_color=(230,230,230)
		#飞船设置
		
		self.ship_limit=3
		
		#子弹设置
		
		self.bullet_width=3
		self.bullet_height=15
		self.bullet_color=60,60,60
		self.bullet_allowed=5
		#外星人速度和移动方向设置
		
		self.alien_drop_speed=5
		
		#加快游戏节奏设置
		self.speedup_scale=1.1
		self.score_scale=1.5
		self.initialize_dynamic_settings()
	def increase_speed(self):
		self.ship_speed_factor*=self.speedup_scale
		self.bullet_speed_factor*=self.speedup_scale
		self.alien_speed_factor*=self.speedup_scale	
		self.alien_points*=self.score_scale
	def initialize_dynamic_settings(self):
		self.ship_speed_factor=1.5
		self.bullet_speed_factor=3
		self.alien_speed_factor=1
		self.fleet_direction=1
		self.alien_points=50
	
		
		
		
    
	
	
		
    
	
	
	
	
	
	
