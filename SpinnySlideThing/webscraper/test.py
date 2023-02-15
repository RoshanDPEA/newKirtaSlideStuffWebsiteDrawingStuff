from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from pyvirtualdisplay import Display

display = Display(visible=False, size=(1600, 1200))
display.start()

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
#chrome_options.add_argument("--kiosk")

#open driver
#https://chromedriver.chromium.org/getting-started
driver = webdriver.Chrome(executable_path="/usr/local/bin/geckodriver", options=chrome_options)
driver.get("https://www.google.com")


