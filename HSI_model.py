import cv2
import numpy as np
from PIL import Image, ImageTk
import os

import beta1_support as control

image = None
result = None
h,w = 0,0
class process:
    def rgb_to_hsi(img):
        global result,image
        H1 = int((control.h)/2)
        H2 = int((control.h2)/2)
        sat1 = int(float(control.s)*255)
        sat2 = int(float(control.s2)*255)
        inten1 = int(control.v)
        inten2 = int(control.v2)
        print("Image path =",img)
        # img = Image.open(img)
        image = cv2.imread(img)
        # แปลงภาพจาก RGB เป็น HSI(HSV)
        hsi = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        #HSI(HSV) ช่วงของ Hue 0-180
        #Saturation เป็น 0-255 = 0-100%
        #Intensity เป็น 0-255 = 0-100%
        lower = np.array([H1, sat1, inten1])
        upper = np.array([H2, sat2, inten2])
        print("lower :",lower,"upper :",upper)

        # สร้าง mask สำหรับ hsi
        mask = cv2.inRange(hsi, lower, upper)

        # ตัดภาพเฉพาะส่วน ที่ในช่วงที่กำหนดของ HSI
        cut = cv2.bitwise_or(image, image, mask=mask)

        # สร้างภาพใหม่และแทนที่พิกเซลด้วยสีเขียว
        result = image.copy()
        result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        pixels = np.where(mask != 0)
        result[pixels] = (0, 255, 0)

        print("size = ",result.shape)
        return result
    def get_relative_path(file_path):
        # Get the current working directory
        current_directory = os.getcwd()

        # Get the absolute path of the file
        absolute_path = os.path.abspath(file_path)

        # Get the relative path
        relative_path = os.path.relpath(absolute_path, current_directory)

        return relative_path
    def get_shape():
        global h,w
        h = int(result.shape[0])
        w = int(result.shape[1])
        print ("h = ",h,"w = ",w)
        return h, w
    def display_mask(img):
        H1 = int((control.h)/2)
        H2 = int((control.h2)/2)
        sat1 = int(float(control.s)*255)
        sat2 = int(float(control.s2)*255)
        inten1 = int(control.v)
        inten2 = int(control.v2)
        print("Image path =",img)
        # img = Image.open(img)
        image = cv2.imread(img)
        # แปลงภาพจาก RGB เป็น HSI(HSV)
        hsi = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        #HSI(HSV) ช่วงของ Hue 0-180
        #Saturation เป็น 0-255 = 0-100%
        #Intensity เป็น 0-255 = 0-100%
        lower = np.array([H1, sat1, inten1])
        upper = np.array([H2, sat2, inten2])
        print("lower :",lower,"upper :",upper)

        # สร้าง mask สำหรับ hsi
        mask = cv2.inRange(hsi, lower, upper)

        # ตัดภาพเฉพาะส่วน ที่ในช่วงที่กำหนดของ HSI
        cut = cv2.bitwise_or(image, image, mask=mask)

        # สร้างภาพใหม่และแทนที่พิกเซลด้วยสีเขียว
        result = image.copy()
        result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        pixels = np.where(mask != 0)
        result[pixels] = (0, 255, 0)

        print("size = ",result.shape)
        return result

    # # อ่านภาพ
    # image_path = '2023-01-31_13.42.40.png'
    # image = cv2.imread(image_path)

    # # เรียกใช้ฟังก์ชันแปลง RGB เป็น HSI
    # hsi_result = rgb_to_hsi(image)
