from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


import geckodriver_autoinstaller


geckodriver_autoinstaller.install()

#https://pypi.org/project/geckodriver-autoinstaller/

display = Display(visible=0, size=(1024, 768))
display.start()

options = Options()

options.add_argument('--no-sandbox')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-dev-shm-usage')




#open driver
#https://chromedriver.chromium.org/getting-started
driver = webdriver.Firefox()


driver.get('http://raspberrypi.stackexchange.com/')
driver.quit()

display.stop()