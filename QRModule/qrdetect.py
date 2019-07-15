from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

def decode(im):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')
    return decodedObjects


# Display barcode and QR code location
def display(im, decodedObjects):
    # Loop over all decoded objects
    for decodedObject in decodedObjects:
        points = decodedObject.polygon
        # If the points do not form a quad, find convex hull
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points
        # Number of points in the convex hull
        n = len(hull)
        # Draw the convext hull
        for j in range(0, n):
            cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)
    # Display results
    # cv2.imshow("Results", im);
    # cv2.waitKey(0);
    return im

# # Main
# if __name__ == '__main__':
#     im = cv2.imread('ttt.png')
#     decodedObjects = decode(im)
#     print(decodedObjects)
#     # img = display(im, decodedObjects)
#     # plt.imshow(img, cmap = 'gray')


def hasQR(image):
    im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    decodedObjects = decode(im)
    ret = False
    print(decodedObjects)
    for decodedObject in decodedObjects:
        if decodedObject.type == 'QRCODE':
            ret = True
        points = decodedObject.polygon
        # If the points do not form a quad, find convex hull
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points
        # Number of points in the convex hull
        n = len(hull)
        # Draw the convext hull
        for j in range(0, n):
            cv2.line(image, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

    return ret, image

