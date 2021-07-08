import pyautogui, time

pyautogui.hotkey('ctrl','alt','t')
time.sleep(5)
pyautogui.write('sudo apt-get update -y && sudo apt-get upgrade -y')
pyautogui.hotkey('enter')
#time.sleep(3)
pyautogui.write('c4zNt9ex2',interval=0.25)
pyautogui.hotkey('enter')


