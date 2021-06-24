import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.onet.pl")
assert "Onet" in driver.title

counter = 0
while counter < 30:
    try:
        button = driver.find_element_by_xpath("//button[contains(@class, 'cmp-intro_acceptAll')]")
        button.click()
        break
    except:
        time.sleep(1)
        counter += 1

header = driver.find_element_by_xpath("(//div[contains(@class, 'popupCloseIcon')])[2]")
header.click()
driver.close()
