import pyautogui;
import time;

pyautogui.PAUSE = 0.3

# Open the Chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)

# Accessing the website
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.hotkey('Ctrl', 'l')
pyautogui.write(link)
pyautogui.press('enter')