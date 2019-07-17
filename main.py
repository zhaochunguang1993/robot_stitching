import cv2
from utils import doAction, getWindowPos, getRectangle, moveFromInitTo
from QRModule.qrdetect import hasQR

totalX = 3
totalY = 3
curX = 0
curY = 0
interest_points = []
directionX = True
windowTitle = 'Outlook'
# windowTitle = 'Motion Controller Programming Software'

def savePos(x, y):
    global interest_points
    interest_points.append((x, y))
    return


def storeImages(l, t, r, b):
    # Initial Position
    # doAction('X0')
    # doAction('Y0')
    _directionX = True

    cap = cv2.VideoCapture(0)

    cap.set(3, 640)
    cap.set(4, 480)

    _curX = l
    _curY = t

    while t <= _curY < b and cap.isOpened():
        print(_curX, _curY)

        # get image
        ret, image = cap.read()
        cv2.imshow('Robot', image)

        file_name = "Images/{}_{}.jpg".format(_curX, _curY)
        cv2.imwrite(file_name, image)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break

        if _directionX is True:
            if _curX+1 < r:
                doAction('X+')
                _curX += 1
            else:
                doAction('Y+')
                _curY += 1
                _directionX = not _directionX
        else:
            if _curX-1 >= 0:
                doAction('X-')
                _curX -= 1
            else:
                doAction('Y+')
                _curY += 1
                _directionX = not _directionX


def perform():
    global curX, curY, totalX, totalY, directionX
    bGetWindow = getWindowPos(windowTitle)
    if not bGetWindow:
        print("---Can't find Control Windows.---")
        return

# Initial Position
    print("---move initial position---")
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
    print("---QR Codes Positions---")
    print(l, t, r, b)

    if l <= r and t <= b:
        print("---move initial position---")
        doAction('X0')
        doAction('Y0')

        print("---move qr position---")
        moveFromInitTo(l, t)

        print("---Image Stitching---")
        # storeImages(l, t, r, b)


if __name__ == '__main__':
    perform()

