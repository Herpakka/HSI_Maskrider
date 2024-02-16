import cv2
import numpy as np
from PIL import Image, ImageTk
import os

import beta1_support as control

class process:



    def rgb_to_hsi(img):
        print("Image path =",img)
        # img = Image.open(img)
        image = cv2.imread(img)
        # แปลงภาพจาก RGB เป็น HSI(HSV)
        hsi = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # กำหนดช่วงของ HSI(HSV) ช่วงของ Hue 0-180
        #Saturation เป็น 0-255 = 0-100%
        #Intensity เป็น 0-255 = 0-100%
        lower = np.array([50, 0, 0])
        upper = np.array([70, 255, 255])

        # สร้าง mask สำหรับ hsi
        mask = cv2.inRange(hsi, lower, upper)

        # ตัดภาพเฉพาะส่วน ที่ในช่วงที่กำหนดของ HSI
        cut = cv2.bitwise_or(image, image, mask=mask)

        # สร้างภาพใหม่และแทนที่พิกเซลด้วยสีเขียว
        result = image.copy()
        pixels = np.where(mask != 0)
        result[pixels] = (0, 255, 0)

        # แสดงผลลัพธ์ที่ได้
        # print("ภาพเดิม")
        # cv2.imshow("image",image)
        # print("HSI")
        # cv2.imshow("HSI",hsi)
        # print("Mask")
        # cv2.imshow("Mask",mask)
        # print("ภาพตัด")
        # cv2.imshow("cut",cut)
        # print("ผลลัพธ์")
        # cv2.imshow("result",result)

        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
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

    # # อ่านภาพ
    # image_path = '2023-01-31_13.42.40.png'
    # image = cv2.imread(image_path)

    # # เรียกใช้ฟังก์ชันแปลง RGB เป็น HSI
    # hsi_result = rgb_to_hsi(image)
