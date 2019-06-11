import re
import urllib.request


def get_boss_html(url):
    """
    获取岗位页面源码
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    return response.read().decode('utf8')
#
#
# def parse_html(html):
#     patterns = re.compile('<div class="company-list">.*</div>.*<ul>(.*)</ul>.*<div class="page">', re.S)
#     result = patterns.findall(html)
#     print(result)
#     # 2. 匹配刚查询的url中li中的岗位信息
#     job_patterns = re.compile('<div class="job-title">(.*)</div><span class="red">(.*)</span>', re.S)
#     result = job_patterns.findall(result[0])
#     print(result)


def main():
# 爬取boss中成都python岗位的源码
    url = 'https://www.zhipin.com/job_detail/?query=python'
    # 定义获取源码的方法
    html = get_boss_html(url)
    print(html)
    # parse_html(html)


if __name__ == '__main__':
    main()