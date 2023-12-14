from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction
from utils_keyword import open_product_v1, driver

# Setup Connection and prodruct
SESSION = 100
SCROLL_LOOP = 2
CATEGORY = "" #Add Keyword
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


A = 0
while A <= SESSION:
    k = 0
    while k <= SCROLL_LOOP:
        print (f"Scrape the loop at {k}")
        open_product_v1(CATEGORY=CATEGORY)
        time.sleep(2)
        driver.swipe(360, 1300, 360, 400, 500) # Adjust Swipe Product with your device
        k = k + 1

    A = A + 1