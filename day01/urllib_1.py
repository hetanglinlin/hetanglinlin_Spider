import urllib.request
import urllib.error
import urllib.response
import urllib.parse

# urllib.request.urlopen(url, data=None, timeout=socket._)


# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf8'))

# req = urllib.request.Request(url='http://www.baidu.com/s?wd=python')
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf8'))


proxyHandler = urllib.request.ProxyHandler({
    'https': 'https://119.57.108.53:53281'
})
opener = urllib.request.build_opener(proxyHandler)

data = urllib.parse.urlencode({'wd': 'python'})
data = bytes(data, encoding='utf8')
response = opener.open('http://www.baidu.com/s?wd=python')
print(response.read().decode('utf8'))