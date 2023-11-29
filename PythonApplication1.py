from bs4 import BeautifulSoup
import requests
url='https://www.google.com/search?q=iphone13&tbm=shop'
html=requests.get(url)
sp=BeautifulSoup(html.text,'html.parser')

#print(sp)

productNames=sp.select("div div div")

nameList=[]
for name in range(len(productNames)):
    nameList.append(productNames[name].text)    
print(*nameList, sep = "\n")
