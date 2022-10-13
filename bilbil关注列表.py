import requests
print("请输入uid")
from bs4 import BeautifulSoup
uid = input()
cookies = {
    'buvid3': '9FE0BE0D-718E-0EEA-5696-75041DEAD8DA05300infoc',
    'b_nut': '1665296305',
    'i-wanna-go-back': '-1',
    'b_ut': '7',
    '_uuid': '410947A72-9C87-2E32-9D1F-10697101510CEDF06303infoc',
    'buvid4': '4C51E20C-055C-968E-DA8B-FF79F33545DB06158-022100914-Vvnd5zdoRgGxc5uFWJ1/kw%3D%3D',
    'fingerprint': '46bb08629b69b7557047db703feffb81',
    'buvid_fp_plain': 'undefined',
    'SESSDATA': '66e5c4c1%2C1680848337%2Cf1eea%2Aa1',
    'bili_jct': '1b61808a83fcef6d2d0bed9f6b47c43a',
    'DedeUserID': '290927498',
    'DedeUserID__ckMd5': '05d32a4d134e1426',
    'buvid_fp': '58aeb394e0cc43335b33769c39bedfad',
    'rpdid': '|(um~kR)lmk)0J\'uYYlkmYJl~',
    'CURRENT_FNVAL': '16',
    'bp_video_offset_290927498': '714925464409342000',
    'PVID': '1',
    'b_lsid': '319118AE_183CBC268C3',
}

headers = {
    'authority': 'space.bilibili.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'buvid3=9FE0BE0D-718E-0EEA-5696-75041DEAD8DA05300infoc; b_nut=1665296305; i-wanna-go-back=-1; b_ut=7; _uuid=410947A72-9C87-2E32-9D1F-10697101510CEDF06303infoc; buvid4=4C51E20C-055C-968E-DA8B-FF79F33545DB06158-022100914-Vvnd5zdoRgGxc5uFWJ1/kw%3D%3D; fingerprint=46bb08629b69b7557047db703feffb81; buvid_fp_plain=undefined; SESSDATA=66e5c4c1%2C1680848337%2Cf1eea%2Aa1; bili_jct=1b61808a83fcef6d2d0bed9f6b47c43a; DedeUserID=290927498; DedeUserID__ckMd5=05d32a4d134e1426; buvid_fp=58aeb394e0cc43335b33769c39bedfad; rpdid=|(um~kR)lmk)0J\'uYYlkmYJl~; CURRENT_FNVAL=16; bp_video_offset_290927498=714925464409342000; PVID=1; b_lsid=319118AE_183CBC268C3',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'referer': f"https://space.bilibili.com/{uid}/fans/follow"
}

response = requests.get(f'https://api.bilibili.com/x/relation/followings?vmid={uid}&pn=1&ps=20&order=desc&jsonp=jsonp&callback=__jp3', cookies=cookies, headers=headers)
page_text = response.text
result = response.text
filename = 'bl.js'
with open(filename, 'w', encoding='utf-8-sig') as tem:
    tem.write(result)
print(filename, '保存成功')
response.close()
print("close")