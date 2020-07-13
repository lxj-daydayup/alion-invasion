# alion-invasion
## 项目介绍
* 外星人侵略射击游戏。该项目基于Python3.6编写，是《Python编程：从入门到实践》中的项目，目的用于学习的入门Python项目。 使用上下左右移动飞船位置，空格发射子弹。外星人会左右移动并且下移。
当外星人到达屏幕底部或者碰到飞船将重新开始，有3条命。
增加计分、关卡数和最高分显示，随着关卡数增加，飞船相应速度、子弹速度和消灭外星人的分数也会增加，相应地，外星人速度也会提高，提高难度。

## 目录结构
* alion-invasion.py是游戏的入口程序，包含游戏的主逻辑。初始化游戏并创建一个屏幕，为每个游戏所需的类创建实例，给游戏命名，响应用户按键。
* alion.py bullet.py button.py scoreboard.py screen.py ship.py分别定义了游戏中的外星人类、子弹类、按钮类、计分板类、屏幕类和飞船类。
* game_function定义了支撑游戏主程序的函数，包括创建类，判断边界条件，响应用户按键，更新屏幕等。
* setting.py定义了游戏的设置，包括外星人移动速度、子弹大小等。包含游戏设置更新的方法，关卡升级的时候会调用该方法。

## 下载安装
* 下载dist文件夹，点击alion_invasion.exe可执行文件即可开始游戏
