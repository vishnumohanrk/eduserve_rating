from selenium import webdriver
# vishnumohan rk

driver = webdriver.Firefox()
driver.get("https://eduserve.karunya.edu/Login.aspx")

lis_file = []
with open('README.txt', 'rt') as my_file:
    for i in my_file:
        lis_file.append(i)

user = lis_file[8][7:]
pwd = lis_file[9][9:]

elem = driver.find_element_by_xpath('//*[@id="mainContent_Login1_UserName"]')
elem.send_keys(user)
elem = driver.find_element_by_xpath('//*[@id="mainContent_Login1_Password"]')
elem.send_keys(pwd)

submit = driver.find_element_by_xpath('//*[@id="mainContent_Login1_LoginButton"]')
submit.click()

try:
    a = driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[1]/td[5]/div/ul/li[5]/a')
    a.click()
except:
    pass

try:
    b = driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[5]/div/ul/li[5]/a')
    b.click()
except:
    pass

try:
    c = driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[5]/div/ul/li[5]/a')
    c.click()
except:
    pass

try:
    d = driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[4]/td[5]/div/ul/li[5]/a')
    d.click()
except:
    pass

try:
    e = driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[5]/td[5]/div/ul/li[5]/a')
    e.click()
except:
    pass

try:
    f = driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[6]/td[5]/div/ul/li[5]/a')
    f.click()
except:
    pass

try:
    g = driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[7]/td[5]/div/ul/li[5]/a')
    g.click()
except:
    pass

try:
    h = driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[8]/td[5]/div/ul/li[5]/a')
    h.click()
except:
    pass

try:
    i = driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[8]/td[5]/div/ul/li[5]/a')
    i.click()
except:
    pass

try:
    save = driver.find_element_by_xpath('//*[@id="mainContent_btnSave"]')
    save.click()
except:
    pass
