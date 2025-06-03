import requests
import execjs

cookies = {
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22196d87b86801d1b-00ee29281a685dd8-26011f51-1327104-196d87b86811b11%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk2ZDg3Yjg2ODAxZDFiLTAwZWUyOTI4MWE2ODVkZDgtMjYwMTFmNTEtMTMyNzEwNC0xOTZkODdiODY4MTFiMTEifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22196d87b86801d1b-00ee29281a685dd8-26011f51-1327104-196d87b86811b11%22%7D',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.dewu.com',
    'Referer': 'https://www.dewu.com/',
    'SK': '',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'ltk': 'PMK3w7bDosOiZMKRw67Co8KTDMKnwpfDnMO6XcOmwpbCncKlNDTCnnjDmMOrKcONLHnDjwjCrSjCsMKywq9pd8OtRW/CqMOzw5PDu8O+wojCosON',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sessionid': 'a3nnv21x-rovg-zhlj-knwr-om5gbsfyewxpmklh',
    'shumeiId': '20250516174456a60ff58feef2467ef73543e8f87d33e000c0bed7edc59a50',
    'traceparent': '00-f5a6e3306827094394a1302736c79e69-3e068c66d55d847c-01',
    # 'Cookie': 'sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22196d87b86801d1b-00ee29281a685dd8-26011f51-1327104-196d87b86811b11%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk2ZDg3Yjg2ODAxZDFiLTAwZWUyOTI4MWE2ODVkZDgtMjYwMTFmNTEtMTMyNzEwNC0xOTZkODdiODY4MTFiMTEifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22196d87b86801d1b-00ee29281a685dd8-26011f51-1327104-196d87b86811b11%22%7D',
}

json_data = {
    # 'sign': 'f2b6b4c666227d52fdadf251f307445d',
    'pickRuleId': 644479,
    'pageNum': 1,
    'pageSize': 24,
    'filterUnbid': True,
    'showCspu': True,
}

sign = execjs.compile(open('dewu.js',encoding='utf8').read()).call("c",json_data)
print('sign:',sign)
json_data['sign'] = sign

response = requests.post(
    'https://app.dewu.com/api/v1/h5/commodity-pick-interfaces/pc/pick-rule-result/feeds/info',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.text)

# AES DES RSA会用加密算法--即encrypt  其它摘要算法如md5 sha1是不会用到这个关键字的\
# 关键字越泛越不是好词，大概率搜出一大堆 这里的可以sign可以试试写作sign=/sign:/sign( 减少搜索量

# 断点断到了 接着测有没有上述这些算法的属性 这里t作为属性是网页的页面，所以可以在控制台多测，看是否是对应我想要的参数  不然有可能请求都对应错
# 最后选中c(e) 发现就是我们想要的入口定位md5