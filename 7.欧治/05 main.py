from lxml import etree
import requests
from functools import partial
import subprocess
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs


# 初始化拿到第一个报错的相关数据
url = 'https://www.ouyeel.com/search-ng/commoditySearch/queryCommodityResult'
header = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
'referer':'https://www.ouyeel.com/steel/search?pageIndex=0&pageSize=50'
}
session = requests.session()
response = session.get(url,headers=header)
response.encoding = 'utf8'
tree = etree.HTML(response.text)

# 把几个要素取出来
content_str = tree.xpath('//meta/@content')[-1]
ts_js = tree.xpath('//script/text()')[0]
auto_url = 'https://www.ouyeel.com' + tree.xpath('//script[2]/@src')[0]
auto_js = session.get(auto_url).text

# py与js文件互动，传输cookie
js_code = open('04 main.js','r',encoding='utf8').read()
js_code=js_code.replace('metaContent',content_str).replace('auto_js',auto_js).replace('ts_js',ts_js)
# print(js_code)
js_compile = execjs.compile(js_code)
cookie_t = js_compile.call('get_cookie').split(';')[0].split('=')
# print(cookie_t)

# 更新cookie
session.cookies.update({cookie_t[0]:cookie_t[1]})
# print(session.cookies.get_dict())

# 新增传入参数
data = {
    "criteriaJson": '{"pageIndex":1,"pageSize":50,"industryComponent":null,"channel":null,"productType":null,'
                    '"sort":null,"warehouseCode":null,"key_search":null,"is_central":null,"searchField":null,'
                    '"companyCode":null,"inquiryCategory":null,"inquirySpec":null,"provider":null,'
                    '"packCodes":null,"shopCode":null,"steelFactory":null,"resourceIds":null,"jsonParam":{},'
                    '"excludeShowSoldOut":null}'
}

response = session.post(url,headers=header,data=data)
print(response.text)  # 这里仍得到的是cookie为错的返回(即三动参的html文件--因为引入的全是静态参)，还想调试把前几个文件中的三静参都替换为动态参数即可