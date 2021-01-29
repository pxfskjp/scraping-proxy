from selenium import webdriver
from selenium.webdriver.common.proxy import *
import time
import csv

# IP: 192.199.249.207
# Port: 21239
# user: sondeeshar14595
# password: qjlqt1s03h

# sudo apt update
# sudo apt install python3-pip
# sudo apt-get install python-pip3
# sudo pip3 install selenium
# https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu
# https://medium.com/@griggheo/running-selenium-webdriver-tests-using-firefox-headless-mode-on-ubuntu-d32500bb6af2

# IP: 45.76.20.81
# Port: 22
# user: root
# pass: Pq5_A4tco?G]QX*S

myProxy = "192.199.249.207: 21239"
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy, # set this value as desired
    'ftpProxy': myProxy,  # set this value as desired
    'sslProxy': myProxy,  # set this value as desired
    'noProxy': '',         # set this value as desired
    'socksUsername': 'sondeeshar14595',
    'socksPassword': 'qjlqt1s03h'
    })


driver = webdriver.Firefox(proxy=proxy)

# driver = webdriver.Firefox()
# driver.maximize_window()
driver.get("https://wordpress.org/themes/browse/popular/")
i = 0
# total = 4248

while i < 10:
    height = driver.execute_script("return document.body.scrollHeight")
    print("i = ", i, ",height = ", height)
    if (height < 1000 * i):
        break
    driver.execute_script("window.scrollTo(0, " + str(1000 * i) + ");")
    i += 1
    time.sleep(1.5)

container = driver.find_elements_by_xpath("//a[@class='theme-name entry-title']")
titles = []
for name in container:
    titles.append(name.text)
print(len(titles))

with open('output.csv', 'w', newline='') as output:
    fieldnames = ['name', 'index']
    writer = csv.DictWriter(output, fieldnames = fieldnames)
    writer.writeheader()

    with open('input.csv', newline='') as input:
        reader = csv.DictReader(input)
        for row in reader:
            search = row['title']
            if (search in titles):
                writer.writerow({'name': search, 'index': titles.index(search) + 1})
            else:
                writer.writerow({'name': search, 'index': 'no'})
driver.close()