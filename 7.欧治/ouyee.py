import json
import random
import sys
import time

from lxml import etree
import requests

# 为subprocess在使用execjs的情况下统一设置utf8，同时不让其因为改变影响别的用到subprocess的地方
from functools import partial
import subprocess
my_popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
from loguru import logger
execjs._external_runtime.Popen = my_popen


# 1.初始化各种参数
session = requests.session()
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
}
url = 'https://www.ouyeel.com/search-ng/commoditySearch/queryCommodityResult'


# 2.第一次发起请求访问瑞数页，获取三大件
def surf_1():
    res = session.get(url, headers=header).text
    tree = etree.HTML(res)
    metaContent = tree.xpath('//meta/@content')[-1]
    ts_script = tree.xpath('//script/text()')[0]
    auto_url = 'https://www.ouyeel.com' + tree.xpath('//script/@src')[0]
    auto_script = session.get(auto_url).text
    return metaContent, ts_script, auto_script


# 3.将三大件动态替换并使用其生成cookie2
def get_cookie2(metaContent, ts_script, auto_script):
    with open('ouyee.js', encoding='utf8') as f:
        js_code = f.read()
    # 原文就是双引号，所以要把那个双引号带着包裹一块替换
    js_code = js_code.replace('metaContent', metaContent).replace('"ts_js"', ts_script).replace('"auto_js"',
                                                                                                auto_script)
    js_compile = execjs.compile(js_code)
    js_cookie_key_value = js_compile.call('get_cookie').split(';')[0].split('=')
    # print(js_cookie_key_value)
    session.cookies.update({js_cookie_key_value[0]: js_cookie_key_value[1]})
    # print(session.cookies.get_dict())


# 4.更新c2并第二次发起请求访问数据页,并做数据清洗
def surf_2(page_index):
    data = {
        "criteriaJson": '{"pageIndex":%d,"pageSize":50,"industryComponent":null,"channel":null,"productType":null,'
                        '"sort":null,"warehouseCode":null,"key_search":null,"is_central":null,"searchField":null,'
                        '"companyCode":null,"inquiryCategory":null,"inquirySpec":null,"provider":null,'
                        '"packCodes":null,"shopCode":null,"steelFactory":null,"resourceIds":null,"jsonParam":{},'
                        '"excludeShowSoldOut":null}' % page_index
    }
    response = session.post(url, headers=header, data=data).json()
    logger.info(f'正在打印第{page_index}页产品列表...')
    ret = response['resultList']
    ret = json.loads(ret)
    for i in ret:
        print(i)


# 5.编写爬虫整体逻辑
def main():
    for page in range(1, 8):
        metaContent, ts_script, auto_script = surf_1()
        get_cookie2(metaContent, ts_script, auto_script)
        surf_2(page)
        session.cookies.clear()  # 瑞数特点，需要不断清空cookie并给其新动态cookie值
        time.sleep(random.uniform(0.5, 0.8))


# 5.执行
if __name__ == '__main__':
    main()
