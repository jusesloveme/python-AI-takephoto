import os
import random

import pygame
from VideoCapture import Device
import time
import sys
from pygame.locals import *
import faceu as bd

# import index

pygame.init()
pygame.mixer.init()
pygame.display.set_caption('人机匹配')
screen = pygame.display.set_mode((1300, 700))
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
n1_x = 210
n1_y = 193
speed = 5
h_direction = 1
qwe = True


class take_photo():
    tk = '.\images\\alert.png'
    al = pygame.image.load(tk)
    filename = ".\images\\test.jpg"
    path = os.path.abspath('')  # 当前路径
    image_msg = path + '\images\\test.jpg'
    print(image_msg)

    # male_list1 = ['王祖蓝', '黄渤', '郭德纲', '小沈阳', '杜海涛']
    # male_list2 = ['雷佳音', '孙红雷', '吴京', '张学友', '雷佳音']
    # male_list3 = ['霍建华', '李敏镐', '黄子韬', '周杰伦', '邓超']
    # male_list4 = ['蔡徐坤', '张艺兴', '黄晓明', '胡歌', '吴亦凡']
    # male_list5 = ['鹿晗', '王俊凯', '王源', '陈伟霆', '吴磊']
    # female_list1 = ['贾玲', '吴莫愁', '凤姐', '谢依霖', '韩红']
    # female_list2 = ['周冬雨', '曾轶可', '容祖儿', '戚薇', '邓紫棋']
    # female_list3 = ['张韶涵', '白百何', '宋祖儿', '杨紫', '林心如']
    # female_list4 = ['郑爽', '韩雪', '赵丽颖', '刘亦菲', '关晓彤']
    # female_list5 = ['杨幂', '唐嫣', 'Angelababy', '赵丽颖', '刘诗诗']
    # sim = ['94%', '95%', '96%', '97%', '98%']

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
        while True:
            self.image()
            # n1_y += speed * h_direction
            screen.blit(n1, (n1_x, n1_y))
            # if n1_y > 230:
            #     h_direction = -h_direction
            # elif n1_y < 0:
            #     h_direction = -h_direction
            # pygame.display.update()
            # 显示图像
            pygame.display.flip()
            # 休眠一下
            time.sleep(SLEEP_TIME_LONG)
            # for i in range(193, 509):
            #     n1 = pygame.image.load(n)
            #     screen.blit(n1, (210, i))
            #     if i == 509:
            #         break
            # for v in range(4):
            #     tick.tick(4)
            #     rect2.y += v * rect2.height
            #     if rect2.y > 1000:
            #         rect2.y = 0
            #     screen.fill((255, 255, 255))
            #     screen.blit(n1, (210, 193), rect2)  # 这里给了3个实参，分别是图像，绘制的位置，绘制的截面框
            #     # pygame.display.flip()
            if self.handleEvent():
                break

    # 监测退出事件
    def handleEvent(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            elif event.type == pygame.MOUSEBUTTONDOWN and 308 <= event.pos[0] <= 478 and 519 <= event.pos[1] <= 561:
                self.show_image()

    # def life_num(self):
    #     life1 = int(analytic_dict['beauty'])
    #     return life1
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
            if igender == 'male':
                igender = '男'
            else:
                igender = '女'
            # 判断颜值，根据颜值写相似度
            # if igender == 'male':
            #     if int(ibeauty) <= 20:
            #         people = self.male_list1[random.randint(0, 4)]
            #     elif 20 < int(ibeauty) <= 30:
            #         people = self.male_list2[random.randint(0, 4)]
            #     elif 30 < int(ibeauty) <= 40:
            #         people = self.male_list3[random.randint(0, 4)]
            #     elif 40 < int(ibeauty) <= 50:
            #         people = self.male_list4[random.randint(0, 4)]
            #     elif 50 < int(ibeauty) :
            #         people = self.male_list5[random.randint(0, 4)]
            # if igender == 'female':
            #     if int(ibeauty) <= 20:
            #         people = self.female_list1[random.randint(0, 4)]
            #     elif 20 < int(ibeauty) <= 30:
            #         people = self.female_list2[random.randint(0, 4)]
            #     elif 30 < int(ibeauty) <= 40:
            #         people = self.female_list3[random.randint(0, 4)]
            #     elif 40 < int(ibeauty) <= 50:
            #         people = self.female_list4[random.randint(0, 4)]
            #     elif 50 < int(ibeauty):
            #         people = self.female_list5[random.randint(0, 4)]

            # 写出信息
            TextFont = pygame.font.SysFont("simsunnsimsun", 30)
            infgander1 = TextFont.render(igender, True, (255, 255, 255))
            infage1 = TextFont.render(str(iage), True, (255, 255, 255))
            infscore1 = TextFont.render(str(int(ibeauty)), True, (255, 255, 255))
            # infsimilar = TextFont.render('和' + people + '相似度为' + self.sim[random.randint(0, 4)], True, (255, 255, 255))
            screen.blit(infgander1, (1000, 270))
            screen.blit(infage1, (1000, 370))
            screen.blit(infscore1, (1000, 470))
            # screen.blit(infsimilar, (800, 490))

        else:
            TextFont = pygame.font.SysFont("simsunnsimsun", 40)
            war = TextFont.render('未识别到人像', True, (255, 255, 255))
            screen.blit(war, (800, 350))

        while True:
            # 显示图像
            pygame.display.flip()

            time.sleep(5)
            screen.blit(self.al, (0, 0))
            screen.blit(infscore1, (810, 281))
            screen.blit(infscore1, (810, 334))

            # self.handleEvent()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and 678 <= event.pos[0] <= 881 and 417 <= event.pos[1] <= 462:
                    self.show_video()
                # elif event.type == QUIT or event.type == pygame.MOUSEBUTTONDOWN and 735 <= event.pos[
                #     0] <= 925 and 433 <= event.pos[1] <= 4063:
                #     os.system("python index.py")sys.exit()
                #     os.system("python .\\index.py")
                elif event.type == pygame.MOUSEBUTTONDOWN and 437 <= event.pos[0] <= 645 and 417 <= event.pos[
                    1] <= 462:
                    # os.system("python .\\index.py") and sys.exit()
                    # pygame.quit()
                    # global qwe
                    # qwe = False
                    # os.system("python .\\index.py")
                    pygame.quit()
                    exit()
                    # print('111')
                    # sys.exit()
                    # if os.system("python .\\index.py"):
                        # pygame.quit()
                        # exit()
                        # sys.exit()
                    # os._exit()
                elif event.type == QUIT:
                    sys.exit()


    # def show_alert(self):
    #     time.sleep(10)
    #     screen.blit(self.al, (600, 300))


# if __name__ == '__main__':

take = take_photo()
take.show_video()
if qwe == False:
    os.system("python .\\index.py")

# for event in pygame.event.get():
#     if event.type == pygame.KEYDOWN:  # 键被按下
#         if event.key == pygame.K_0:
#             take.show_video()

# if __name__ == '__main__':
#     main()
#     import os
#
#     str = ('python index.py')  # python命令 + B.py
#     p = os.system(str)
#     print(p)  # 打印执行结果 0表示 success ， 1表示 fail
