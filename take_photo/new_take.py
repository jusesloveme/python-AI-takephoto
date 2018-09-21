import os
import pygame
from VideoCapture import Device
import time
import sys
from pygame.locals import *
import faceu as bd

pygame.init()
pygame.mixer.init()
pygame.display.set_caption('人机匹配')
screen = pygame.display.set_mode((1300, 700))
# screen = pygame.display.set_mode((320, 240), 32, pygame.FULLSCREEN)
SLEEP_TIME_LONG = 0.001
# 初始化摄像头
cam = Device(devnum=0, showVideoWindow=0)
# filename = "./images/test.jpg"
cam.setResolution(640, 480)
bj = '.\images\\bg (3).png'
en = '.\images\\timg.jpg'
m = 'C:\\Users\winnie\Desktop\\111.mp3'
n = '.\images\\222.png'
pygame.mixer.music.load(m)
pygame.mixer.music.play()
n1 = pygame.image.load(n)


class take_photo():
    tk = '.\images\\alert.png'
    al = pygame.image.load(tk)
    filename = ".\images\\test.jpg"
    path = os.path.abspath('')  # 当前路径
    image_msg = path + '\images\\test.jpg'
    print(image_msg)

    def image(self):
        cam.saveSnapshot(self.filename, timestamp=3, boldfont=1, quality=75)
        # 加载图像
        image = pygame.image.load(self.filename)
        bg = pygame.image.load(bj)

        # 传送画面
        screen.blit(image, (70, 125))
        screen.blit(bg, (0, 0))

    # 显示实时图像，动态
    def show_video(self):
        n1_x = 210
        n1_y = 193

        while True:
            self.image()
            # global n1_y
            if 494 >= n1_y >= 193:
                n1_y += 10
                if n1_y > 493:
                    n1_y = 193
            screen.blit(n1, (n1_x, n1_y))
            # 显示图像
            pygame.display.flip()
            # 休眠一下
            time.sleep(SLEEP_TIME_LONG)
            if self.handleEvent():
                break

    # 监测退出事件
    def handleEvent(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and 308 <= event.pos[0] <= 478 and 519 <= event.pos[1] <= 561:
                self.show_image()
            elif event.type == pygame.MOUSEBUTTONDOWN and 678 <= event.pos[0] <= 881 and 417 <= event.pos[1] <= 462:
                self.show_video()
            elif event.type == pygame.MOUSEBUTTONDOWN and 437 <= event.pos[0] <= 645 and 417 <= event.pos[
                1] <= 462:
                pygame.quit()
                os.system("python .\\index.py")
                exit()

    # 显示拍摄的图片,静态
    def show_image(self):
        self.image()
        # 创建实例对象，获取解析的人脸信息
        face = bd.Faceu()
        face.face_detection(self.image_msg)
        analytic_dict = face.face_detection(self.image_msg)
        if analytic_dict:
            igender = analytic_dict['gender']
            iage = analytic_dict['age']
            ibeauty = analytic_dict['beauty']
            with open('1.txt', 'w') as f:
                f.write(str(int(ibeauty)))

            if igender == 'male':
                igender = '男'
            else:
                igender = '女'

            # 在画布上写出信息
            TextFont = pygame.font.SysFont("simsunnsimsun", 30)
            infgander1 = TextFont.render(igender, True, (255, 255, 255))
            infage1 = TextFont.render(str(iage), True, (255, 255, 255))
            infscore1 = TextFont.render(str(int(ibeauty)), True, (255, 255, 255))
            screen.blit(infgander1, (1000, 270))
            screen.blit(infage1, (1000, 370))
            screen.blit(infscore1, (1000, 470))

        else:
            TextFont = pygame.font.SysFont("simsunnsimsun", 40)
            war = TextFont.render('未识别到人像', True, (255, 255, 255))
            screen.blit(war, (800, 350))

        while True:
            # 显示图像
            pygame.display.flip()
            time.sleep(1)
            screen.blit(self.al, (0, 0))
            screen.blit(infscore1, (810, 281))
            screen.blit(infscore1, (810, 334))
            self.handleEvent()


take = take_photo()
take.show_video()
