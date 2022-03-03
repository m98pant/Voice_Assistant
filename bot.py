from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def account_info():
    with open('account_info.txt', 'r') as f:
        info = f.read().split()
        email = info[0]
        password = info[1]
    return email, password

email, password = account_info()


options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://www.instagram.com/accounts/login/")

email_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
password_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
login_xpath = '//*[@id="loginForm"]/div/div[3]'

not_now_xpath = '//*[@id="react-root"]/div/div/section/main/div/div/div/div/button'
not_now_notfication = '/html/body/div[5]/div/div/div/div[3]/button[2]'
message_count_xpath = '//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div/div' 

time.sleep(3)

driver.find_element_by_xpath(email_xpath).send_keys(email)
driver.find_element_by_xpath(password_xpath).send_keys(password)
driver.find_element_by_xpath(login_xpath).click()
time.sleep(3)
driver.find_element_by_xpath(not_now_xpath).click()
time.sleep(2)
driver.find_element_by_xpath(not_now_notfication).click()
time.sleep(2)
count = driver.find_element_by_xpath(message_count_xpath).text
print('Message: '+count)

