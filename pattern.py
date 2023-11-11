import cv2
import time
import keyboard
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)

#button_GPIO = 23

# def wait(seconds): 
#     wait_time = 0
#     start = time.time()
#     while wait_time <= seconds:
#         wait_time = time.time()-start

def button_with_image(image, input):
    if keyboard.is_pressed(input): # change to rpi button
    #if GPIO.input(input) == False:
        cv2.imshow('merlins', image)
        cv2.waitKey(1)
        #wait(1) # this function call can change how long the pictures are shown for
        time.sleep(1)
        current_sequence.append(input)
        if current_sequence[-1] != correct_sequence[len(current_sequence)-1]:
            return False

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

correct_sequence = ['1','2','3','4','5','6','7','8','9']

current_sequence = []

buttons = ['1','2','3','4','5','6','7','8','9']

cv2.namedWindow('merlins', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('merlins',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

while True:

    cv2.imshow('merlins', cv2.imread('images/black'))
    cv2.waitKey(1)

    for x in range(len(buttons)):
        if button_with_image(merlist[x], buttons[x]) == False:
            current_sequence = []

    if current_sequence == correct_sequence:
        print("win")
        cv2.destroyAllWindows
        break

    if keyboard.is_pressed('esc'):
        cv2.destroyAllWindows
        break