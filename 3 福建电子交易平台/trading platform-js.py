import json
import time
import random
import requests

import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
# 此处作用是处理编解码问题，部分地方不是默认一种编码如utf8，在js与py的互传中会出现问题。
import execjs

js_code = open('get_sign.js',encoding='utf8').read()
js_compile = execjs.compile(js_code)

cookies = {
    'Hm_lvt_9d1de05cc99f08ddb5dc6d5e4d32ad30': '1748663404',
    'Hm_lvt_db393520fa240b442a13a6d1c5ae95c1': '1748663404',
    'Hm_lvt_94bfa5b89a33cebfead2f88d38657023': '1748663404',
    '_qddagsx_02095bad0b': '56513d8598483de2ed73aed55e8aabf16ed281359ea81cfc61624365ae344a225aa2e8fbb447be28a300aa106242e9f48e05fe34df0c36bacbe6032e8b8f02ad81410d23a71ce5843ca6f721bcf735d8c93cb2cd5dbdbb1c6e31796c45fc03f00c954367bc8f910a45a98e5f5d7489ea86a6f1c9abfc36a88deb16fd4b7b0141',
}

# 批量获取
for i_ in range(1, 11):
    # 生成时间戳
    t = int(time.time() * 1000)
    json_data = {
        'pageNo': i_,
        'pageSize': 20,
        'total': 2623,
        'AREACODE': '',
        'M_PROJECT_TYPE': '',
        'KIND': 'GCJS',
        'GGTYPE': '1',
        'PROTYPE': '',
        'timeType': '6',
        'BeginTime': '2024-12-01 00:00:00',
        'EndTime': '2025-06-01 23:59:59',
        'createTime': '',
        'ts': t,
    }
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ggzyfw.fujian.gov.cn',
        'Referer': 'https://ggzyfw.fujian.gov.cn/business/list/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'Hm_lvt_9d1de05cc99f08ddb5dc6d5e4d32ad30=1748663404; Hm_lvt_db393520fa240b442a13a6d1c5ae95c1=1748663404; Hm_lvt_94bfa5b89a33cebfead2f88d38657023=1748663404; _qddagsx_02095bad0b=56513d8598483de2ed73aed55e8aabf16ed281359ea81cfc61624365ae344a225aa2e8fbb447be28a300aa106242e9f48e05fe34df0c36bacbe6032e8b8f02ad81410d23a71ce5843ca6f721bcf735d8c93cb2cd5dbdbb1c6e31796c45fc03f00c954367bc8f910a45a98e5f5d7489ea86a6f1c9abfc36a88deb16fd4b7b0141',
    }
    # 加密逻辑
    sign = js_compile.call('d',json_data) # 调用d这个函数，传入json_data作为参数
    headers['portal-sign'] = sign



    response = requests.post(
        'https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    data = response.json().get('Data')
    # 解密逻辑
    contents = js_compile.call('b',data) # 使用js代码中的b函数，data作为传入参数
    # 从逆向网站得到的数据/加解密数据，一般都是json格式（字符串包裹），通常需要data.json()或者json.loads(xx)将其转化为py对象
    contents = json.loads(contents)
    print(f'正在打印第{i_}页...')
    for i in contents['Table']:
        print(i['NAME'])
    time.sleep(random.uniform(0.4, 0.7))
print(f'打印完成!一共打印10页!')
