# Automated-Mouse-Control-To-Tweet
A simple Project to open chrome, and to open twitter, login with the credentials and post a tweet on its own. Done using Keyboard and Mouse automation libraries.
It is done for a 1920x1080 display (you have to change the co-ordinates for different display size)
The co-ordinates need to be changed for the chrome location in taskbar(in my case the location was x= 651, y = 1048), You can easily find the accurate location using pyautogui.position() function.
Do no remove time.sleep to make it look magical, because loading website takes some time, and if the mouse if clicked before the loading is completed, it wont register the click and the  further clicks will be misplaced.
