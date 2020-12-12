from time import time
import cv2 as cv
import numpy as np
import win32con
import win32gui
import win32ui
import ScreenCapture

app_name = '950459: IFCMarkets-Demo - Demo Account - [XAUOIL,H1]'

ScreenCapture.list_window_names()
max_fps = 0
min_fps = 60
wincap = ScreenCapture.WindowCapture(app_name)
cv.namedWindow('Meta Trader', cv.WINDOW_GUI_NORMAL)
while 1:
    st = time()
    screenshot = wincap.get_screenshot()

    










    fps = 1 / (time() - st)
    if fps > max_fps:
        max_fps = fps
    if fps < min_fps:
        min_fps = fps
    print('FPS: {:.2f}, min: {:.2f}, max: {:.2f}'.format(fps, min_fps, max_fps))
    cv.imshow('Meta Trader', screenshot)
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
