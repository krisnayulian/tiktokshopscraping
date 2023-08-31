import pandas as pd
import subprocess as proc
import re
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time

# Input
START_SHOP = 7
CATEGORY = "Skincare"
CONNECTION = "192.168.0.108:5555"

# Sony Xperia XZ2
SHOP_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]"
OPEN_SHOP = "com.ss.android.ugc.trill:id/oo"
SELECT_PRODUCT = {275 : 750, 800 : 745, 276 : 1620, 805 : 1622}
SCROLL_DOWN = [538, 1750, 538, 800, 500]
SWIPE_PRODUCT = [538, 1750, 538, 540, 500]
CLOSE_TOP_PRODUCT = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.lynx.tasm.behavior.ui.LynxFlattenUI[3]"
SHARE_BUTTON = "com.ss.android.ugc.trill:id/imb"
SHARE_BUTTON_2 = "com.ss.android.ugc.trill:id/i3u"
COPY_BUTTON = "//android.widget.Button[@content-desc=\"Copy link\"]/android.widget.ImageView"
KEYWORD_BOX = "com.zhiliaoapp.musically:id/l3r"
BACK_BUTTON ="com.ss.android.ugc.trill:id/b39"
BACK_SEARCH ="com.ss.android.ugc.trill:id/a5o"
SC_1 = SWIPE_PRODUCT
SC_2 = SCROLL_DOWN

# byte_output = proc.check_output(["adb", "shell", "ip", "addr", "show", "wlan0", "|", "grep", "inet"])
# str_output = str(byte_output, "utf-8")
# regex = re.findall(r'(?<=inet ).*?(?=/)', str_output)
# try: print("connected to: " + regex[0])
# except: print("please connect to device")

shop_link = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vT7tvXpj_f76tQ253mumt-PaGOH_Xn7qo1k-BFRNm4VppAaOgBipS4BogQEtt4APFYXqhc8PQuNw7tA/pub?gid=1297736669&single=true&output=csv")
link_shop = shop_link["shop_link"].iloc[START_SHOP:]

desired_caps = {
    "platformName": "Android",
    "appium:deviceName": "device",
    "appium:udid": CONNECTION,
    "appium:noReset": True,
}

driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub", desired_caps)
actions = TouchAction(driver)


def get_link_search():
    #driver.implicitly_wait(4)
    time.sleep(3) 
    # default 3s
    # TouchAction(driver).tap(None, 506, 101).perform()
    driver.find_element(by=AppiumBy.ID, value=f"{SHARE_BUTTON}").click()
    #driver.implicitly_wait(4)
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value=f"{COPY_BUTTON}").click()
    return driver.get_clipboard_text()


# Open product function
def open_prod():
    df = []
    for i, j in SELECT_PRODUCT.items():
        try: time.sleep(3); actions.tap(None,i,j).perform()
        except: print("cant open the product"); pass
        try:
            link = get_link_search()
            print("found link : ", link) 
            df.append(link)
            driver.swipe(SC_1[0], SC_1[1], SC_1[2], SC_1[3], SC_1[4]) # swipe live product video
            time.sleep(1); driver.back(); continue  
        except: pass
        try: driver.find_element(by=AppiumBy.ID, value=f"{BACK_BUTTON}").click()
        except: pass

        # try: time.sleep(1); driver.find_element(by=AppiumBy.ID, value=f"{CLOSE_END_LIVE}").click(); print("cant share link 1"); continue
        # except: print ("can't close end live"); pass
        # try: time.sleep(1); driver.find_element(by=AppiumBy.XPATH, value=f"{CLOSE_TOP_PRODUCT}").click(); print("cant share link 2"); continue
        # # except: pass
        # try: 
        #     """
        #     for back to the page if open the keyword recomendation page
        #     """
        #     if driver.find_element(by=AppiumBy.ID, value=KEYWORD_BOX).text != CATEGORY:
        #         print("ups.. wrong click. back......")
        #         driver.back(); continue
        #     else: pass
        # except: pass
    df = pd.DataFrame(df)
    df.to_csv(f'/home/krisna/github/tiktokscraping/data_juli/{CATEGORY}.csv', mode='a', index=False, header=False)

# Scroll and select products function
def swipe():
    k = 1
    while k<=50:
        print (f"Scrape the loop at {k}")
        open_prod()
        driver.swipe(SC_2[0], SC_2[1], SC_2[2], SC_2[3], SC_2[4]) # Adjust with your device
        time.sleep(2)
        k = k+1
        try:
            driver.find_element(by=AppiumBy.XPATH, value="//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc='No more products']").click()
            break
        except: pass

# Main flow of program
b = 0
for i in link_shop:
    print(f"opening shop {b}")
    try:
        driver.execute_script("mobile: deepLink", {'url': i, 'package': 'com.ss.android.ugc.trill'})
    except: continue
    time.sleep(3)
    try:
        driver.find_element(by=AppiumBy.ID, value=f"{OPEN_SHOP}").click()
    except: pass
    time.sleep(4)
    try: 
        driver.find_element(by=AppiumBy.XPATH, value='//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Categories"]').click()
        time.sleep(4)
        driver.find_element(by=AppiumBy.XPATH, value=f'//*[contains(@text,"{CATEGORY}")]').click()
    except: 
        pass
    time.sleep(3)
    try:
        driver.find_element(by=AppiumBy.XPATH, value='//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Bestsellers"]').click()
    except: pass
    time.sleep(2)
    swipe()
    b = b+1
    driver.close_app()