#from urllib import response
#from bs4 import BeautifulSoup
#url = 'https://www.zhihu.com/creator/hot-question/hot/0/hour'
from pyexpat import model
import requests
import re
import csv
from pandas.io.excel import ExcelWriter
import pandas as pd


url = 'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&period=hour'
offset = 20
url2 = f'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&limit=20&offset={offset}&period=hour'

#参数
cookies = {
    '_zap': 'f3cf59ab-0720-4f1f-95c7-71f1d634745b',
    'd_c0': 'AFDTyOf1rhWPTl8mcGV63yaFc5lXO5R0N6o=|1665298657',
    '_9755xjdesxxd_': '32',
    'YD00517437729195%3AWM_TID': 'H9AdI9GYO0tEFQEAFAKVTouOgIJVe9dQ',
    '_xsrf': 'BmljXDfZmr9gwEv0D3mKDgFn5EnSdXAD',
    'gdxidpyhxdE': 'r%5CDGypqOJUIjWByqCv0t3NsDsmOle1xqKqzC0fE9Pi6NsP%2FdeTQQvLnQhXjR0rZTs%2Bl339qGEhg7%2F6azK0c6E84uTVMT6SnvZwGBAcPwG6Y6E8elgjV%5CWZToPlxSC1u2gxLT00Hl1wVqjPd3RVLVQcCA%5CnKotEER%2F4NxeAnuTqsT%2Bo78%3A1665458489826',
    'YD00517437729195%3AWM_NI': 'Mg3bC4Qkx7L1rVqP3Ocq5FzxqV7LFU%2B7z4OrvL0l3VSYcPVyC2q7FQhiOotdt852Wu9y3%2FaYcZngiW1y0lx8NIbwTCD7IcAcTA7SZqSg%2FK%2BHGMWRPPESdzU%2BWtachRRFbE8%3D',
    'YD00517437729195%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6eeaded7ab38e8fb1ee5297b48fb2d44e968e9bb1d154b68ba7a2c83c8ca99ab2f52af0fea7c3b92a8fb9fd83c24093b5b8d8cf3bb28abfb1b245a1affba7f974b38af9adc55fe9e9b6d5ce7ab694008db25e9187adb1d57381eebfd8c55bacb78190f770b8e8fbd3d67ffba7fdd0e453a186a288ec5df3a7008dfb348e97ae98d74988e98784c469989ff9b4d97b91b9e1acaa44859399b3d35c878dac9bd82195acaf84eb5a929aaea6bb37e2a3',
    '__snaker__id': 'TkYb4ryLUrS3pwy2',
    'captcha_session_v2': '2|1:0|10:1665457604|18:captcha_session_v2|88:Z0UxTGNMY0xnNXdKc1EyNlRhMzYwaDNFc0RtQ2p6T1FlKzFhaDVneHlqMzdWVVhyOXYvUkNYUDJSQzZadStrSQ==|c19b7dfc6cfa0478f3978472f0c453f5a16f0689cc1c5b92ee6c718f944492f2',
    'q_c1': '7bcc06aed71b454b8e910ad001ef2b96|1665457693000|1665457693000',
    'z_c0': '2|1:0|10:1665457696|4:z_c0|92:Mi4xYjY2c0VRQUFBQUFBVU5QSTVfV3VGU1lBQUFCZ0FsVk5IQ3d5WkFCRzU0TGdmQVFaYUg4MkU0WHFuVm91Z3liSk9n|e28bf825a4575ad46c464b616cd8d51a3667bc35886a45f838454aa746367809',
    'tst': 'h',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1665298659,1665457588,1665501628',
    'KLBRSID': '3d7feb8a094c905a519e532f6843365f|1665565516|1665565516',
}

headers = {
    'authority': 'www.zhihu.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_zap=f3cf59ab-0720-4f1f-95c7-71f1d634745b; d_c0=AFDTyOf1rhWPTl8mcGV63yaFc5lXO5R0N6o=|1665298657; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=H9AdI9GYO0tEFQEAFAKVTouOgIJVe9dQ; _xsrf=BmljXDfZmr9gwEv0D3mKDgFn5EnSdXAD; gdxidpyhxdE=r%5CDGypqOJUIjWByqCv0t3NsDsmOle1xqKqzC0fE9Pi6NsP%2FdeTQQvLnQhXjR0rZTs%2Bl339qGEhg7%2F6azK0c6E84uTVMT6SnvZwGBAcPwG6Y6E8elgjV%5CWZToPlxSC1u2gxLT00Hl1wVqjPd3RVLVQcCA%5CnKotEER%2F4NxeAnuTqsT%2Bo78%3A1665458489826; YD00517437729195%3AWM_NI=Mg3bC4Qkx7L1rVqP3Ocq5FzxqV7LFU%2B7z4OrvL0l3VSYcPVyC2q7FQhiOotdt852Wu9y3%2FaYcZngiW1y0lx8NIbwTCD7IcAcTA7SZqSg%2FK%2BHGMWRPPESdzU%2BWtachRRFbE8%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeaded7ab38e8fb1ee5297b48fb2d44e968e9bb1d154b68ba7a2c83c8ca99ab2f52af0fea7c3b92a8fb9fd83c24093b5b8d8cf3bb28abfb1b245a1affba7f974b38af9adc55fe9e9b6d5ce7ab694008db25e9187adb1d57381eebfd8c55bacb78190f770b8e8fbd3d67ffba7fdd0e453a186a288ec5df3a7008dfb348e97ae98d74988e98784c469989ff9b4d97b91b9e1acaa44859399b3d35c878dac9bd82195acaf84eb5a929aaea6bb37e2a3; __snaker__id=TkYb4ryLUrS3pwy2; captcha_session_v2=2|1:0|10:1665457604|18:captcha_session_v2|88:Z0UxTGNMY0xnNXdKc1EyNlRhMzYwaDNFc0RtQ2p6T1FlKzFhaDVneHlqMzdWVVhyOXYvUkNYUDJSQzZadStrSQ==|c19b7dfc6cfa0478f3978472f0c453f5a16f0689cc1c5b92ee6c718f944492f2; q_c1=7bcc06aed71b454b8e910ad001ef2b96|1665457693000|1665457693000; z_c0=2|1:0|10:1665457696|4:z_c0|92:Mi4xYjY2c0VRQUFBQUFBVU5QSTVfV3VGU1lBQUFCZ0FsVk5IQ3d5WkFCRzU0TGdmQVFaYUg4MkU0WHFuVm91Z3liSk9n|e28bf825a4575ad46c464b616cd8d51a3667bc35886a45f838454aa746367809; tst=h; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1665298659,1665457588,1665501628; KLBRSID=3d7feb8a094c905a519e532f6843365f|1665565516|1665565516',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}


#response = requests.get('https://www.zhihu.com/hot', cookies=cookies, headers=headers)

response = requests.get(url=url, cookies=cookies,headers=headers)
#请求内容（第一页）
response.encoding = 'utf-8'
page_text = response.text
#print(response.text)
result = response.text
# filename = '知乎热榜.html'
# with open(filename, 'w', encoding='utf-8') as tem:
#     tem.write(result)
offset = 20
while offset<=200:

    url2 = f'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&limit=20&offset={offset}&period=hour'
    offset=offset+20
    response2 = requests.get(url=url2, cookies=cookies,headers=headers)
    result2 = response2.text
    result = result+result2
    # with open(filename, 'a', encoding='utf-8') as tem:
    #     tem.write(result2)
else:    
    print('读取成功')
#请求剩下的下拉内容


obj1 = re.compile(r'"url":"(?P<链接>.*?)","created":.*?"title":"(?P<标题>.*?)","highlight_title".*?"new_pv":(?P<浏览增量>.*?),"new_pv_7_days.*?"new_follow_num":(?P<关注增量>.*?),"new_follow_num_7_days":0,"new_answer_num":(?P<回答增量>.*?),"new_answer_num_7_days":0,"new_upvote_num":(?P<赞同增量>.*?),"new_upvote_num_7_days":0,"pv":(?P<总浏览>.*?),"follow_num":(?P<总关注>.*?),"answer_num":(?P<总回答>.*?),"upvote_num":(?P<总赞同>.*?),"pv_incr_rate":"0.00%".*?"score":(?P<热力值>.*?),"score_level".*?"text":""}},',re.S)
#正则处理数据
it = obj1.finditer(result,re.S)

# for i in it:
#     print (i.group("总赞同"))
response.close()
response2.close()


f = open("知乎热榜.csv",mode="w")
csvwriter = csv.writer(f)
for i in it:
    dic = i.groupdict()
    csvwriter.writerow(dic.values())

df = pd.read_csv('知乎热榜.csv',header=None,names=['链接','标题','浏览增量','关注增量','回答增量','赞同增量','总浏览','总关注','总回答','总赞同','热力值'])    
df.to_csv('知乎热榜.csv',index=False)
#加表头


with ExcelWriter('知乎热榜.xlsx') as ew:
    #转换为excel文件
	pd.read_csv("知乎热榜.csv").to_excel(ew, sheet_name="1", index=False)

from openpyxl import load_workbook

path = '知乎热榜.xlsx'

wb = load_workbook(path)
ws = wb.active
ws.column_dimensions['B'].width = 102

wb.save('知乎小时热榜.xlsx')


print("close")