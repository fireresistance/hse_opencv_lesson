import cv2
from utils import viewImage

image = cv2.imread("3.jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, threshold_image = cv2.threshold(gray_image, 127, 255, 0)
viewImage(gray_image, "grayscale_dog")
viewImage(threshold_image, "threshold_dog")