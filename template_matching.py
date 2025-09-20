import cv2
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy

img_original = cv2.imread('./template_matching_original.jpg')
img_rgb = deepcopy(img_original)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template_matching_tem.jpg',cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

res =cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    
# Output
cv2.imshow('original', img_original)
cv2.imshow('result', img_rgb)
cv2.waitKey(0)