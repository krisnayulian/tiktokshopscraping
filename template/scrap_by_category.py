from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction
from utils_category import open_product_v1, driver, up_button

# Setup Connection and prodruct
SESSION = 100
SCROLL_LOOP = 2
CATEGORY = "" #Add Category Product on Tiktok
CONNECTION = "3be6ee120904" # Use Device ID / TCPIP
SERVER_APPIUM_PORT = "4723"
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
driver.swipe(350, 1300, 400, 580, 500) # Adjust with your device
time.sleep(1)


A = 0
while A <= SESSION:
    k = 0
    while k <= SCROLL_LOOP:
        print (f"Scrape the loop at {k}")
        open_product_v1(CATEGORY=CATEGORY)
        time.sleep(2)
        driver.swipe(360, 1300, 360, 400, 500) # Adjust Swipe Product with your device
        k = k + 1
    try: time.sleep(2); up_button()
    except: pass

    time.sleep(2)
    driver.swipe(360, 260, 360, 638, 200) # Refresh Product (Swipe Down on Screen)
    time.sleep(6)
    driver.swipe(360, 1300, 360, 580, 500) # Swipe to Product Layout
    A = A + 1