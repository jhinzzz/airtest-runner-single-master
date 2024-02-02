import re
import cv2
import numpy as np

def darkAndlight(light_loc,dark_loc):
    # 加载按钮图像
    light_button_image = cv2.imread(light_loc.filepath) # 替换为亮色按钮的图像文件路径
    dark_button_image = cv2.imread(dark_loc.filepath) # 替换为暗色按钮的图像文件路径

    # 转换为灰度图像
    light_button_gray = cv2.cvtColor(light_button_image, cv2.COLOR_BGR2GRAY)
    dark_button_gray = cv2.cvtColor(dark_button_image, cv2.COLOR_BGR2GRAY)

    # 计算图像的颜色直方图
    light_hist = cv2.calcHist([light_button_gray], [0], None, [256], [0, 256])
    dark_hist = cv2.calcHist([dark_button_gray], [0], None, [256], [0, 256])

    # 计算直方图的峰值
    light_peak = np.argmax(light_hist)
    dark_peak = np.argmax(dark_hist)

    # 根据峰值判断按钮颜色
    if light_peak > dark_peak:
        return True
    else:
        return False
