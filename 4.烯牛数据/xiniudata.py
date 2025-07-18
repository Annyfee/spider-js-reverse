import requests

import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
# 此处作用是处理编解码问题，部分地方不是默认一种编码如utf8，在js与py的互传中会出现问题。
import execjs


js_code =open('get_sign.js',encoding='utf8').read()
js_compile = execjs.compile(js_code)


cookies = {
    'btoken': 'XW5ZWFLQC4GNC29CQ0WNORLRHNSR854E',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1748917495,1748998768',
    'HMACCOUNT': 'F7B8C534891B7E31',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1749019827',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.xiniudata.com',
    'priority': 'u=1, i',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    # 'cookie': 'btoken=XW5ZWFLQC4GNC29CQ0WNORLRHNSR854E; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1748917495,1748998768; HMACCOUNT=F7B8C534891B7E31; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1749019827',
}
payload = {
    "sort": 1,
    "start": 100,
    "limit": 40
}
result_dict = js_compile.call('encrypt_data',payload)
f = result_dict['f']
sig = result_dict['sig']



json_data = {
    'payload': f,
    'sig': sig,
    'v': 1,
}

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

en_data = response.json().get('d')
# 解密逻辑
data = js_compile.call('decrypt_data',en_data)
for i in data['list']:
    print(i['name'])
