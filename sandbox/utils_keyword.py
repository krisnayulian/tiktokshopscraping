from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction

# Setup Component
SHARE_BUTTON = "com.zhiliaoapp.musically:id/j85"
SHARE_BUTTON2="com.zhiliaoapp.musically:id/bf7"
COPY_BUTTON = "com.zhiliaoapp.musically:id/j7p"
CLOSE_DIALOG = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/X.RSl/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.lynx.component.svg.UISvg[9]"
UP_BUTTON = "com.zhiliaoapp.musically:id/c2p"
RES_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView"
PROMO_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.lynx.tasm.behavior.ui.LynxFlattenUI[15]"
BACK_BUTTON ="com.zhiliaoapp.musically:id/b8w"
BACK_SEARCH ="com.zhiliaoapp.musically:id/a9a"
BACK_VIDEO ="com.zhiliaoapp.musically:id/a9_"
CLOSE_LIVE ="com.zhiliaoapp.musically:id/b98"

def driver(SERVER_APPIUM_IP, SERVER_APPIUM_PORT, desired_caps):
        global driver
        driver = webdriver.Remote(f"http://{SERVER_APPIUM_IP}:{SERVER_APPIUM_PORT}/wd/hub", desired_caps)
        return driver

def up_button(): TouchAction(driver).tap(None, 643, 1243).perform() # coordinat of up button 
    # return driver.find_element(by=AppiumBy.ID, value=f"{UP_BUTTON}").click() # Adjust with your device

def close_dialog(): 
    return driver.find_element(by=AppiumBy.XPATH, value=f"{CLOSE_DIALOG}").click() # close unnecesary dialogbox

def close_response(): 
    return driver.find_element(by=AppiumBy.XPATH, value=f"{RES_BUTTON}").click() # close response product

def close_promo(): 
    return driver.find_element(by=AppiumBy.XPATH, value=f"{PROMO_BUTTON}").click() # close layout promo

def get_link_product():
    #driver.implicitly_wait(4)
    time.sleep(3) 
    # default 3s
    # TouchAction(driver).tap(None, 506, 101).perform()
    driver.find_element(by=AppiumBy.ID, value=f"{SHARE_BUTTON}").click()
    #driver.implicitly_wait(4)
    time.sleep(1)
    driver.find_element(by=AppiumBy.ID, value=f"{COPY_BUTTON}").click()
    return driver.get_clipboard_text()

def get_link_product2():
    #driver.implicitly_wait(4)
    time.sleep(10) 
    # default 3s
    # TouchAction(driver).tap(None, 506, 101).perform()
    driver.find_element(by=AppiumBy.ID, value=f"{SHARE_BUTTON2}").click()
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
    xy = {172 : 580, 525 : 582, 175 : 1200, 500 : 1202}
    for i, j in xy.items():
        try: time.sleep(3); actions.tap(None,i,j).perform()
        except: continue
        # try: close_response()
        # except: pass
        try:
            link = get_link_product()
            print("found link : ", link)
            df.append(link)
            time.sleep(2)
            driver.back();continue
        except: pass
        try: driver.find_element(by=AppiumBy.ID, value=f"{BACK_BUTTON}").click() ;continue
        except: pass
        try:
            link = get_link_product2()
            print("found link : ", link)
            df.append(link)
            time.sleep(3)
            driver.back()
            time.sleep(3)
            driver.back()
        except: pass
        # time.sleep(6)
        # try: driver.find_element(by=AppiumBy.ID, value=f"{BACK_VIDEO}").click()
        # except: continue
        # try: driver.find_element(by=AppiumBy.ID, value=f"{CLOSE_LIVE}").click()
        # except: continue
    df = pd.DataFrame(df)
    df.to_csv(f'/home/krisna/github/tiktokscraping/data_september/{CATEGORY}.csv', mode='a', index=False, header=False) # Set up Folder Save File CSV