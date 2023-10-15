import cv2
import time

merlin_1 = cv2.imread('images/merlin-mouse')
merlin_2 = cv2.imread('images/tv-merlin')
merlin_3 = cv2.imread('images/merlin-shrek')
black = cv2.imread('images/black')

merlist = [merlin_1, merlin_2, merlin_3]

wait_time = 0

cv2.namedWindow('merlins', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('merlins',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

while True:

    cv2.imshow('merlins', black)

    cv2.waitKey(0)

    for merlin in merlist:
        start = time.time()
        cv2.imshow('merlins', merlin)
        cv2.waitKey(1)
        while wait_time <= 2:
            wait_time = time.time()-start
        wait_time = 0
