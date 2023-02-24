#stackoverflow https://stackoverflow.com/questions/37354868/how-can-i-open-a-image-in-another-tab-using-selenium-for-python

#import libraries
#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import _thread as thread
import threading
import time
from time import sleep

import enum
from dpea_p2p import Client

class PacketType(enum.Enum):
    NULL = 0
    COMMAND1 = 1
    COMMAND2 = 2

#         |Server IP     |Port |Packet enum
c = Client("172.17.21.2", 5001, PacketType)
c.connect()

def packetChecking():
    while True:
        pack = c.recv_packet()
        if pack[1] == "1":
            driver.navigate().refresh()
        

#guide for chrome driver install https://techenum.com/install-raspberrypi-selenium-chromedriver/

#wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip

#multiple kiosk windows https://stackoverflow.com/questions/74928751/how-can-i-open-2-chrome-windows-in-kiosk-mode-on-2-monitors-with-webdriver-in-py

def imageUpdate():
    # https://stackoverflow.com/questions/40121382/control-chromium-kiosk-mode-url-from-python
    chrome_options1 = Options()
    #chrome_options1.add_argument('--headless')
    chrome_options1.add_argument('--no-sandbox')
    chrome_options1.add_argument('--disable-dev-shm-usage')

    chrome_options1.add_argument("--kiosk")

    # open driver
    # https://chromedriver.chromium.org/getting-started
    driver1 = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options1)

    driver1.set_window_position(2000, 0)

    # go to website where images are
    web_url1 = "https://en.wikipedia.org/wiki/Image"
    driver1.get(web_url1)

    # https://stackoverflow.com/questions/37354868/how-can-i-open-a-image-in-another-tab-using-selenium-for-python
    # search for image by looking for keyword
    im_link1 = driver1.find_element_by_class_name("image")
    # im_link.click()
    # open in new tab
    im_link1.send_keys(Keys.CONTROL + Keys.RETURN)

    # open new kiosk tab
    # #https://www.tutorialspoint.com/how-to-close-active-current-tab-without-closing-the-browser-in-selenium-python

    # choose where to open tab
    # https://stackoverflow.com/questions/3816073/in-a-multi-monitor-display-environment-how-do-i-tell-selenium-which-display-to
    # have a second thread control the second monitor

    # identify element
    # m = driver.find_element_by_link_text("Help")
    # m.click()
    # obtain parent window handle

    # https://www.tutorialspoint.com/how-to-close-active-current-tab-without-closing-the-browser-in-selenium-python closing tabs
    p1 = driver1.window_handles[1]
    driver1.switch_to.window(p1)

    while True:
        sleep(15)

    """"
    #m.click()
    # obtain parent window handle
    p = driver.window_handles[0]
    # obtain browser tab window
    #c = driver.window_handles[1]
    # switch to tab browser
    driver.switch_to.window(c)
    print("Page title :")
    print(driver.title)
    # close browser tab window
    driver.close()
    # switch to parent window
    driver.switch_to.window(p)
    print("Current page title:")
    #print(driver.title)
    # close browser parent window
    driver.quit()
    """



#https://stackoverflow.com/questions/40121382/control-chromium-kiosk-mode-url-from-python
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--kiosk")

#open driver
#https://chromedriver.chromium.org/getting-started
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)

#driver.set_window_position(2000, 0)
#go to website where images are
#driver.get("https://www.google.com")
web_url = "https://en.wikipedia.org/wiki/Image"
driver.get(web_url)

print("going to website")



#https://stackoverflow.com/questions/37354868/how-can-i-open-a-image-in-another-tab-using-selenium-for-python
#search for image by looking for keyword
print("finding image")
im_link = driver.find_element_by_class_name("image")
#im_link.click()
#open in new tab
im_link.send_keys(Keys.CONTROL+Keys.RETURN)

#open new kiosk tab
# #https://www.tutorialspoint.com/how-to-close-active-current-tab-without-closing-the-browser-in-selenium-python

#choose where to open tab
#https://stackoverflow.com/questions/3816073/in-a-multi-monitor-display-environment-how-do-i-tell-selenium-which-display-to
#have a second thread control the second monitor

#identify element
#m = driver.find_element_by_link_text("Help")
#m.click()
#obtain parent window handle

#https://www.tutorialspoint.com/how-to-close-active-current-tab-without-closing-the-browser-in-selenium-python closing tabs
p= driver.window_handles[0]
driver.switch_to.window(p)

driver.switch_to.window(p)
driver.close()




"""
#obtain browser tab window
c = driver.window_handles[1]
#switch to tab browser
driver.switch_to.window(c)
print("Page title :")
print(driver.title)
#close browser tab window
driver.close()
#switch to parent window
#driver.switch_to.window(p)
print("Current page title:")
#print(driver.title)
#close browser parent window
driver.quit()

"""

#second monitor

#thread.start_new_thread(imageUpdate(), ())

thr = threading.Thread(target=imageUpdate())
thr.start()


thr = threading.Thread(target=imageUpdate())
thr.start()
