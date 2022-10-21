from dataclasses import replace
from encodings.utf_8 import encode
from http.client import ImproperConnectionState
from importlib.resources import path
from pyexpat import model
import requests
import re
import csv
from pandas.io.excel import ExcelWriter
import pandas as pd
import time
import sys
import os
import datetime
import schedule
from openpyxl import load_workbook

print("不在学校，挂梯子也打不开新闻网只能换这个了qaq，网址 https://www.bkjx.sdu.edu.cn/index/jxkx.htm")
def run():
    url = 'https://www.bkjx.sdu.edu.cn/index/jxkx.htm'
    u = ''

    headers = {
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cache-Control': 'max-age=0',
        # 'Connection': 'keep-alive',
        # 'Cookie': 'JSESSIONID=CDB1EF44CF3156A9FDC8D07645B98F42',
        # 'If-Modified-Since': 'Fri, 14 Oct 2022 07:19:29 GMT',
        # 'If-None-Match': '"4c2b-5eaf9725acf79-gzip"',
        # 'Sec-Fetch-Dest': 'document',
        # 'Sec-Fetch-Mode': 'navigate',
        # 'Sec-Fetch-Site': 'cross-site',
        # 'Sec-Fetch-User': '?1',
        # 'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8'
    result = response.text
    # filename = '沙袋.html'
    # with open(filename, 'w', encoding='utf-8') as tem:
    #     tem.write(result)
    # print(result)
    response.close()
    print("正在加载")
    a = 101
    #循环加载数据
    while a>93:
        url2 = f'https://www.bkjx.sdu.edu.cn/index/jxkx/{a}.htm'
        a = a-1
        response2 = requests.get(url=url2,headers=headers)
        response2.encoding = 'utf-8'
        result2 = response2.text
        result = result+result2
        u =result.replace('..','https://www.bkjx.sdu.edu.cn')
        #修改链接显示
    else:    
        print('读取成功')

    # filename = '沙袋.html'
    # with open(filename, 'w', encoding='utf-8') as tem:
    #     tem.write(result) 
    # response.close()

    obj1 = re.compile(r'<div style="float:left"><a href="(?P<链接>.*?)" target="_blank" title="(?P<标题>.*?)">.*?<div style="float:right;">(?P<发布日期>.*?)</div>',re.S)
    #正则处理数据
    it = obj1.finditer(u,re.S)

    # for i in it:
    #     print (i.group("标题"))
    # response.close()

    f = open("沙袋教学快讯.csv",mode="w",encoding='utf-8')
    csvwriter = csv.writer(f)
    for i in it:
        dic = i.groupdict()
        csvwriter.writerow(dic.values())
    f.close()
    df = pd.read_csv('沙袋教学快讯.csv',header=None,names=['链接','标题','发布日期'])    
    df.to_csv('沙袋教学快讯.csv',index=False)
    #加表头

    # data=pd.read_csv('教学快讯.csv')
    # data.replace(r'..',r'https://www.bkjx.sdu.edu.cn', regex=True)
    # data.to_csv("沙袋教学快讯.csv",index=False)
    #修改链接显示
    with ExcelWriter('沙袋教学快讯.xlsx') as ew:
    #转换为excel文件
   
        pd.read_csv("沙袋教学快讯.csv").to_excel(ew, sheet_name="1", index=False)
    
    path = '沙袋教学快讯.csv'
    path2 = '沙袋教学快讯.xlsx'
    #修改列宽
    wb = load_workbook(path2)
    ws = wb.active
    ws.column_dimensions['A'].width = 70
    ws.column_dimensions['B'].width = 95
    wb.save('沙袋教学快讯.xlsx')

    os.remove(path)

run()

print("每小时刷新一次哟，如果不需要可直接关闭此窗口或键入任意关闭")
schedule.every(60).minutes.do(run)
input()

print("close")
time.sleep(1)
# 每隔1h执行一次任务