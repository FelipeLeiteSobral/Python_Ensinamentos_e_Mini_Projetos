# Bot no computador - pyautogui
import pyautogui
import time
pyautogui.PAUSE = 2
# abrir a ferramenta, sistema ou programa
pyautogui.press("win")
pyautogui.write("login.xlsx")
pyautogui.press("backspace")
pyautogui.press("enter")

#descobrir onde se deve clicar
time.sleep(3)
pyautogui.position()

# Bot na Internet - Selenium
# web driver (chromedriver) coloca esse arquivo na pasta onde está o python.exe
