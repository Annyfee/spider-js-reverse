from hashlib import md5
import execjs


# obj = md5()
# obj.update('123456'.encode('utf8'))
# pwd = obj.hexdigest()
# print(pwd)
pwd_data = '123456'
pwd =execjs.compile(open('gongzhonghao.js',encoding='utf8').read()).call('getPwd',pwd_data)
print(pwd)
import requests

username = '123456'

cookies = {
    'ptcz': 'd6431faf4ef6cdf39b7189e47d934a848515a3f91952b4ba620e8b1496c9379d',
    'pgv_pvid': '1488977493',
    '_qimei_uuid42': '189061322001003a3a86b16ed843c4f87c17368e6a',
    'pac_uid': '0_zy37DafNh4E1w',
    '_qimei_fingerprint': '901302a8f4eb05b6788999de9e59fecb',
    '_qimei_h38': 'e147d01a3a86b16ed843c4f80200000ba18906',
    'logTrackKey': '7592e65a4dfc46fb883cc06910a9b0f5',
    'ETCI': '50916fe3d87d45c3a148856580b21f53',
    'eas_sid': 'q1G7E380I2V8V1f8x6m1k2a8O4',
    '_uetvid': '16a195f09b7b11ef84c7279a81f32bb5',
    '_qimei_q32': '2cd6a7a473fdb6557ee90e159703911b',
    '_qimei_q36': '7305b9c51af4a61a451b679130001d91890d',
    'Qs_lvt_323937': '1736775439',
    'Qs_pv_323937': '3711180309161474600',
    'ptui_loginuin': '2287551746',
    'poc_sid': 'HHh3D2ijfNjIVz8E-HqF9ykyI9-JkqM_qzRjG-fR',
    'RK': 'yb1I0bsryI',
    'ua_id': 'LiWGttR9fszfJCMjAAAAAN77-c9TX8-ikoIOGoegFwo=',
    '_clck': '1i8736e|1|fw9|0',
    'wxuin': '48345124638297',
    'uuid': '60daa144791404fcf79e8d41c0a3c246',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://mp.weixin.qq.com',
    'priority': 'u=1, i',
    'referer': 'https://mp.weixin.qq.com/',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'ptcz=d6431faf4ef6cdf39b7189e47d934a848515a3f91952b4ba620e8b1496c9379d; pgv_pvid=1488977493; _qimei_uuid42=189061322001003a3a86b16ed843c4f87c17368e6a; pac_uid=0_zy37DafNh4E1w; _qimei_fingerprint=901302a8f4eb05b6788999de9e59fecb; _qimei_h38=e147d01a3a86b16ed843c4f80200000ba18906; logTrackKey=7592e65a4dfc46fb883cc06910a9b0f5; ETCI=50916fe3d87d45c3a148856580b21f53; eas_sid=q1G7E380I2V8V1f8x6m1k2a8O4; _uetvid=16a195f09b7b11ef84c7279a81f32bb5; _qimei_q32=2cd6a7a473fdb6557ee90e159703911b; _qimei_q36=7305b9c51af4a61a451b679130001d91890d; Qs_lvt_323937=1736775439; Qs_pv_323937=3711180309161474600; ptui_loginuin=2287551746; poc_sid=HHh3D2ijfNjIVz8E-HqF9ykyI9-JkqM_qzRjG-fR; RK=yb1I0bsryI; ua_id=LiWGttR9fszfJCMjAAAAAN77-c9TX8-ikoIOGoegFwo=; _clck=1i8736e|1|fw9|0; wxuin=48345124638297; uuid=60daa144791404fcf79e8d41c0a3c246',
}

params = {
    'action': 'startlogin',
}

data = {
    'username': username,
    'pwd': pwd,
    'verify_ticket': '',
    'rand_str': '',
    'f': 'json',
    'userlang': 'zh_CN',
    'redirect_url': '',
    'fingerprint': '51b8e2593b2653f98af536180c97c835',
    'token': '',
    'lang': 'zh_CN',
    'ajax': '1',
}

response = requests.post('https://mp.weixin.qq.com/cgi-bin/bizlogin', params=params, cookies=cookies, headers=headers, data=data)
print(response.text)