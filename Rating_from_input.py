from selenium import webdriver
# vishnumohan rk

driver = webdriver.Firefox()
driver.get("https://eduserve.karunya.edu/Login.aspx")

user = input()
pwd = input()

elem = driver.find_element_by_xpath('//*[@id="mainContent_Login1_UserName"]')
elem.send_keys(user)
elem = driver.find_element_by_xpath('//*[@id="mainContent_Login1_Password"]')
elem.send_keys(pwd)

submit = driver.find_element_by_xpath('//*[@id="mainContent_Login1_LoginButton"]')
submit.click()

for i in range(13):
    try:
        x = ('/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[{}]/td[5]/div/ul/li[5]/a'.format(i))
        # print(x)
        driver.find_element_by_xpath(x).click()
    except:
        pass

try:
    save = driver.find_element_by_xpath('//*[@id="mainContent_btnSave"]')
    save.click()
except:
    pass
