# import cv2
import time

totalX = 5
totalY = 10
curX = 0
curY = 0

interest_points = []
directionX = True
###
#
# type
#     0: init x
#     1: init y
#     2: step x+
#     3: step x-
#     4: step y+
#     5: step y-
###

def hasQR(image):
    return True


def click_real_button(type):
    return


def doAction(type, sleep=0.5):

    delay(sleep)
    return


def delay(t):
    time.sleep(t)
    return


def savePos(x, y):
    interest_points.append((x, y))
    return


doAction('X0')
doAction('Y0')
while curY < totalY:
    print(curX, curY)

    # get image
    image = None
    if hasQR(image):
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