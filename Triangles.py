import pyautogui  
import time 
import math
import random

list1 = [1137, 70, 1131, 98, 1106, 73, 1104, 100, 1079, 70, 1045, 98, 997, 78]
l = 200
hypotenuse = l
i = 0
a = 10
b = 400

pyautogui.hotkey("Alt", "Tab")
#pyautogui.typewrite("Paint")
#pyautogui.press("Enter")
time.sleep(0.5)
pyautogui.moveTo(730, 80, 0.2)
pyautogui.click()
time.sleep(0.2)
pyautogui.move(0, 250, 0.2)
pyautogui.click()
time.sleep(1)

def default_triangle():
    pyautogui.moveTo(x_c, y_c)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(a, b)
    pyautogui.drag(l,0)
    p = hypotenuse * math.sin(math.pi/3)
    q = hypotenuse * math.cos(math.pi/3)
    pyautogui.drag(-q,-p)
    pyautogui.drag(-q, p)

def inverted_traingle():
    pyautogui.moveTo(x_c, y_c)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(a, b)
    pyautogui.drag(l,0)
    p = hypotenuse * math.sin(math.pi/3)
    q = hypotenuse * math.cos(math.pi/3)
    pyautogui.drag(-q,p)
    pyautogui.drag(-q,-p)

while True:
    i = i + 1
    if i == 69:
        break 
    if i == 1:
        a = 10
        b = 400 
        j = random.randint(0,13)
        if j % 2 == 0: 
            x_c = list1[j]
            y_c = list1[j + 1]
            default_triangle()
        else:
            x_c = list1[j - 1]
            y_c = list1[j]
            default_triangle()

    elif i % 2 !=0:
        a = a + hypotenuse * math.cos(math.pi/3)
        b = b + hypotenuse * math.sin(math.pi/3)
        if i % 35 == 0:
            a = 10 
            b = b + hypotenuse * math.sin(math.pi/3)
        j = random.randint(0,13)
        if j % 2 == 0: 
            x_c = list1[j]
            y_c = list1[j + 1]
            default_triangle()
        else:
            x_c = list1[j - 1]
            y_c = list1[j]
            default_triangle()

    else:
        b = b - hypotenuse * math.sin(math.pi/3)
        a = a + hypotenuse * math.cos(math.pi/3)
        if i == 18:
            a = 10 
            b = 400
        if i == 52:
            a = 10
            b = b + hypotenuse * math.sin(math.pi/3)
        j = random.randint(0,13)
        if j % 2 == 0: 
            x_c = list1[j]
            y_c = list1[j + 1]
            inverted_traingle()
        else:
            x_c = list1[j - 1]
            y_c = list1[j]
            inverted_traingle()
    print(i)
