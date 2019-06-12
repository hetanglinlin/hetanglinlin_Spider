from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import time

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


for i in range(10):
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    # }
    url = "https://maoyan.com/board/4/?offset={}".format(i*10)
    # res = requests.get(url, headera=headers)
    html = urlopen(url).read().decode('utf-8')
    # time.sleep(3)
    # print(res)
    print(type(html))
    soup = BeautifulSoup(html, features='lxml')
    score = soup.find_all("p", {"class": "score"})
    # scor1 = soup.find_all("i", {"class": "fraction"})
    for i in score:
        print(i.get_text())

# html = urlopen ("https://maoyan.com/board/4").read().decode('utf-8')
# soup = BeautifulSoup(html, features='lxml')

# res = requests.get(url, headers = HEADERS)