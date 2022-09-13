import os
import time
import pyautogui

print(pyautogui.position())
os.startfile('C:\Windows\System32\mspaint.exe')
pyautogui.moveTo(570, 504)
time.sleep(0.5)
pyautogui.dragTo(681, 398)
pyautogui.dragTo(763, 471)
pyautogui.dragTo(800, 504)
pyautogui.dragTo(800, 570)
pyautogui.dragTo(570, 570)
pyautogui.dragTo(570, 504)
pyautogui.dragTo(800, 504)

