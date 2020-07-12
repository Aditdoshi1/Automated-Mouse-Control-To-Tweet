import time
import pyautogui

##Location of chrome icon
pyautogui.click(651, 1048, duration = 1)
##Location of the URL bar
pyautogui.click(271, 59, duration = 1)
pyautogui.typewrite("www.twitter.com")
pyautogui.click(1340, 124, duration = 1)
time.sleep(6)
##Location of the Sign-in button
pyautogui.click(1340, 124, duration = 1)
##Location of the Email-id button
pyautogui.click(762, 312, duration = 1)
##input your Email-id inside the parenthesis
pyautogui.typewrite("aditdoshi02@gmail.com")
##Location of the Password Button
pyautogui.click(691, 417, duration = 1)
##input your Password inside the parenthesis
pyautogui.typewrite("12345678")
##Location of the Login Button
pyautogui.click(932, 491, duration = 1)
time.sleep(6)
##Location of the Tweet Button
pyautogui.click(294, 741, duration = 1)
##Location where you need to type your tweet
pyautogui.click(805, 248, duration = 1)
##Change your Tweet Content here
pyautogui.typewrite("Test Successful")
##Location of the Post Button
pyautogui.click(1264, 473, duration = 1)