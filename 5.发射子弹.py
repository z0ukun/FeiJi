# coding=utf-8

import pygame
from pygame.locals import *

# 接下来要做的任务
# 1.实现飞机在你想要的位置显示
# 2.实现按键控制飞机移动
# 3.实现按下空格键的时候，显示一颗子弹

'''
1、搭建界面，主要完成窗口和背景图的显示
'''


class HeroPlane(object):
    def __init__(self, screen):
        # 设置飞机的默认位置
        self.x = 190
        self.y = 600
        # 设置要显示内容的窗口
        self.screen = screen
        # 用来保存英雄飞机需要的图片名字
        self.imageName = "./images/hero.gif"
        # 根据名字生成飞机图片
        self.image = pygame.image.load(self.imageName).convert()
        # 用来保存英雄飞机发射出的所有子弹
        self.bulletList = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

        # # 修改所有子弹的位置
        # for bullet in self.bulletList:
        #     bullet.y -= 2

    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10

    def sheBullet(self):
        newBullet = Bullet(self.x, self.y, self.screen)
        self.bulletList.append(newBullet)


# 定义子弹类
class Bullet(object):
    def __init__(self, x, y, screen):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen
        self.image = pygame.image.load("./images/bullet-3.gif").convert()

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 1


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
                    heroPlane.sheBullet()
        # 更新需要显示的内容
        pygame.display.update()
