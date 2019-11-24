import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.error
import json
import random
import string


def find_dom(domain):
    """
    输入要查询的域名名字进行查询
    例如:
        find_dom(abc)
    那么查询的是 abc.com是否被查询
    并且将查询到未注册的域名写入到data.txt文件里面
    :param domain: 查询的域名名字
    :return:
    """
    headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0;'
                             ' WOW64) AppleWebKit/537.36 (KHTML, like '
                             'Gecko) Chrome/63.0.3239.26 Safari/537.36 Co'
                             're/1.63.6726.400 QQBrowser/10.2.2265.400')  # 模拟浏览器
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]  # 使用自己的代码模拟浏览器
    urls = "https://checkapi.aliyun.com/check/checkdomain?domain=%s.com&command=&" \
           "token=Y9f55e9ce9c1606f54cdedbca15ded06a&ua=&currency=&site=&bid=&_csrf_token=&" \
           "callback=jsonp_1574580335310_2403" % domain
    respon1 = opener.open(urls)  # 打开网页

    soup = BeautifulSoup(respon1, features='html.parser')  # 解码存到soup中
    a = soup.decode()
    pattern = re.compile(r'{"avail.*?"}')
    flag = pattern.findall(a)
    try:
        js = json.loads(flag[0])
    except:
        return "被注册"
    if js.get("avail") == 1:
        print(js.get("name"))
        with open('data.txt', 'a+') as f:
            f.write(js.get("name") + "\r\n")
    else:
        print("已注册")
        # pass


# 随机字母
def get_random_letters(index):
    """
    获取完全随机的index位字母
    :param index: 表示的是字母的长度
    :return: index个随机字母
    """
    s = string.ascii_lowercase  # 所有小写字母(a-z)
    random_letters = ''
    for i in range(index):
        a = random.choice(s)
        random_letters += a
    return random_letters


# 顺序字母并且查询
def get_order_letters_and_find():
    """
    从aaaaa到zzzzz的顺序规律进行暴力循环查询
    :return:
    """
    s = string.ascii_lowercase  # 所有小写字母(a-z)
    for i in s:
        for j in s:
            for k in s:
                for l in s:
                    for m in s:
                        letter = i + j + k + l + m
                        find_dom(letter)


if __name__ == '__main__':
    # 第一种使用方式
    for i in range(1000000):
        find_dom(get_random_letters(5))

    # 第二种
    get_order_letters_and_find()

