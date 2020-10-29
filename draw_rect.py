import cv2
from utils import viewImage

image = cv2.imread("3.jpeg")
output = image.copy()
cv2.rectangle(output, (200, 250), (500, 450), (0, 255, 255), 10)
viewImage(output, "rect")