from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")

#Set driver to Chrome.
#Add your path to chromedriver in the parens. Ex.  /home/user/Downloads/chromedriver
driver=webdriver.Chrome("")

driver.get("https://html5up.net")

elements = []

for i in range(1, 46):
    xpath = '//*[@id="items"]/article[' + str(i) + ']/header/div/a[2]'
    elements.append(driver.find_element_by_xpath(xpath))

for element in elements:
    element.click()
    driver.find_element_by_css_selector('#dialog > div > a').click()
    sleep(5)
