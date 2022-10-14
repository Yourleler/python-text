from ast import pattern
from pdb import line_prefix
import string
from tokenize import group
import requests
from bs4 import BeautifulSoup
import re
import csv
from http.client import ImproperConnectionState
from pyexpat import model
from pandas.io.excel import ExcelWriter
import pandas as pd
import numpy as np
import time
import sys
import os
import datetime


print("请输入两人uid,用空格空开")
uid,uid2 = map(int,input().split())

#一堆参数，伪装浏览器
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
headers2 = {
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
    'referer': f"https://space.bilibili.com/{uid2}/fans/follow"
}


cookies2 = {
    'buvid3': 'CE713CA7-9FF2-3046-FB7F-2C9D9E6FE81392972infoc',
    'i-wanna-go-back': '-1',
    '_uuid': '1FD710799-D1099-3157-2223-5BB175F2C15293130infoc',
    'CURRENT_BLACKGAP': '0',
    'rpdid': '|(um~kR)l)mm0J\'uYY|ukJum)',
    'buvid_fp_plain': 'undefined',
    'DedeUserID': '290927498',
    'DedeUserID__ckMd5': '05d32a4d134e1426',
    'SESSDATA': 'ccc2dc1c%2C1675675403%2C93bd3*81',
    'bili_jct': '7c4ba74ee792d0236c09565fa9d72e0d',
    'nostalgia_conf': '-1',
    'b_ut': '5',
    'hit-dyn-v2': '1',
    'LIVE_BUVID': 'AUTO7016613261424954',
    'CURRENT_QUALITY': '0',
    'b_nut': '100',
    'fingerprint3': '2146050fb11d0033b539475be262473c',
    'buvid4': 'EFAE8712-A096-C6BA-4002-CE0357D728AD94507-022080917-Vvnd5zdoRgE5y1W%2FN%2FmkTQ%3D%3D',
    'fingerprint': '090c42ada1773c0c9272346edac82afc',
    'buvid_fp': '693fa8c67a1f18dbb91e0bb66ceff11d',
    'sid': '8jpywscc',
    'bp_video_offset_290927498': '716735745860042800',
    'CURRENT_FNVAL': '4048',
    'PVID': '2',
    'innersign': '1',
    'b_lsid': '22EED43C_183D59D102F',
}

headers2 = {
    'authority': 'space.bilibili.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'buvid3=CE713CA7-9FF2-3046-FB7F-2C9D9E6FE81392972infoc; i-wanna-go-back=-1; _uuid=1FD710799-D1099-3157-2223-5BB175F2C15293130infoc; CURRENT_BLACKGAP=0; rpdid=|(um~kR)l)mm0J\'uYY|ukJum); buvid_fp_plain=undefined; DedeUserID=290927498; DedeUserID__ckMd5=05d32a4d134e1426; SESSDATA=ccc2dc1c%2C1675675403%2C93bd3*81; bili_jct=7c4ba74ee792d0236c09565fa9d72e0d; nostalgia_conf=-1; b_ut=5; hit-dyn-v2=1; LIVE_BUVID=AUTO7016613261424954; CURRENT_QUALITY=0; b_nut=100; fingerprint3=2146050fb11d0033b539475be262473c; buvid4=EFAE8712-A096-C6BA-4002-CE0357D728AD94507-022080917-Vvnd5zdoRgE5y1W%2FN%2FmkTQ%3D%3D; fingerprint=090c42ada1773c0c9272346edac82afc; buvid_fp=693fa8c67a1f18dbb91e0bb66ceff11d; sid=8jpywscc; bp_video_offset_290927498=716735745860042800; CURRENT_FNVAL=4048; PVID=2; innersign=1; b_lsid=22EED43C_183D59D102F',
    'referer': 'https://www.bilibili.com/',
    'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
}

#两者的数据抓取
response = requests.get(f'https://api.bilibili.com/x/relation/followings?vmid={uid}&pn=1&ps=20&order=desc&jsonp=jsonp&callback=__jp3', cookies=cookies, headers=headers)
result = response.text
jp = 5
a = 2
while jp<=8:
    response2 = requests.get(f'https://api.bilibili.com/x/relation/followings?vmid={uid}&pn={a}&ps=20&order=desc&jsonp=jsonp&callback=__jp{jp}', cookies=cookies, headers=headers)
    jp=jp+1
    a = a+1
    result2 = response2.text
    result=result+result2
    response2.close()
else:
    print(f"{uid}加载完毕")


response3 = requests.get(f'https://api.bilibili.com/x/relation/followings?vmid={uid2}&pn=1&ps=20&order=desc&jsonp=jsonp&callback=__jp3', cookies=cookies, headers=headers2)
result3 = response3.text
response3.close()
jp2 = 5
b=2
while jp2<=8:
    response4 = requests.get(f'https://api.bilibili.com/x/relation/followings?vmid={uid2}&pn={b}&ps=20&order=desc&jsonp=jsonp&callback=__jp{jp2}', cookies=cookies, headers=headers2)
    jp2=jp2+1
    b=b+1
    result4 = response4.text
    result3=result3+result4
    response4.close()

else:
    print(f"{uid2}加载完毕")

result = result+result3
# filename = 'bl.html'
# with open(filename, 'w', encoding='utf-8-sig') as tem:
#     tem.write(result)
# print(filename, '保存成功')
print("二者数据载入成功")
obj1 = re.compile(r'"mid":(.*?),"attribute"',re.S)
list1 = obj1.findall(result)
list1 = list(map(int,list1))

same = []
list1.sort()
#print (list1)
n = len(list1)
#print(n)
q = 0
p=q+1
while p<n:
    b=list1[q]
    c=list1[p]
    if b==c:
        same.append(list1[q])
    q = q+1
    p=q+1

else:
    print("正在查找共同关注信息~")


j = len(same)

if j == 0:
    print("没有发现两者有共同关注呢，目前来说某个蒙古上单限制每人只能获取前100个关注，可能这两个有，但是我们看不到吧（也可能是）")


if j != 0:
    e = 0
    while e<j:
        uid_ = same[e]
        response_0 = requests.get(f'https://api.bilibili.com/x/space/acc/info?mid={uid_}&token=&platform=web&jsonp=jsonp', cookies=cookies2, headers=headers2)
        response_1 = requests.get(f'https://api.bilibili.com/x/relation/stat?vmid={uid_}&jsonp=jsonp', cookies=cookies2, headers=headers2)
        response_2 = requests.get(f'https://api.bilibili.com/x/space/upstat?mid={uid_}&jsonp=jsonp', cookies=cookies2, headers=headers2)
        result_0 = response_0.text
        result_1 = response_1.text
        result_2 = response_2.text
        result_0 = result_0+result_1+result_2
        result_ = "a"
        result_ = result_+result_0
        e = e+1
        response_0.close()
        response_1.close()
        response_2.close()
    else: l = 1
obj2 = re.compile(r'"mid":(?P<uid>.*?),"name":"(?P<昵称>.*?)","sex":"(?P<性别>.*?)","face":"(?P<头像图片链接>.*?)","face_nft".*?"sign":".*?",".*?"level":(?P<等级>.*?),"jointime.*?"following":(?P<关注数>.*?),"whisper".*?"follower":(?P<粉丝>.*?)}}.*?"archive":{"view":(?P<播放数>.*?)},"article":{"view":(?P<阅读数>.*?)},"likes":(?P<获赞>.*?)}}',re.S)
it = obj2.finditer(result_,re.S)


f =open("bilibili共同关注列表.csv",mode="w",encoding='utf-8')
csvwriter = csv.writer(f)   
for i in it:
    dic = i.groupdict()
    csvwriter.writerow(dic.values())
f.close()
df = pd.read_csv('bilibili共同关注列表.csv',header=None,names=['uid','昵称','性别','头像图片链接','等级','关注数','粉丝','播放数','阅读数','获赞'])    
df.to_csv('bilibili共同关注列表.csv',index=False)
     #加表头
with ExcelWriter('bilibili共同关注列表.xlsx') as ew:
 #转换为excel文件
    pd.read_csv("bilibili共同关注列表.csv").to_excel(ew, sheet_name="1",index=False,engine = "python")
from openpyxl import load_workbook

path = 'bilibili共同关注列表.csv'



#print(list1)
#uid_list = obj1.finditer(result)

# for i in uid_list:
#     print(i.group("uid"))

# f = open("uid1.csv",mode="w")
# csvwriter = csv.writer(f)
# for i in uid_list:
#     dic = i.groupdict()
#     csvwriter.writerow(dic.values())

response.close()
response3.close()
response_0.close()
response_1.close()
response_2.close()

os.remove(path)
print("若两者有共同关注，bilibili共同关注列表已生成，位置在bilibili关注列表.py同一根目录下")
print("按任意键退出")
o = input()
print("close")