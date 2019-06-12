from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

soup = BeautifulSoup(html, 'lxml')
num1 = soup.find_all('ul', {'class': re.compile('list.*')})
for i in num1:
    print(i.get_text())



