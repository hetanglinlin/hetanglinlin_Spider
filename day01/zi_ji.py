from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

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
def main():
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

if __name__ == '__main__':
    # main1()
    # main2()
    # main3()
    main()