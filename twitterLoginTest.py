import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\Mandalorian\\Documents\\Browser Driver\\chromedriver_win32\\chromedriver.exe")
driver.get("https://twitter.com")
driver.maximize_window()
# driver.implicitly_wait(5)

assert "Icon--bird" in driver.page_source

login = WebDriverWait(driver,5).until(lambda driver : driver.find_element_by_xpath('//*[@id="doc"]/div/div[1]/div[1]/div[2]/div[2]/div/a[2]'))
login.click()

time.sleep(5)

link = WebDriverWait(driver,5).until(lambda driver : driver.find_element_by_link_text("Forgot password?"))
link.click()

time.sleep(5)
driver.back()

checkbox = WebDriverWait(driver,5).until(lambda driver : driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/div/label/input'))
checkbox.click()

username = WebDriverWait(driver,5).until(lambda driver : driver.find_element_by_css_selector(".js-username-field.email-input.js-initial-focus"))
# username = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')

password = WebDriverWait(driver,5).until(lambda driver : driver.find_element_by_css_selector('.js-password-field'))

login_button = WebDriverWait(driver,5).until(lambda driver : driver.find_element_by_css_selector('.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium'))
# login_button = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')

username.clear()
#type twitter username here
username.send_keys("")

password.clear()
#type twitter password here
password.send_keys("")
login_button.click()

assert "Icon Icon--bird bird-topbar-etched" in driver.page_source

print("Test Execution Success !!!!")

time.sleep(5)
driver.quit()
