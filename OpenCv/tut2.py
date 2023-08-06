import cv2
import random

img = cv2.imread('mypic.jpg',-1)
img2 = cv2.imread('new_img.jpg',0)
# this will make the image as an numpy array
print(type(img))
print(img.shape)

# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j]= [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

# Copying an image in other image

tag = img[500:700,400:700]
img[100:300,300:600] = tag

img3 = cv2.cvtColor(img2,cv2.COLOR_GRAY2RGB)

cv2.imshow('image',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()