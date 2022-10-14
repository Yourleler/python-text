from curses import savetty
from fileinput import filename
from unittest import result
import pandas as pd
import datetime
url="https://api.bilibili.com/x/relation/followings?vmid=5102641&pn=1&ps=20&order=desc&jsonp=jsonp&callback=__jp3"
headers={
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Content-Type': 'application/json; charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56',
}
headers['Cookie']=""# 填入相应的Cookie才会显示是否是特别关心，否则这一栏看不到(只能看自己的)
params={
    'vmid':'2206456',
    'pn': '1',
    'ps': '1',
    'order':'desc',
    'jsonp':'jsonp'
}
datalist = []  #用来存储爬取的网页信息
byYourself={
    'number':50, # 由于b站限制，最多访问前5页，每次申请最多数量50，所以最多爬取250个关注者
    'vmid': ['2206456','437662663'] # 你想爬取的用户的bid列表
}

def AddData(content):
    for i in content['data']['list']:
        AddContent=i
        datalist.append(AddContent)
    #print(len(datalist))
def export_excel(export):
    #将字典列表转换为DataFrame
    pf = pd.DataFrame(list(export))
    #指定字段顺序
    order = ['mid','uname','sign','special']
    pf = pf[order]
    #将列名替换为中文
    columns_map = {
        'mid': 'bid',
        'uname': '名字',
        'sign': '个签',
        'special': '是否特别关心',
    }
    pf.rename(columns=columns_map, inplace=True)
    #指定生成的Excel表格名称
    file_path = pd.ExcelWriter(str(params['vmid'])+'的关注列表'+str(datetime.date.today())+'.xlsx')
    #替换空单元格
    pf.fillna(' ', inplace=True)
    #输出
    pf.to_excel(file_path, encoding='utf-8', index=False)
    #保存表格
    filename = '123456.xlsx'
with save(filename, 'w', encoding='utf-8') as tem:
    tem.write(pf)


