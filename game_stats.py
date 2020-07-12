class Stats():
	def __init__(self,ai_setting):
		'''初始化统计信息'''
		self.game_active=False
		self.ai_setting=ai_setting
		
		self.reset_stats()
		
	def reset_stats(self):
		'''初始化在游戏期间可能变化的统计信息'''
		self.ship_left=self.ai_setting.ship_limit
		self.score=0
		
