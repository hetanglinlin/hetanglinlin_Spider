from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

html = urlopen("https://www.zhipin.com/job_detail/?query=python").read().decode('utf8')
print(html)


# soup = BeautifulSoup(html, features='lxml')
# print(soup.h1)
# print('\n', soup.p)



