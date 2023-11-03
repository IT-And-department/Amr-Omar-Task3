# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread("C:/Users/amr/OneDrive/Desktop/task/ppp.jpg",0)

S = []

rows =img.shape[0]
columns = img.shape[1]

for r in range(rows):
    for c in range(columns):
        S.append(np.binary_repr(img[r,c],width=8))
        
bit_1_img = (np.array([int(i[7])for i in S],dtype=np.uint8)*1).reshape(rows,columns)
bit_2_img = (np.array([int(i[6])for i in S],dtype=np.uint8)*2).reshape(rows,columns)
bit_3_img = (np.array([int(i[5])for i in S],dtype=np.uint8)*4).reshape(rows,columns)
bit_4_img = (np.array([int(i[4])for i in S],dtype=np.uint8)*8).reshape(rows,columns)

bit_5_img = (np.array([int(i[3])for i in S],dtype=np.uint8)*16).reshape(rows,columns)
bit_6_img = (np.array([int(i[2])for i in S],dtype=np.uint8)*32).reshape(rows,columns)
bit_7_img = (np.array([int(i[1])for i in S],dtype=np.uint8)*64).reshape(rows,columns)
bit_8_img = (np.array([int(i[0])for i in S],dtype=np.uint8)*128).reshape(rows,columns)

l1 = cv2.hconcat([bit_1_img,bit_2_img,bit_3_img,bit_4_img])
l2 = cv2.hconcat([bit_5_img,bit_6_img,bit_7_img,bit_8_img])
f = cv2.vconcat([l1,l2])
#cv2.imshow("BFS", f)
#cv2.waitkey(0)

sum = bit_5_img+bit_6_img+bit_7_img+bit_8_img
cv2.imshow("sum", sum)
cv2.waitKey(0)

