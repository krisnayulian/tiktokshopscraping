from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction

# Setup Component
SHARE_BUTTON = "com.ss.android.ugc.trill:id/ka0"
SHARE_BUTTON2="com.ss.android.ugc.trill:id/bqs"
COPY_BUTTON = "com.ss.android.ugc.trill:id/k_k"
BACK_BUTTON ="com.ss.android.ugc.trill:id/bjk"
BACK_SEARCH ="com.ss.android.ugc.trill:id/agy"
BACK_VIDEO ="com.ss.android.ugc.trill:id/agx"
CLOSE_LIVE ="com.ss.android.ugc.trill:id/bjy"
TOP_PROUDCT="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.lynx.tasm.behavior.ui.LynxFlattenUI[4]"


def driver(SERVER_APPIUM_IP, SERVER_APPIUM_PORT, desired_caps):
        global driver
        driver = webdriver.Remote(f"http://{SERVER_APPIUM_IP}:{SERVER_APPIUM_PORT}/wd/hub", desired_caps)
        return driver

def up_button(): TouchAction(driver).tap(None, 643, 1243).perform() # coordinat of up button 
    # return driver.find_element(by=AppiumBy.ID, value=f"{UP_BUTTON}").click() # Tap using Element(adjust with your device)

def get_link_product():
    #driver.implicitly_wait(4)
    time.sleep(3) 
    driver.find_element(by=AppiumBy.ID, value=f"{SHARE_BUTTON}").click()
    #driver.implicitly_wait(4)
    time.sleep(1)
    driver.find_element(by=AppiumBy.ID, value=f"{COPY_BUTTON}").click()
    return driver.get_clipboard_text()

def back_button(): 
    return driver.find_element(by=AppiumBy.ID, value=f"{BACK_BUTTON}").click()

#Open Product by Coordinat
def open_product_v1(CATEGORY):
    actions = TouchAction(driver)
    df = []
    xy = {275 : 750, 800 : 745, 276 : 1620, 805 : 1622} #Adjust With Your Coordinat Layout Product (4 Product On Screen)
    for i, j in xy.items():
        try: time.sleep(3); actions.tap(None,i,j).perform()
        except: continue
        try:
            link = get_link_product()
            print("found link : ", link)
            df.append(link)
            time.sleep(1)
            driver.back(); continue
        except: pass
        try: driver.find_element(by=AppiumBy.ID, value=f"{BACK_SEARCH}").click(); continue
        except: pass
        try: driver.find_element(by=AppiumBy.ID, value=f"{BACK_BUTTON}").click()
        except: pass

    df = pd.DataFrame(df)
    df.to_csv(f'/home/krisna/github/tiktokshopscraping/output/{CATEGORY}.csv', mode='a', index=False, header=False) # Set up Folder Save File CSV
