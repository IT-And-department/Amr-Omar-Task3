import cv2
import numpy as np

img = cv2.imread("C:/Users/amr/OneDrive/Desktop/task/splash.png", 0)


S =np.array(img)
rows,columns =img.shape
print(rows,columns)
start = 100
end = 200
new_value = 255

for r in range(rows):
    for c in range(columns):
        if(img[r,c] >= start and img[r,c] <= end):
            S[r,c] = new_value
           
cv2.imshow("Original", img)
cv2.imshow("Gray Level Slicing",S)
cv2.waitKey(0)  