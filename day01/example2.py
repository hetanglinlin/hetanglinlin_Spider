import requests

# res = requests.get('http://www.baidu.com')
# print(res.text)
# print(res.content)

res = requests.get('http://www.baidu.com/s', {'wd': 'python'})
# print(res.text)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
res = requests.get('http://www.baidu.com/s', {'wd': 'python'}, headers=headers)
print(res.text)
