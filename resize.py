# -*- coding: utf-8 -*-
import cv2
from utils import viewImage


img = cv2.imread("1.jpeg")
shape = img.shape
cropped = img[50:250, 10:310]

scale_percent = 20 # Процент от изначального размера
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
viewImage(resized, "20% resized")

resized = cv2.resize(img, (512, 512), interpolation = cv2.INTER_CUBIC)
viewImage(resized, "512x512 resized")