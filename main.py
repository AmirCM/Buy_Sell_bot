from time import time
import cv2 as cv
import numpy as np
import win32con
import win32gui
import win32ui
from PIL import ImageGrab


def take_screen():
    w = 1920
    h = 1080
    # hwnd = win32gui.FindWindow(None, windowname)
    hwnd = None

    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)

    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    return img


max_fps = 0
min_fps = 60
while True:
    st = time()
    screenshot = take_screen()
    fps = 1 / (time() - st)
    if fps > max_fps:
        max_fps = fps
    if fps < min_fps:
        min_fps = fps
    print('FPS: {:.2f}, min: {:.2f}, max: {:.2f}'.format(fps, min_fps, max_fps))
    cv.imshow('CSV', screenshot)
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
