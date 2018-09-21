import os
import pygame
from VideoCapture import Device
import time
import sys
from pygame.locals import *
import faceu as bd
from wav import WWAV
from translation import Translation
import time
from aip import AipSpeech


pygame.init()
pygame.mixer.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (25, 27)
pygame.display.set_caption('人机匹配')
screen = pygame.display.set_mode((1300, 715))

# screen = pygame.display.set_mode((320, 240), 32, pygame.FULLSCREEN)
SLEEP_TIME_LONG = 0
# 初始化摄像头
cam = Device(devnum=0, showVideoWindow=0)
# filename = "./images/test.jpg"
cam.setResolution(640, 480)
bj = '.\images\\bgg.png'
mous = '.\images\\mous.png'
mous = pygame.image.load(mous)  # 拍照
mous1 = '.\images\\mouse.png'
mous1 = pygame.image.load(mous1)  # 换拍照按钮
nopeople = '.\images\\nopeople.png'
nopeople = pygame.image.load(nopeople)
n = '.\images\\222.png'
n1 = pygame.image.load(n)  # 扫描线
m = '.\images\\111.mp3'  # 开始音乐
pygame.mixer.music.load(m)
pygame.mixer.music.play()

def Robot_Speech(data):
    """ 百度AI语音合成"""
    APP_ID = '11528870'
    API_KEY = 'FdXMGfvchufHTIyyBDPAqqvu'
    SECRET_KEY = 'OQeLmMRoHiUL9W2lenTebkl6OjO90fOj'
    # 上面三个参数则需要去百度AI官网免费申请
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    # 合成语音类型参数，详见百度AI
    word = client.synthesis(data, 'zh', 1, {
        'vol': 10, 'spd': 2, 'per': '4'
    })
    # 识别正确返回语音二进制
    if not isinstance(word, dict):
        with open('abc.mp3','wb') as f: 
            f.write(word)
            f.close()         
    else:
        pass


class take_photo():
    tk = '.\images\\alert.png'
    al = pygame.image.load(tk)  # 提醒进入游戏图片
    filename = ".\images\\test.jpg"  # 照片保存名字
    path = os.path.abspath('')  # 当前路径
    image_msg = path + '\images\\test.jpg'  # 绝对路径
    print(image_msg)

    def image(self):
        cam.saveSnapshot(self.filename, timestamp=3, boldfont=1, quality=75)
        # 加载图像
        image = pygame.image.load(self.filename)
        bg = pygame.image.load(bj)

        # 传送画面
        screen.blit(image, (70, 125))
        screen.blit(bg, (0, 0))
        screen.blit(mous, (373, 513))

    # 显示实时图像，动态
    def show_video(self):
        n1_x = 217
        n1_y = 193

        while True:
            self.image()
            # global n1_y
            pre = pygame.mouse.get_pos()
            if 373 <= pre[0] <= 433 and 511 <= pre[1] <= 571:
                screen.blit(mous1, (366, 505))
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
            elif event.type == pygame.MOUSEBUTTONDOWN and 373 <= event.pos[0] <= 433 and 511 <= event.pos[1] <= 571:
                self.show_image()
            elif event.type == pygame.MOUSEBUTTONDOWN and 678 <= event.pos[0] <= 881 and 417 <= event.pos[1] <= 462:
                self.show_video()
            elif event.type == pygame.MOUSEBUTTONDOWN and 437 <= event.pos[0] <= 645 and 417 <= event.pos[
                1] <= 462:
                pygame.quit()
                os.system("python .\\index.py")
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and 905 <= event.pos[0] <= 1033 and 432 <= event.pos[1] <= 470:
                self.show_video()

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
            TextFont = pygame.font.Font(".\\ttf\\111.TTF", 30)
            infgander1 = TextFont.render(igender, True, (255, 255, 255))
            infage1 = TextFont.render(str(iage), True, (255, 255, 255))
            infscore1 = TextFont.render(str(int(ibeauty)), True, (255, 255, 255))
            screen.blit(infgander1, (1000, 274))
            screen.blit(infage1, (1000, 372))
            screen.blit(infscore1, (1000, 468))
            word1 = "您的战斗力是" + str(int(ibeauty))
            word2 = "匹配生命值是" + str(int(ibeauty))
            # word = word1 + word2
            # voice = communication(word)
            while pygame.mixer.music.get_busy():
                time.sleep(2)
            pygame.mixer.music.load('2.mp3')
            Robot_Speech(word1)
            pygame.mixer.music.load('abc.mp3')
            pygame.mixer.music.play()
            time.sleep(3)
            pygame.mixer.music.load('2.mp3')
            Robot_Speech(word2)
            pygame.mixer.music.load('abc.mp3')
            pygame.mixer.music.play()

        else:
            screen.blit(nopeople, (802, 141))
            TextFont = pygame.font.Font(".\\ttf\\123.ttf", 34)
            war = TextFont.render('未识别到人像', True, (255, 255, 255))
            screen.blit(war, (879, 335))
            TextFont = pygame.font.Font(".\\ttf\\123.ttf", 30)
            war1 = TextFont.render('重新扫描', True, (255, 255, 255))
            screen.blit(war1, (905, 430))
        while True:
            # 显示图像
            pygame.display.flip()
            if analytic_dict:
                time.sleep(2)
                screen.blit(self.al, (0, 0))
                screen.blit(infscore1, (810, 278))
                screen.blit(infscore1, (810, 332))

            self.handleEvent()


take = take_photo()
take.show_video()
