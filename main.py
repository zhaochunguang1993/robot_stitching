import cv2
from utils import doAction, getWindowPos, getRectangle, moveFromInitTo, moveInitPos, delay
from QRModule.qrdetect import hasQR

totalX = 3
totalY = 3
interest_points = []

windowTitle = 'Outlook'
# windowTitle = 'Motion Controller Programming Software'

def savePos(x, y):
    global interest_points
    interest_points.append((x, y))
    return


def storeImages(l, t, r, b):
    _directionX = True

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    _curX = l
    _curY = t
    while t <= _curY <= b and cap.isOpened():
        print(_curX, _curY)

        # get image
        ret, image = cap.read()

        file_name = "Output/{:02d}_{:02d}.jpg".format(_curY, _curX)
        cv2.imwrite(file_name, image)

        cv2.imshow('Robot', image)
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

        delay(1)


def performScan():
    global totalX, totalY
    directionX = True
    bGetWindow = getWindowPos(windowTitle)
    if not bGetWindow:
        print("---Can't find Control Windows.---")
        return

# Initial Position
    print("---Move initial position---")
    moveInitPos()
    curX = 0
    curY = 0

    # Capture Camera
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

# Scan All Region and Get position.
    print("---Scan all region---")
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
        delay(1)

# Get Region.
    l, t, r, b = getRectangle(interest_points)

    if l <= r and t <= b:
        print("---QR Codes Region---")
        print(l, t, r, b)

        print("---Move initial position---")
        moveInitPos()

        print("---Move qr position ({}, {})---".format(l, t))
        moveFromInitTo(l, t)

        print("---Get Images For Stitching---")
        storeImages(l, t, r, b)
    else:
        print("---Can't get QR Codes Region---")


if __name__ == '__main__':
    performScan()

