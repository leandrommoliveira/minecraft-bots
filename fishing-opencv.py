import cv2 as cv
import numpy as np 
import pyautogui
from pynput.keyboard import Key, Controller
import time

def take_screenshot_minor():
    myScreenshot = pyautogui.screenshot()
    myScreenshot = myScreenshot.resize((1024,768))
    myScreenshot.save(r'screenshot.png')

def search_in_image(image_to_search, haystack):
    haystack_img = cv.imread(image_to_search, cv.IMREAD_UNCHANGED)
    need_img = cv.imread(haystack, cv.IMREAD_UNCHANGED)

    result = cv.matchTemplate(haystack_img, need_img, cv.TM_CCOEFF_NORMED)
    return cv.minMaxLoc(result)

print('Aguardando tempo de delay....')

time.sleep(10)

print('Starting comands now....')

while True:
    pyautogui.click(button='right')
    time.sleep(1.5)

    take_screenshot_minor()
    min_val, max_val, min_loc, max_loc = search_in_image('screenshot.png', 'isca-cortada.png')
    print("#################")
    print(max_loc)
    print("#################")

    location = max_loc

    while True:
        take_screenshot_minor()
        min_val, max_val, min_loc, max_loc = search_in_image('screenshot.png', 'isca-cortada.png')
        
        print(max_loc[0])


        if location[0]+10 < max_loc[0] or location[0]-10 > max_loc[0]:
            break

    pyautogui.click(button='right')
    time.sleep(2)
