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
time.sleep(3)

# login
email = 'vinicius_gnascimento2013@hotmail.com'
password = 'senha123'

pyautogui.click(x=1820, y=410)
pyautogui.write(email)
pyautogui.press('tab')
pyautogui.write(password)
pyautogui.press('tab')
pyautogui.press('enter')
