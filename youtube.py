import webbrowser
import time
import os

url = input("Enter youtube URL:")
refresh = input("Enter refresh time in seconds:")
browser = input("Enter your browser (e.g chrome/firefox")
count= input("How many views you want?")

def openURL():
    os.system("TASKILL /F /IM"+browser+".exe")
    webbrowser.open(url)
    time.sleep(int(refresh))

    for i in range(int(count)):
        print("Webpage has been viewed")
        openURL()


openURL()
    
