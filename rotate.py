import cv2
from utils import viewImage

image = cv2.imread("1.jpeg")
(h, w, d) = image.shape
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
viewImage(rotated, "warpaffine")

rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
viewImage(rotated, "rotated")