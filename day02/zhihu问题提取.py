from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


def get_zhihu_html(url):
    # 获取页面源码
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    return res.text


def parse_html(html):
    # 解析页面源码
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find_all(class_='question_link')#拿到所有的a标签
    result = []
    for item in data:#item代表每个a
        result.append({'question': item.string.strip(), 'href':item.attrs['href']})
    return result


def main():
    url = 'https://www.zhihu.com'
    search_path = 'explore'
    # 获取页面源码
    html = get_zhihu_html(urljoin(url, search_path))
    #解析页面源码
    result = parse_html(html)
    #解析最终返回结果
    # for item in result:
    #     item['href'] = urljoin(url, item['href'])
    result= [{'question': item['question'], 'href': urljoin(url, item['href'])} for item in result]
    print(result)


if __name__ == '__main__':
    main()