import cv2
from utils import doAction, getWindowPos, getRectangle, moveFromInitTo
from QRModule.qrdetect import hasQR

totalX = 3
totalY = 3
curX = 0
curY = 0
interest_points = []
directionX = True
windowTitle = 'Motion Controller Programming Software'

def savePos(x, y):
    global interest_points
    interest_points.append((x, y))
    return


def imageStitching(l, t, r, b):
    global curX, curY, totalX, totalY, directionX
    # getWindowPos('Chrome')

    # Initial Position
    doAction('X0')
    doAction('Y0')
    cap = cv2.VideoCapture(0)

    cap.set(3, 640)
    cap.set(4, 480)

    curX = l
    curY = t
    while t <= curY < b and cap.isOpened():
        print(curX, curY)

        # get image
        ret, image = cap.read()

        cv2.imshow('Robot', image)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break



def perform():
    global curX, curY, totalX, totalY, directionX
    getWindowPos(windowTitle)

# Initial Position
    doAction('X0')
    doAction('Y0')

# Capture Camera
    cap = cv2.VideoCapture(0)

    cap.set(3, 640)
    cap.set(4, 480)

    while curY < totalY and cap.isOpened():
        print(curX, curY)

        # get image
        ret, image = cap.read()

        cv2.imshow('Robot', image)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break

        haveQRCode, image = hasQR(image)

        if haveQRCode:
            savePos(curX, curY)

        if directionX is True:
            if curX+1 < totalX:
                doAction('X+')
                curX += 1
            else:
                doAction('Y+')
                curY += 1
                directionX = not directionX
        else:
            if curX-1 >= 0:
                doAction('X-')
                curX -= 1
            else:
                doAction('Y+')
                curY += 1
                directionX = not directionX

    l, t, r, b = getRectangle(interest_points)
    imageStitching(l, t, r, b)


if __name__ == '__main__':
    perform()

