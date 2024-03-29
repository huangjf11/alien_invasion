import sys
import pygame

#监视屏幕和鼠标事件
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right=True
            elif event.key == pygame.K_LEFT:
                ship.moving_left=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right=False
            elif event.key == pygame.K_LEFT:
                ship.moving_left=False

def update_screen(ai_settings,screen,ship,people):
    """更新屏幕上的图像，并切换到新图像"""
    #每次循环时都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    people.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()