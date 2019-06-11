import urllib.request
import re


def get_boss_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    return response.read().decode('utf8')


def parse_html(html):
    patterns = re.compile('<div class="s_position_list " id="s_position_list">.*<ul>.*<li>(.*)</li></ul></div>', re.S)
    result = patterns.findall(html)
    # print(result)
    job_patterns = re.compile('<div class="p_top">(.*)</div>')
    result = job_patterns.findall(result[0])
    print(result)


def main():
    url = 'https://www.lagou.com/jobs/list_python?city=%E6%88%90%E9%83%BD#order'
    html = get_boss_html(url)
    # print(html)
    parse_html(html)


if __name__ == '__main__':
    main()