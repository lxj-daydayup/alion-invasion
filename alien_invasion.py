import pygame
import sys
from ship import Ship
from setting import Settings
import game_function as gf 
from pygame.sprite import Group
from game_stats import Stats
from button import Button
from scoreboard import Scoreboard

def run_game():
	#初始化游戏并创建一个屏幕,创建setting实例和船实例,给游戏命名
	pygame.init()
	ai_setting=Settings()
	screen=pygame.display.set_mode(
	(ai_setting.screen_width,ai_setting.screen_height))
	pygame.display.set_caption('Alien Invasion')
	ship=Ship(ai_setting,screen)
	#创建用于存储子弹的编组
	bullets=Group()
	aliens=Group()
	gf.create_fleet(screen,ai_setting,ship,aliens)
	stats=Stats(ai_setting)
	play_button=Button(screen,ai_setting,'play')
	sb=Scoreboard(screen,stats,ai_setting)
	
	#开始游戏主循环
	while True:
		#监视键盘和鼠标事件
		gf.check_events(ai_setting,screen,stats,play_button,aliens,bullets,ship)
		if stats.game_active:
			ship.update()
			gf.update_bullets(screen,ai_setting,ship,bullets,aliens,stats,sb)
			gf.update_fleet(ai_setting,aliens,ship,screen,stats,bullets)
		
			
		
		
				
		gf.update_screen(ai_setting,screen,ship,bullets,aliens,stats,play_button,sb)
				
		
run_game()
				
	
	
