import cv2

img = cv2.imread('image.jpg');
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('image_gray.jpg',img_gray);
