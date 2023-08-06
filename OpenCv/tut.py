import cv2

img = cv2.imread('mypic.jpg',0)
# -1 => for color
# 0 => for grayscale
# 1 => for no change
# this will make the image size to 400px
img = cv2.resize(img,(300,300))
# this will reduce the image size to half
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
# now we can save the changed image by
cv2.imwrite('new_img.jpg',img)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()