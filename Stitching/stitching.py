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


def _subStitching(images, group_cnt=5):
    stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()

    g_cnt = group_cnt
    res_images = []
    sub_images = []
    cnt = 0
    for im in images:
        cnt += 1
        sub_images.append(im)
        if cnt % g_cnt == 0 or cnt >= len(images):
            (status, stitched) = stitcher.stitch(sub_images)
            if status == 0:
                res_images.append(stitched)
            sub_images = []

    (status, stitched) = stitcher.stitch(res_images)
    return stitched


def Stitching(l, t, r, b):
    images_final = []
    for y in range(t, b):
        images = []
        for x in range(l, r):
            imagePath = path + '{:02d}_{:02d}.jpg'.format(y, x)
            im = cv2.imread(imagePath)
            images.append(im)
        im = _subStitching(images, 7)
        images_final.append(im)

    (status, result_img) = _subStitching(images_final)
    if status == 0:
        cv2.imwrite('result_final.jpg', result_img)
        cv2.imshow("Stitched", result_img)


Stitching(0, 0, 19, 18)