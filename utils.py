import time
import win32gui
import pyautogui

hWnd = 0
windowPos = (0, 0)
btnInitX = (307, 162)
btnInitY = (307, 210)
btnXP = (250, 162)
btnXM = (192, 162)
btnYP = (250, 210)
btnYM = (192, 210)


def getWindowPos(title_text):
    global hWnd, windowPos
    _hwnd = _get_windows_bytitle(title_text, False)
    print(_hwnd)
    if len(_hwnd) == 0:
        return False

    l, t, r, b = win32gui.GetWindowRect(_hwnd[0])
    hWnd = _hwnd[0]
    windowPos = (l, t)
    print("windowPos - {}".format(windowPos))
    return True


def _get_windows_bytitle(title_text, exact=True):
    def _window_callback(hwnd, all_windows):
        title = win32gui.GetWindowText(hwnd)
        all_windows.append((hwnd, title))
    windows = []
    win32gui.EnumWindows(_window_callback, windows)
    if exact:
        return [hwnd for hwnd, title in windows if title_text == title]
    else:
        return [hwnd for hwnd, title in windows if title_text in title]


def click_real_button(type):
    global windowPos
    win32gui.SetForegroundWindow(hWnd)
    pyautogui.FAILSAFE = False
    x = 0
    y = 0
    if type == 'X0':
        x = windowPos[0] + btnInitX[0]
        y = windowPos[1] + btnInitX[1]
    elif type == 'Y0':
        x = windowPos[0] + btnInitY[0]
        y = windowPos[1] + btnInitY[1]
    elif type == 'X+':
        x = windowPos[0] + btnXP[0]
        y = windowPos[1] + btnXP[1]
    elif type == 'X-':
        x = windowPos[0] + btnXM[0]
        y = windowPos[1] + btnXM[1]
    elif type == 'Y+':
        x = windowPos[0] + btnYP[0]
        y = windowPos[1] + btnYP[1]
    elif type == 'Y-':
        x = windowPos[0] + btnYM[0]
        y = windowPos[1] + btnYM[1]

    pyautogui.moveTo(x, y)
    pyautogui.click(interval=0.15)

    return


###
#
# type
#     X0: init x
#     Y0: init y
#     X+: step x+
#     X-: step x-
#     Y+: step y+
#     Y-: step y-
#
###

def doAction(type, sleep=0.5):
    click_real_button(type)
    delay(sleep)
    return


def delay(t):
    time.sleep(t)
    return


def moveFromInitTo(targetX, targetY):
    for x in range(targetX):
        doAction('X+')

    for y in range(targetY):
        doAction('Y+')


def getRectangle(points):
    l = 10000
    t = 10000
    r = 0
    b = 0
    for point in points:
        if point[0] < l:
            l = point[0]
        if point[0] > r:
            r = point[0]
        if point[1] < t:
            t = point[1]
        if point[1] > b:
            b = point[1]

    return l, t, r, b


