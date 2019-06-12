from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re
import requests
import os
from urllib.request import urlretrieve

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 获取网页内容
html = urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html"
).read().decode('utf-8')


# ①正则表达式写法
def main1():
    res = re.findall(r"<title>(.+?)</title>", html)
    print(res[0])

    res1 = re.findall(r"<p>(.*)</p>", html, flags=re.DOTALL)
    print(res1[0])

    res2 = re.findall(r'href="(.*?)"', html)
    print(res2)


# ②导入BeautifulSoup，pip安装lxml解析器
def main2():
    # 让BeautifulSoup吃掉html
    soup = BeautifulSoup(html, features='lxml')

    # 找所有的h1标签
    print(soup.h1, '\n')

    # 找所有的p标签
    print(soup.p, '\n')

    # 找a标签中的href属性
    all_href = soup.find_all('a')
    for i in all_href:
        print(i['href'])
    # 简写 all_href = [i['href'] for i in all_href]
    print([i['href'] for i in all_href])


# ③使用 CSS 的 Class 来选择内容
def main3():
    # 获取网页内容
    html = urlopen(
        "https://morvanzhou.github.io/static/scraping/list.html"
    ).read().decode('utf-8')
    print(html)

    # 加入到BeautiflSoup里面,附加解析器lxml
    soup = BeautifulSoup(html, features='lxml')

    # 用class来缩小搜索范围,所有的li里面的month
    month = soup.find_all('li', {'class': 'month'})
    for i in month:
        # 显示所有的li，包含列表的代码
        # print(i)
        # 只显示文字
        print(i.get_text())

    # 获取ul里面别的元素,jan的li,找到 class=jan 的信息.
    # 然后在 <ul> 下面继续找 <ul> 内部的 <li> 信息.
    # 这样一层层嵌套的信息
    jan = soup.find('ul', {'class': 'jan'})

    # li已经被细化的类直接jan.find_all,不需要soup.find_all找
    d_jan = jan.find_all('li')
    for i in d_jan:
        # 只显示文字
        print(i.get_text())


# ④在 BeautifulSoup 中如何使用正则表达式, 获取更有难度的信息.
def main4():
    # 获取网页内容
    html = urlopen(
        "https://morvanzhou.github.io/static/scraping/table.html"
    ).read().decode('utf-8')
    print(html)

    # 加入到BeautiflSoup里面,附加解析器lxml
    soup = BeautifulSoup(html, features='lxml')

    # 匹配所有的img标签属性src，用正则来匹配src,截止图片格式为jpg格式
    img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg')})
    for link in img_links:
        # 获取src的链接(图片链接)
        print(link['src'])

    # 匹配其它的链接(不是图片)，a标签的href属性正则匹配
    course_links = soup.find_all("a", {"href": re.compile('https://morvan.*')})
    for link in course_links:
        # 获取href的链接
        print(link['href'])


# ⑤爬百度百科，导入random随机挑选一个内部的网页
def main5():
    # 在线编码解析，把中文解析了
    base_url = "https://baike.baidu.com"
    # 搜集之前选择过的网页,这是现在的网页
    his = ["/item/%E4%B8%80%E4%BA%BA%E4%B9%8B%E4%B8%8B/19685729"]
    # 从his中抽取最后一个网页，加上主网页
    url = base_url + his[-1]

    # 读取网页并解码
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')

    # 找单个,只要标题,是h1标签,获取第一个就可以,并且从his中取到儿子,也就是his初始值
    print(soup.find('h1').get_text(), 'url:', his[-1])


    # 找全部,并随机抽取,网页中所有的his,找规律并正则匹配
    # 所有的a里面的target属性是_blank,正则匹配其中的href属性
    sub_urls = soup.find_all('a', {'target': '_blank',
                                   'href': re.compile('/item/(%.{2})+$')})
    print(sub_urls)

    # 判断,如果找到了大于等于1的数据，就添加到his中,
    # 随机抽取1个target,选择href属性的数据，链接,
    # 如果sub_urls没有数据，就重新返回上一个his的链接，从上一个继续往下爬
    # 这是一个循环的代替
    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        his.pop()
    print(his)


    # 组合,找全部的href属性,先定义初始的网页
    his = ["/item/%E4%B8%80%E4%BA%BA%E4%B9%8B%E4%B8%8B/19685729"]
    # 循环20次
    for i in range(20):
        # 从his中抽取最后一个网页，加上主网页
        url = base_url + his[-1]
        # 读取网页并解码
        html = urlopen(url).read().decode('utf-8')
        soup = BeautifulSoup(html, features='lxml')
        # 循环次数+h1的标题+his中最后一个网页
        print(i, soup.find('h1').get_text(), 'url:', his[-1])
        # 所有a标签中有target属性，正则匹配href
        sub_urls = soup.find_all("a", {"target": "_blank",
                                       "href": re.compile("/item/(%.{2})+$")})
        # 判断是否取到href
        if len (sub_urls) != 0:
            his.append(random.sample(sub_urls, 1)[0]['href'])
        else:
            his.pop()


# ⑥使用requests进行post和get操作
def main():
    # 使用get,搜索的信息
    param = {"wd": "一人之下"}
    # 生成params参数,https://www.baidu.com/s?wd=%E4%B8%80%E4%BA%BA%E4%B9%8B%E4%B8%8B
    r = requests.get('https://www.baidu.com/s', params=param)
    print(r.url)


    # 使用post,模拟登陆,
    data = {'firstname': '冰', 'lastname': '凉'}
    # 获取post的url,监测动态：检查/Network/点登陆/processing.php/Headers/Request URL：xxxxxx
    r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
    print(r.text)

    # post的上传图片
    # file = {'uploadFile': open('1101.jpg', 'rb')}
    # r = requests.post('http://pythonscra/ping.com/pages/files/processing2.php', files=file)
    # print(r.text)

    # 使用cookies
    # payload = {'username': 'Morvan', 'password': 'password'}
    # r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
    # print(r.cookies.get_dict())

    # r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
    # print(r.text)

    # 使用session
    session = requests.Session()
    payload = {'username': '1101', 'password': 'password'}
    r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
    print(r.cookies.get_dict())

    r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
    print(r.text)


# ⑦下载文件
def main():
    # 第一种
    os.makedirs ('./img/', exist_ok=True)
    IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
    # 或者
    urlretrieve (IMAGE_URL, './img/image1.png')

    # 第二种
    r = requests.get (IMAGE_URL)
    with open ('./img/image2.png', 'wb') as f:
        f.write (r.content)  # whole document

    # 第三种
    r = requests.get (IMAGE_URL, stream=True)  # stream loading
    with open ('./img/image3.png', 'wb') as f:
        for chunk in r.iter_content (chunk_size=32):
            f.write (chunk)


if __name__ == '__main__':
    # main1()
    # main2()
    # main3()
    # main4()
    # main5()
    # main6()
    main()