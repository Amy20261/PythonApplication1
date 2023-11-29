from time import sleep
from selenium import webdriver

browser=webdriver.Firefox()
browser.get('https://www.google.com/search?q=iphone13&tbm=shop')
browser.maximize_window()
sleep(3)

names=browser.find_elements_by_xpath('//h3')

nameList=[]
for name in range(len(names)):
    nameList.append(names[name].text)    
print(*nameList, sep = "\n")



