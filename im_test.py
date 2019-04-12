# coding:utf-8
# cv2库测试：图片读取、显示
"""
多行注释 测试
"""

import cv2 as cv #导入OpenCV2库，并以cv命名

im = cv.imread('test.jpg')
# cv.nameWindow('test')		# 打开窗口命令【此句可省】
cv.imshow('test',im)	# ''里是窗口名，可以不填

# ————若没有此句：图片一闪而过，且窗口一直无响应————
cv.waitKey(0) #cv.waitKey(1000) # 

# ————释放窗口是个好习惯————
#cv.destroyALLWindows() # cv.destroyWindow('test')
