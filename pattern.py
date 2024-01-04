import cv2
import time
import keyboard
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

button_GPIO = 23

def button_with_image(image, input):
    #if GPIO.input(input) == False:
    if keyboard.is_pressed(input):
        cv2.imshow('merlins', image)
        cv2.waitKey(1)
        time.sleep(1)
        current_sequence.append(input)
        if current_sequence[-1] != correct_sequence[len(current_sequence)-1]:
            return False

merlist = []

merlist.append(cv2.resize(cv2.imread('images/Picture1.jpg'), (1080,1080)))
merlist.append(cv2.resize(cv2.imread('images/Picture2.jpg'), (1080,1080)))
merlist.append(cv2.resize(cv2.imread('images/Picture3.png'), (1080,1080)))
merlist.append(cv2.resize(cv2.imread('images/Picture4.png'), (1080,1080)))
merlist.append(cv2.resize(cv2.imread('images/Picture5.jpg'), (1080,1080)))
merlist.append(cv2.resize(cv2.imread('images/Picture6.jpg'), (1080,1080)))
merlist.append(cv2.resize(cv2.imread('images/Picture7.jpg'), (1080,1080)))
merlist.append(cv2.resize(cv2.imread('images/Picture8.jpg'), (1080,1080)))
merlist.append(cv2.resize(cv2.imread('images/Picture9.jpg'), (1080,1080))) 

correct_sequence = ['1','2','3','4','5','6','7','8','9']

current_sequence = []

buttons = ['1','2','3','4','5','6','7','8','9']

cv2.namedWindow('merlins', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('merlins',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

while True:

    cv2.imshow('merlins', cv2.resize(cv2.imread('images/black'), (1080,1080)))
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