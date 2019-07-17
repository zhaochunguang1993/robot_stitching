# -*- coding: utf-8 -*-
"""
Created on Tue Oct 7 11:41:42 2018

@author: Caihao.Cui
"""
from __future__ import print_function

import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time

def decode(im) :
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data,'\n')     
    return decodedObjects


font = cv2.FONT_HERSHEY_SIMPLEX

frame = cv2.imread("test.png")
# Our operations on the frame come here
im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

decodedObjects = decode(im)

for decodedObject in decodedObjects:
    points = decodedObject.polygon

    # If the points do not form a quad, find convex hull
    if len(points) > 4 :
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else :
      hull = points;

    # Number of points in the convex hull
    n = len(hull)
    # Draw the convext hull
    for j in range(0,n):
      cv2.line(frame, hull[j], hull[ (j+1) % n], (255,0,0), 3)

    x = decodedObject.rect.left
    y = decodedObject.rect.top

    print(x, y)

    print('Type : ', decodedObject.type)
    print('Data : ', decodedObject.data,'\n')

    barCode = str(decodedObject.data)
    cv2.putText(frame, barCode, (x, y), font, 1, (0,255,255), 2, cv2.LINE_AA)


cv2.imshow('test', frame)
cv2.waitKey(0)