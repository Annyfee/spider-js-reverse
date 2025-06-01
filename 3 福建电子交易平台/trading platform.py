import base64
import json
import time
from hashlib import md5
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import requests

cookies = {
    'Hm_lvt_9d1de05cc99f08ddb5dc6d5e4d32ad30': '1748663404',
    'Hm_lvt_db393520fa240b442a13a6d1c5ae95c1': '1748663404',
    'Hm_lvt_94bfa5b89a33cebfead2f88d38657023': '1748663404',
    '_qddagsx_02095bad0b': '56513d8598483de2ed73aed55e8aabf16ed281359ea81cfc61624365ae344a225aa2e8fbb447be28a300aa106242e9f48e05fe34df0c36bacbe6032e8b8f02ad81410d23a71ce5843ca6f721bcf735d8c93cb2cd5dbdbb1c6e31796c45fc03f00c954367bc8f910a45a98e5f5d7489ea86a6f1c9abfc36a88deb16fd4b7b0141',
}

# 批量获取
for i_ in range(1, 21):
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

    # 加密逻辑
    def get_sign():
        # 排序
        sorted_items = dict(sorted(json_data.items()))
        a = ''
        for key_, value_ in sorted_items.items():
            if not value_:
                continue
            a += key_ + str(value_)
        # 合并
        b = 'B3978D054A72A7002063637CCDF6B2E5'
        c = b + a
        # 加入MD5
        obj = md5()
        obj.update(c.encode('utf8'))
        data_ = obj.hexdigest()
        return data_


    my_sign = get_sign()

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
        'portal-sign': my_sign,
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'Hm_lvt_9d1de05cc99f08ddb5dc6d5e4d32ad30=1748663404; Hm_lvt_db393520fa240b442a13a6d1c5ae95c1=1748663404; Hm_lvt_94bfa5b89a33cebfead2f88d38657023=1748663404; _qddagsx_02095bad0b=56513d8598483de2ed73aed55e8aabf16ed281359ea81cfc61624365ae344a225aa2e8fbb447be28a300aa106242e9f48e05fe34df0c36bacbe6032e8b8f02ad81410d23a71ce5843ca6f721bcf735d8c93cb2cd5dbdbb1c6e31796c45fc03f00c954367bc8f910a45a98e5f5d7489ea86a6f1c9abfc36a88deb16fd4b7b0141',
    }

    response = requests.post(
        'https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    data = response.json()
    # 解密逻辑
    # base64解码
    encrypt_data_bytes = base64.b64decode(data['Data'].encode())
    # 浏览器代码复现
    key = b'EB444973714E4A40876CE66BE45D5930'
    iv = b'B5A8904209931867'
    aes = AES.new(key, AES.MODE_CBC, iv)
    contents = json.loads(unpad(aes.decrypt(encrypt_data_bytes), 16).decode())
    # 从逆向网站得到的数据/加解密数据，一般都是json格式（字符串包裹），通常需要data.json()或者json.loads(xx)将其转化为py对象
    print(f'正在打印第{i_}页...')
    for i in contents['Table']:
        print(i['NAME'])
    time.sleep(random.uniform(0.4, 0.7))
print(f'打印完成!一共打印20页!')
