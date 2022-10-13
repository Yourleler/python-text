from re import S
from urllib import response
import requests

url = "https://fanyi.baidu.com/sug"

s = input("输入")

dat = {
    "kw":s
    }
response = requests.post(url,data=dat)
print(response.json())
response.close()