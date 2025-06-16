import re
import time

import requests
import execjs
from bs4 import BeautifulSoup

js_compile = execjs.compile(open('get_sign.js',encoding='utf8').read())

cookies = {
    'enable_web_push': 'DISABLE',
    'DedeUserID': '110713353',
    'DedeUserID__ckMd5': '218ee02179168e75',
    'header_theme_version': 'CLOSE',
    'buvid_fp_plain': 'undefined',
    'is-2022-channel': '1',
    'dy_spec_agreed': '1',
    'CURRENT_BLACKGAP': '0',
    'home_feed_column': '5',
    'buvid3': '3E1D591F-D8D7-D363-1BB3-CC4DA6F8305087289infoc',
    'b_nut': '1736164785',
    '_uuid': '2FAD558C-9A64-9897-E27B-B4BFA6172C8788596infoc',
    'buvid4': '18125705-E487-7FAF-6DDB-9F2E9783671831343-024010711-Nedwr1bULbqfpPsq%2F5Lm5w%3D%3D',
    'hit-dyn-v2': '1',
    'rpdid': "|(k|k)kmkYmk0J'u~JmumRkJ|",
    'enable_feed_channel': 'ENABLE',
    'LIVE_BUVID': 'AUTO6517437776449195',
    'browser_resolution': '1536-703',
    'CURRENT_QUALITY': '112',
    'SESSDATA': '1ce3b432%2C1764668707%2C495b5%2A62CjAJPZOu_XwPDfR8A6Sqhr4HnuTbUeP3kLNJraEg5sDhXOGn6snZpJlK04vXxNgUkY0SVk1ockpBUEpLdmVuRzNzOEhSZDY2VUJib3lqUE50NWREWE9CMlhNMWx0cFNBQUxSZFE1QTZYZ0F6dFp3X05GNDJJaVBpdHJ2S240QmRGMmJKVjhxcjdBIIEC',
    'bili_jct': 'a297982882bca698e91cdb7d06707aa9',
    'sid': '643dnydx',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDkzODg3NDYsImlhdCI6MTc0OTEyOTQ4NiwicGx0IjotMX0.jHZt-GOwZNOdwXdRFKUfoo_2f363Z2VciGfwO3OEPHI',
    'bili_ticket_expires': '1749388686',
    'share_source_origin': 'copy_web',
    'bsource': 'share_source_copylink_web',
    'fingerprint': '9b0b3d549e1f32e70f6dc9bb567f65aa',
    'buvid_fp': '9b0b3d549e1f32e70f6dc9bb567f65aa',
    'PVID': '1',
    'b_lsid': 'BAFDAF76_1974E9B8B6F',
    'bp_t_offset_110713353': '1076027768803688448',
    'CURRENT_FNVAL': '2000',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'origin': 'https://search.bilibili.com',
    'priority': 'u=1, i',
    'referer': 'https://search.bilibili.com/all?vt=71277623&keyword=%E8%8B%B9%E6%9E%9C&from_source=webtop_search&spm_id_from=333.1007&search_source=5&page=2&o=30',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    # 'cookie': "enable_web_push=DISABLE; DedeUserID=110713353; DedeUserID__ckMd5=218ee02179168e75; header_theme_version=CLOSE; buvid_fp_plain=undefined; is-2022-channel=1; dy_spec_agreed=1; CURRENT_BLACKGAP=0; home_feed_column=5; buvid3=3E1D591F-D8D7-D363-1BB3-CC4DA6F8305087289infoc; b_nut=1736164785; _uuid=2FAD558C-9A64-9897-E27B-B4BFA6172C8788596infoc; buvid4=18125705-E487-7FAF-6DDB-9F2E9783671831343-024010711-Nedwr1bULbqfpPsq%2F5Lm5w%3D%3D; hit-dyn-v2=1; rpdid=|(k|k)kmkYmk0J'u~JmumRkJ|; enable_feed_channel=ENABLE; LIVE_BUVID=AUTO6517437776449195; browser_resolution=1536-703; CURRENT_QUALITY=112; SESSDATA=1ce3b432%2C1764668707%2C495b5%2A62CjAJPZOu_XwPDfR8A6Sqhr4HnuTbUeP3kLNJraEg5sDhXOGn6snZpJlK04vXxNgUkY0SVk1ockpBUEpLdmVuRzNzOEhSZDY2VUJib3lqUE50NWREWE9CMlhNMWx0cFNBQUxSZFE1QTZYZ0F6dFp3X05GNDJJaVBpdHJ2S240QmRGMmJKVjhxcjdBIIEC; bili_jct=a297982882bca698e91cdb7d06707aa9; sid=643dnydx; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDkzODg3NDYsImlhdCI6MTc0OTEyOTQ4NiwicGx0IjotMX0.jHZt-GOwZNOdwXdRFKUfoo_2f363Z2VciGfwO3OEPHI; bili_ticket_expires=1749388686; share_source_origin=copy_web; bsource=share_source_copylink_web; fingerprint=9b0b3d549e1f32e70f6dc9bb567f65aa; buvid_fp=9b0b3d549e1f32e70f6dc9bb567f65aa; PVID=1; b_lsid=BAFDAF76_1974E9B8B6F; bp_t_offset_110713353=1076027768803688448; CURRENT_FNVAL=2000",
}
wts = int(time.time()*1000)
w_rid = js_compile.call('get_w_rid',wts)
qv_id = js_compile.call('get_qv_id','')
keyword = input('您要搜索的关键字是:')
# page = input('您要打印的数据页数是:')
params = {
    'category_id': '',
    'search_type': 'video',
    'ad_resource': '5654',
    '__refresh__': 'true',
    '_extra': '',
    'context': '',
    'page': '1',
    'page_size': '42',
    'pubtime_begin_s': '0',
    'pubtime_end_s': '0',
    'from_source': '',
    'from_spmid': '333.337',
    'platform': 'pc',
    'highlight': '1',
    'single_column': '0',
    'keyword': keyword,
    'qv_id': qv_id,
    'source_tag': '3',
    'gaia_vtoken': '',
    'dynamic_offset': '30',
    'page_exp': '0',
    'web_location': '1430654',
    'w_rid': w_rid,
    'wts': wts,
}

response = requests.get(
    'https://api.bilibili.com/x/web-interface/wbi/search/type',
    params=params,
    cookies=cookies,
    headers=headers,
)

res =response.json()
print(res)
result = res['data']['result']
pattern = r'(?:[“《])?\s*<em\s+class="keyword">.*?<\/em>\s*(?:[”》])?'



for i,x in enumerate(result):
    print(f'第{i}个数据...')
    soup = BeautifulSoup(x['title'],'html.parser')
    for em in soup.find_all('em',class_='keyword'):
        em.replace_with('')
    clean_title = str(soup).strip()
    print('标题：',clean_title)
    print('链接：',x['arcurl'])
    print('bv号：',x['bvid'])
    print('-'*50)

