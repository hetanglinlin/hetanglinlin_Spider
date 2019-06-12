from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# def get_page_html(url):
#     headers={
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
#     }
#     res = requests.get(url, headera=headers)
#     return res.text
#
#
# def parse_html(html):
#
#     return ''


# html = urlopen ("https://maoyan.com/board/4").read().decode('utf-8')
# soup = BeautifulSoup(html, features='lxml')
num1 = ""
for i in range(3):
    url = "https://maoyan.com/board/4/?offset={}".format(i*3)
    html = urlopen(url).read().decode('utf-8')
    num1 += html

soup = BeautifulSoup(num1, features='lxml')
print(soup)
print(type(soup))
# name = soup.find_all("p", {"class": 'star'})
# for i in name:
#     print(i.get_text())

    # num = soup.find_all("p", {"class": "releasetime"})
    # for i in num:
    #     print(i.get_text())
    #
    # ranking = soup.find_all("i", {"class": re.compile('board.*')})
    # for i in ranking:
    #     print(i.get_text())
    #
    # movie = soup.find_all("a", {"data-act": re.compile('boarditem.*')})
    # for i in movie:
    #     print(i.get_text())
    #
    # score = soup.find_all("p", {"class": "score"})
    # # scor1 = soup.find_all("i", {"class": "fraction"})
    # for i in score:
    #     print(i.get_text())



