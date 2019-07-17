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

x_rate = 184 / 640
y_rate = 194 / 480
path = '../Images/'

img_ylist = []


def stitching(r, t, l, b):
    output = cv2.imread(path + '0_0.jpg')
    h, w = output.shape[:2]
    add_w = int(w * x_rate)
    add_h = int(h * y_rate)
    for y in range(t, b):
        output = cv2.imread(path + '{}_0.jpg'.format(y))
        for x in range(r+1, l):
            _h, _w = output.shape[:2]
            temp = np.zeros((h, _w + add_w, 3), np.uint8)

            im = cv2.imread(path + '{}_{}.jpg'.format(y, x))
            im_add = im[:h, w-add_w:w]

            temp[0:h, 0:_w] = output
            temp[:h, _w:_w+add_w] = im_add
            output = temp.copy()
            img_ylist.append(output)
        cv2.imshow("test", output)
        cv2.waitKey(0)
        cv2.imwrite("output_{}.jpg".format(y), output)

    output = cv2.imread('output_{}.jpg'.format(t))
    h, w = output.shape[:2]
    for y in range(t+1, b+1):
        print(y)
        _h, _w = output.shape[:2]
        temp = np.zeros((_h + add_h, w, 3), np.uint8)

        im = cv2.imread('output_{}.jpg'.format(y))
        im_add = im[0:add_h, :w]


        temp[0: add_h, 0:w] = im_add
        temp[add_h:add_h + _h, 0:w] = output
        output = temp.copy()

    cv2.imshow("test", output)
    cv2.waitKey(0)
    cv2.imwrite("result.jpg", output)

stitching(0, 0, 8, 8)

