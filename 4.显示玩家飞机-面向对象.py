# coding=utf-8

import pygame
from pygame.locals import *

'''
1、搭建界面，主要完成窗口和背景图的显示
'''


class HeroPlane(object):
    def __init__(self, screen):
        # 设置飞机的默认位置
        self.x = 230
        self.y = 600
        # 设置要显示内容的窗口
        self.screen = screen
        # 用来保存英雄飞机需要的图片名字
        self.imageName = "./images/hero.gif"
        # 根据名字生成飞机图片
        self.image = pygame.image.load(self.imageName).convert()
        # 用来保存英雄飞机发射出的所有子弹
        self.bullet = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10

    def sheBullet(self):
        pass


if __name__ == "__main__":
    # 1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 890), 0, 32)

    # 2.创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./images/background.png").convert()

    # 创建一个飞机对象
    heroPlane = HeroPlane(screen)

    # 3.把背景图片放到窗口中显示
    while True:
        # 显示背景图片
        screen.blit(background, (0, 0))

        # 显示一个飞机

        heroPlane.display()

        # 获取事件，比如按键等
        for event in pygame.event.get():

            # 判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()

            # 判断是否是按下了键
            elif event.type == KEYDOWN:

                # 检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    heroPlane.moveLeft()
                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    heroPlane.moveRight()
                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')
                    # Heroplane.sheBullet()
        # 更新需要显示的内容
        pygame.display.update()
