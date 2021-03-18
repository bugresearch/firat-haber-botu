import requests
from bs4 import BeautifulSoup
import time

token = "YOUR_TELEGRAM_TOKEN"
groudid = "YOUR_GROUP_ID"

oku = open("lastlink.txt")
lastlink = oku.read()
oku.close()

while 1==1:
    r = requests.get('http://www.firat.edu.tr/tr/page/news')
    source = BeautifulSoup(r.content,"lxml")
    yazi = source.find_all("a",attrs={"class":"main-color-1-hover"})
    url = yazi[0].get("href")
    baslik = yazi[0].text
    if lastlink != url:
        sendtext = baslik+"\n"+url
        data = requests.get("https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+groupid+"&text="+sendtext)
        last = open("lastlink.txt", "w")
        last.write(url)
        lastlink = url
        last.close()

    time.sleep(300)
