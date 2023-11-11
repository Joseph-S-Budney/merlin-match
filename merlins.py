import cv2
import time
import keyboard
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)

#button_GPIO = 23

#GPIO.setup(button_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

merlist = []

merlist.append(cv2.imread('images/Picture1.jpg'))
merlist.append(cv2.imread('images/Picture2.jpg'))
merlist.append(cv2.imread('images/Picture3.png'))
merlist.append(cv2.imread('images/Picture4.png'))
merlist.append(cv2.imread('images/Picture5.jpg'))
merlist.append(cv2.imread('images/Picture6.jpg'))
merlist.append(cv2.imread('images/Picture7.jpg'))
merlist.append(cv2.imread('images/Picture8.jpg'))
merlist.append(cv2.imread('images/Picture9.jpg')) 


wait_time = 0

cv2.namedWindow('merlins', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('merlins',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

while True:

    cv2.imshow('merlins', cv2.imread('images/black'))


    cv2.waitKey(0)

    if keyboard.is_pressed('esc'):
        cv2.destroyAllWindows()
        break
    
    #if GPIO.input(button_GPIO) == False:
    for merlin in merlist:
        start = time.time()
        cv2.imshow('merlins', merlin)
        cv2.waitKey(1)
        time.sleep(1)
        # while wait_time <= 1:
        #     wait_time = time.time()-start
        # wait_time = 0
        
