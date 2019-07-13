import cv2
import sys
import numpy as np

filename = [
            'image_data/1.jpg',
            'image_data/2.jpg',
            'image_data/3.jpg',
            'image_data/4.jpg',
            'image_data/5.jpg',
            'image_data/6.jpg',
            'image_data/7.jpg',
            'image_data/8.jpg',
            'image_data/9.jpg',
            'image_data/10.jpg',
            'image_data/11.jpg',
            ]

rate = 1/4.6

output = cv2.imread(filename[0])
h, w = output.shape[:2]
add_w = int(w*rate)

for file in filename[1:]:
    _h, _w = output.shape[:2]
    temp = np.zeros((h, _w + add_w, 3), np.uint8)

    im = cv2.imread(file)
    im_add = im[:h, w-add_w:w]

    temp[0:h, 0:_w] = output
    temp[:h, _w:_w+add_w] = im_add
    output = temp.copy()

cv2.imshow("test", output)
cv2.waitKey(0)
cv2.imwrite("output.jpg", output)

