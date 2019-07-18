from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import os

path = '../output/'

def rename_files():
    path = '../output/'
    file_list = os.listdir(path)
    for afile in file_list:
        filename, file_extension = os.path.splitext(afile)
        t = filename.split('_')
        f = '{:02d}_{:02d}.jpg'.format(int(t[0]), int(t[1]))
        os.rename(path + "/" + afile, path + "/" + f)


def Stitching(l, t, r, b):
    images_final = []
    stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
    for y in range(t, b):
        print(y)
        images = []
        images_mid = []
        group_no = 0
        cnt = 0
        group_cnt = 7
        for x in range(l, r):
            print(cnt)
            print('----- group ', group_no)
            if cnt > group_cnt or group_cnt * group_no + cnt > r - l + 1:
                (status, stitched) = stitcher.stitch(images)
                if status == 0:
                    images_mid.append(stitched)


                cnt = 0
                group_no += 1
                images = []
            else:
                imagePath = path + '{:02d}_{:02d}.jpg'.format(y, x)
                image = cv2.imread(imagePath)
                images.append(image)
                cnt += 1

        (status, stitched) = stitcher.stitch(images_mid)
        if status == 0:
            cv2.imwrite('result_{}.jpg'.format(y), stitched)
            cv2.imshow("Stitched", stitched)
            cv2.waitKey(10)
            images_final.append(stitched)

    images = []
    images_mid = []
    group_no = 0
    cnt = 0
    group_cnt = 5
    for image in images_final:
        images.append(image)
        cnt += 1
        if cnt >= group_cnt or group_cnt * group_no + cnt >= b - t + 1:
            (status, stitched) = stitcher.stitch(images)
            if status == 0:
                images_mid.append(stitched)

            cnt = 0
            group_no += 1
            images = []

    (status, stitched) = stitcher.stitch(images_mid)
    if status == 0:
        cv2.imwrite('result_final.jpg', stitched)
        cv2.imshow("Stitched", stitched)

Stitching(0, 0, 19, 18)
