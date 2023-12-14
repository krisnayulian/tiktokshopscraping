from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction
from utils_category2 import open_product_v2, driver, close_dialog, up_button, back_button

# Setup Connection and prodruct
SESSION = 100
SCROLL_LOOP = 2
CATEGORY ="office"
CONNECTION = "192.168.0.101:5555" # 3be6ee120904/ 192.168.0.106:5555
SERVER_APPIUM_PORT = "4724"
SERVER_APPIUM_IP = "127.0.0.1"

DESIRED_CAPS = {
    "platformName": "Android",
    "appium:deviceName": "device",
    "appium:udid": CONNECTION,
    "appium:noReset": True,
}

driver = driver(SERVER_APPIUM_IP=SERVER_APPIUM_IP, SERVER_APPIUM_PORT=SERVER_APPIUM_PORT, desired_caps=DESIRED_CAPS)

### Scroll To Product Layout
time.sleep(1)
driver.swipe(538, 1750, 538, 450, 500) # Adjust with your device
time.sleep(1)


A = 0
while A <= SESSION:
    k = 0
    while k <= SCROLL_LOOP:
        print (f"Scrape the loop at {k}")
        open_product_v2(CATEGORY=CATEGORY)
        time.sleep(2)
        driver.swipe(538, 1750, 538, 500, 500) # defautl 360, 1300, 360, 400, 400 Adjust with your device
        k = k + 1
    try: time.sleep(2); up_button()
    except: pass

    time.sleep(2)
    driver.swipe(538, 210, 538, 860, 200) # Adjust with your device
    time.sleep(6)
    driver.swipe(538, 1750, 538, 450, 500) # Adjust with your device
    A = A + 1