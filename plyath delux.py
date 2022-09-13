import pyautogui
import time

print(pyautogui.position())
pyautogui.moveTo(1690, 575)
pyautogui.click(button = "right")
pyautogui.moveTo(1461, 870)
time.sleep(0.6)
pyautogui.moveTo(1150, 1000)
pyautogui.click()
pyautogui.moveTo(1690, 575)
pyautogui.doubleClick()
time.sleep(2)
pyautogui.write('Zubnoj v 8:00')