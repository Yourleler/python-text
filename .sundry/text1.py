import requests

# 设置用户代理
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
# 构造请求参数
params = {
    'ie': 'UTF-8',
    'q': 'Python'
}
# 获取响应
r = requests.get('https://www.google.com/search?q=EVA', headers=headers, params=params)

print(r.text)
