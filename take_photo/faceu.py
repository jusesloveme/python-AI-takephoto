import base64
import pygame
import sys
import requests


# 初始化pygame环境
pygame.init()


class Faceu(object):
    # 获取access_token
    def get_access_token(self):
        client_id = 'MSGyseXusqivDfsjknUXco5F'
        client_secret = '2L66OGZXwdGj9yUsjUjjxvi3j3jZ3l5X'
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
        response = requests.get(host)
        # response.add_header('Content-Type', 'application/json; charset=UTF-8')
        content = response.json()
        access_token = content['access_token']
        return access_token

    def open_img(self, img_url):
        # 二进制方式打开图片文件
        f = open(img_url, 'rb')
        img = base64.b64encode(f.read())
        return img

    # 人脸探测,返回数据
    def face_detection(self, img_url):
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
        # headers = {
        #     'Content-Type': 'application/json; charset=UTF-8'
        # }
        img = self.open_img(img_url)
        data = {
            "face_field": "age,gender,beauty",
            "image": img,
            "image_type": "BASE64",
            "max_face_num": 2
        }
        access_token = self.get_access_token()
        params = {
            "access_token": access_token
        }
        response = requests.post(request_url, params=params, data=data)
        content = response.json()
        try:
            if content['result']['face_num'] > 0:
                analytic_dict = {}
                # analytic_dict2 = {}
                # 识别一个人像
                analytic = content['result']['face_list'][0]
                analytic_dict['gender'] = analytic['gender']['type']
                analytic_dict['age'] = analytic['age']
                analytic_dict['beauty'] = analytic['beauty']
                return analytic_dict
        except TypeError:
            analytic_dict1 = {}
            return analytic_dict1
