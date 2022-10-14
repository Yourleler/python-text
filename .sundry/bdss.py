#from urllib import response
import requests

url = 'https://www.baidu.com/s?wd=eva&rsv_spt=1&rsv_iqid=0xcd9573450003990d&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_dl=tb&rsv_enter=1&rsv_sug3=5&rsv_sug1=3&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=eva&rsp=5&inputT=1621&rsv_sug4=2834'

cookies = {
    'BIDUPSID': '052789B7A4B107710035B4A57F3E1C05',
    'PSTM': '1660717246',
    'BAIDUID': '0191E88B630C8FBA994374EA29694AC0:FG=1',
    'BDUSS': 'xsVnJXM0NmZDhzVn5xTjVQRzRHakpTOWJiNEU1OWFYZzNwZFExQ012STBHaVJqRVFBQUFBJCQAAAAAAAAAAAEAAADTIjmF19Hhus3yy-pjcnkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADSN~GI0jfxiNU',
    'BDUSS_BFESS': 'xsVnJXM0NmZDhzVn5xTjVQRzRHakpTOWJiNEU1OWFYZzNwZFExQ012STBHaVJqRVFBQUFBJCQAAAAAAAAAAAEAAADTIjmF19Hhus3yy-pjcnkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADSN~GI0jfxiNU',
    'newlogin': '1',
    'BD_UPN': '12314753',
    'COOKIE_SESSION': '412_0_4_5_1_6_1_0_4_4_1_1_0_0_0_0_1665421557_0_1665421966%7C5%230_0_1665421966%7C1',
    'BA_HECTOR': '0ha40h8k0l0l0l858l0gbvd91hk8kkj1a',
    'BAIDUID_BFESS': '0191E88B630C8FBA994374EA29694AC0:FG=1',
    'ZFY': 'gSHXe8SofYukQYKxj3Aw4ciKEdo5YOnMUGboJ9tIGK0:C',
    'BD_HOME': '1',
    'delPer': '0',
    'BD_CK_SAM': '1',
    'PSINO': '1',
    'H_PS_PSSID': '36543_37561_37550_37359_37345_37486_37402_36804_36789_37498_26350_37488_37351',
    'H_PS_645EC': '094ekqsR5nF4fyC5PGB2Icwl83IBPzSgfed%2FmpTNq6sW8tkVA8XkmMGo9E72pJnYcwSb',
    'channel': 'bing',
    'BDRCVFR[feWj1Vr5u3D]': 'mk3SLVN4HKm',
    'BDSVRTM': '25',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'BIDUPSID=052789B7A4B107710035B4A57F3E1C05; PSTM=1660717246; BAIDUID=0191E88B630C8FBA994374EA29694AC0:FG=1; BDUSS=xsVnJXM0NmZDhzVn5xTjVQRzRHakpTOWJiNEU1OWFYZzNwZFExQ012STBHaVJqRVFBQUFBJCQAAAAAAAAAAAEAAADTIjmF19Hhus3yy-pjcnkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADSN~GI0jfxiNU; BDUSS_BFESS=xsVnJXM0NmZDhzVn5xTjVQRzRHakpTOWJiNEU1OWFYZzNwZFExQ012STBHaVJqRVFBQUFBJCQAAAAAAAAAAAEAAADTIjmF19Hhus3yy-pjcnkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADSN~GI0jfxiNU; newlogin=1; BD_UPN=12314753; COOKIE_SESSION=412_0_4_5_1_6_1_0_4_4_1_1_0_0_0_0_1665421557_0_1665421966%7C5%230_0_1665421966%7C1; BA_HECTOR=0ha40h8k0l0l0l858l0gbvd91hk8kkj1a; BAIDUID_BFESS=0191E88B630C8FBA994374EA29694AC0:FG=1; ZFY=gSHXe8SofYukQYKxj3Aw4ciKEdo5YOnMUGboJ9tIGK0:C; BD_HOME=1; delPer=0; BD_CK_SAM=1; PSINO=1; H_PS_PSSID=36543_37561_37550_37359_37345_37486_37402_36804_36789_37498_26350_37488_37351; H_PS_645EC=094ekqsR5nF4fyC5PGB2Icwl83IBPzSgfed%2FmpTNq6sW8tkVA8XkmMGo9E72pJnYcwSb; channel=bing; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; BDSVRTM=25',
    'Referer': 'https://cn.bing.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37',
    'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'wd': 'eva',
    'rsv_spt': '1',
    'rsv_iqid': '0xcd9573450003990d',
    'issp': '1',
    'f': '8',
    'rsv_bp': '1',
    'rsv_idx': '2',
    'ie': 'utf-8',
    'tn': 'baiduhome_pg',
    'rsv_dl': 'tb',
    'rsv_enter': '1',
    'rsv_sug3': '5',
    'rsv_sug1': '3',
    'rsv_sug7': '100',
    'rsv_sug2': '0',
    'rsv_btype': 'i',
    'prefixsug': 'eva',
    'rsp': '5',
    'inputT': '1621',
    'rsv_sug4': '2834',
}

#response = requests.get('https://www.zhihu.com/hot', cookies=cookies, headers=headers)

response = requests.get(url=url, params=params,cookies=cookies,headers=headers)
response.encoding = 'utf-8'
page_text = response.text

print(response.json())
result = response.text
filename = '123456.html'
with open(filename, 'w', encoding='utf-8') as tem:
    tem.write(result)
print(filename, '保存成功')
response.close()