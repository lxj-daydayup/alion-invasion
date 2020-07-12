import sys
import pygame
from bullet import Bullet
from alien import Alien
from ship import Ship
from time import sleep


def check_keydown_event(ai_setting,event,screen,ship,bullets,stats,aliens):

	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key==pygame.K_LEFT:
		ship.moving_left=True
	elif event.key==pygame.K_UP:
		ship.moving_up=True
	elif event.key==pygame.K_SPACE:
		if len(bullets)<ai_setting.bullet_allowed:
			#创建一颗子弹并加入到编组bulltes(主程序中bullets=Group()是一个编组)中
			new_bullet=Bullet(ai_setting,screen,ship)
			bullets.add(new_bullet)
			#bullets中的每一个元素都是Bullet的实例，所以主程序中bullet可以直接访问Bullet类的属性
	elif event.key==pygame.K_DOWN:
		ship.moving_down=True		
	elif event.key==pygame.K_q:
		
		sys.exit()	
	elif event.key==pygame.K_p:
		ai_setting.initialize_dynamic_settings()
		start_game(stats,aliens,bullets,screen,ai_setting,ship)
def check_keyup_event(event,ship):
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key==pygame.K_LEFT:
		ship.moving_left=False
	elif event.key==pygame.K_UP:
		ship.moving_up=False	
	elif event.key==pygame.K_DOWN:
		ship.moving_down=False	

def check_events(ai_setting,screen,stats,play_button,aliens,bullets,ship):
	'''响应鼠标和按键'''
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pygame.mouse.get_pos()
			check_play_button(ai_setting,screen,stats,play_button,mouse_x,mouse_y,aliens,bullets,ship)
		
		elif event.type==pygame.KEYDOWN:
			check_keydown_event(ai_setting,event,screen,ship,bullets,stats,aliens)
		elif event.type==pygame.KEYUP:
			check_keyup_event(event,ship)

def check_play_button(ai_setting,screen,stats,play_button,mouse_x,mouse_y,aliens,bullets,ship):
	button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		ai_setting.initialize_dynamic_settings()
		start_game(stats,aliens,bullets,screen,ai_setting,ship)
	
		

def start_game(stats,aliens,bullets,screen,ai_setting,ship):
	pygame.mouse.set_visible(False)
	stats.reset_stats()
	stats.game_active=True
	aliens.empty()
	bullets.empty()
	create_fleet(screen,ai_setting,ship,aliens)
	ship.ship_center()								
		
def update_screen(ai_setting,screen,ship,bullets,aliens,stats,play_button,sb):
	'''更新屏幕上的图像，并切换到心屏幕'''
	#每次循环都重绘屏幕
	screen.fill(ai_setting.bg_color)
	
	ship.blitme()
	for bullet in bullets:
		bullet.draw_bullet()
	aliens.draw(screen)
	sb.draw_score()
	if not stats.game_active:
		play_button.draw_button()
		
	pygame.display.flip()
					
				
def create_fleet(screen,ai_setting,ship,aliens):
	'''创建一群外星人，计算外星人个数并初始化其位置'''
	alien=Alien(screen,ai_setting)	
	
	alien_width=alien.rect.width
	alien_height=alien.rect.height
	
	for row_number in range(get_number_rows(ai_setting,alien_height,ship.height)):
		for alien_number in range(get_number_alien_x(ai_setting,alien_width)):
			create_alien(ai_setting,screen,aliens,alien_number,row_number)	
		
		
def get_number_rows(ai_setting,alien_height,ship_height):
	available_space_y=int(ai_setting.screen_height-3*alien_height-ship_height)	
	number_rows=int(available_space_y/(2*alien_height))
	return number_rows
    
    
def get_number_alien_x(ai_settings,alien_width):
	alien_number_x=int((ai_settings.screen_width-2*alien_width)/(2*alien_width))
	return alien_number_x

def create_alien(ai_setting,screen,aliens,alien_number,row_number):
	alien=Alien(screen,ai_setting)	
	alien_width=alien.rect.width
	alien.x=alien_width+2*alien_width*alien_number
	alien.rect.x=alien.x
	alien.rect.y=alien.rect.height+2*alien_width*row_number
	aliens.add(alien)	

def check_fleet_edges(aliens,ai_setting):
	for alien in aliens.sprites():
		if alien.check_alien_edge():
			change_direction(ai_setting,aliens)
			break
			
def change_direction(ai_setting,aliens):
	for alien in aliens.sprites():
		alien.rect.y+=ai_setting.alien_drop_speed
	ai_setting.fleet_direction*=-1
	
def update_fleet(ai_setting,aliens,ship,screen,stats,bullets):
	check_fleet_edges(aliens,ai_setting)
	aliens.update()
	if pygame.sprite.spritecollideany(ship,aliens):
		print('ship hit')
		ship_hit(stats,aliens,bullets,ship,screen,ai_setting)
	check_alien_bottom(stats,aliens,bullets,ship,screen,ai_setting)
		
def update_bullets(screen,ai_setting,ship,bullets,aliens,stats,sb):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom<0:
			bullets.remove(bullet)
	collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
	if collisions:
		for aliens in collisions.values():
			stats.score+=ai_setting.alien_points*len(aliens)
			sb.prep_score()
		
		
	if len(aliens)==0:
		bullets.empty()
		ai_setting.increase_speed()
		create_fleet(screen,ai_setting,ship,aliens)	
				
def ship_hit(stats,aliens,bullets,ship,screen,ai_setting):
	'''响应外星人撞到飞船'''
	stats.ship_left-=1	
	#清空子弹和外星人列表
	aliens.empty()
	bullets.empty()
	#将飞船放在屏幕中央并创建一群新的外星人
	if stats.ship_left>0:
		stats.game_active=True
	else:
		stats.game_active=False
		pygame.mouse.set_visible(True)
		
	
	create_fleet(screen,ai_setting,ship,aliens)
	ship.ship_center()
	#暂停0.5秒
	sleep(0.5)
	
def check_alien_bottom(stats,aliens,bullets,ship,screen,ai_setting):
	screen_rect=screen.get_rect()
	for alien in aliens:
		if alien.rect.bottom>=screen_rect.bottom:
			ship_hit(stats,aliens,bullets,ship,screen,ai_setting)
			break	
	
	
			 
