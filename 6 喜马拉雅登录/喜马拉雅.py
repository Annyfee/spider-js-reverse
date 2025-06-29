import json
import time
import execjs
import requests
import subprocess

cookies = {
    '_xmLog': 'h5&7e5d2a08-fa32-4da9-8b9a-90396b4782b0&process.env.sdkVersion',
    'wfp': 'ACM1ZmM5ZWY3OTdlMGNiZTA4Wxfo3HRvJjd4bXdlYl93d3c',
    'Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070': '1750931827,1751010677',
    'trackType': 'web',
    'x_xmly_traffic': 'utm_source%3A%26utm_medium%3A%26utm_campaign%3A%26utm_content%3A%26utm_term%3A%26utm_from%3A',
    'impl': 'passport.ximalaya.com.web',
    's&e': 'a7ea9c6d0d3b113dfac48f542c3cd4da',
    's&a': '%1BP%0A%02W%04A%07J%0FX%05_RL%07%10%0A%08WV%09NWL%0CX%04%0AW%1F%02VZ_OZVWRLG^VYYWRC_',
    'fds_otp': '5538206756327733594',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://passport.ximalaya.com',
    'Pragma': 'no-cache',
    'Referer': 'https://passport.ximalaya.com/page/web/login?fromUri=https%3A%2F%2Fstudio.ximalaya.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': '_xmLog=h5&7e5d2a08-fa32-4da9-8b9a-90396b4782b0&process.env.sdkVersion; wfp=ACM1ZmM5ZWY3OTdlMGNiZTA4Wxfo3HRvJjd4bXdlYl93d3c; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1750931827,1751010677; trackType=web; x_xmly_traffic=utm_source%3A%26utm_medium%3A%26utm_campaign%3A%26utm_content%3A%26utm_term%3A%26utm_from%3A; impl=passport.ximalaya.com.web; s&e=a7ea9c6d0d3b113dfac48f542c3cd4da; s&a=%1BP%0A%02W%04A%07J%0FX%05_RL%07%10%0A%08WV%09NWL%0CX%04%0AW%1F%02VZ_OZVWRLG^VYYWRC_; fds_otp=5538206756327733594',
}

params = {
    'fromUri': 'https%3A%2F%2Fstudio.ximalaya.com',
}

# 获取nonce
def get_nonce():
    t = int(time.time() * 1000)
    ret = requests.get(f'https://passport.ximalaya.com/web/nonce/{t}', cookies=cookies, headers=headers,params=params).json()
    nonce = ret['nonce']
    return nonce


# 获取传递值account与password
def get_encrypt(account,password):
    all_ = subprocess.check_output(f'node get_sign.js "{account}" "{password}"') # 分别获得传递
    all_ = all_.decode('utf8').strip()
    # 通过json传递取出对应值
    js_data = json.loads(all_)
    account = js_data['account']
    pwd = js_data['pwd']
    return account,pwd

# 获取signature
def get_signature(enc_account, enc_password,nonce_val):
    js_compile = execjs.compile(open('sign.js',encoding='utf8').read())
    data = {
            'account': enc_account,
            'password': enc_password,
            'nonce': nonce_val
        }
    signature = js_compile.call('getSignature',data)
    return signature

def login(enc_account,enc_password,nonce,signature):
    json_data = {
        'account': enc_account,
        'password':enc_password,
        'nonce':nonce,
        'signature': signature
    }
    response = requests.post(
        'https://passport.ximalaya.com/web/login/pwd/v2',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    return response.text


if __name__ == '__main__':
    account = '123456789'
    password = '123456'
    cur_nonce = get_nonce()
    enc_account,enc_pwd = get_encrypt(account, password)
    signature = get_signature(enc_account,enc_pwd,cur_nonce)
    ret = login(enc_account,enc_pwd,cur_nonce,signature)
    print(ret)