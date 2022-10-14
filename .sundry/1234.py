import requests


if __name__ == "__main__":
    # 定义url的地址
    url = r'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&'
    # 定义搜索内容
    kw = '秦国'
    param = {
        'wd': kw
    }
    # 伪装请求头
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}
    # 发起请求
    response = requests.get(url=url, params=param, headers=head)
    # 获取请求结果
    result = response.text
    # 定义储存结果的文件名
    filename = kw+'.html'
    # 存储文件
    with open(filename, 'w', encoding='utf-8') as tem:
        tem.write(result)
    print(filename, '保存成功')
    # 定义搜索内容
    kw = '秦国'
    param = {
        'wd': kw
    }
    # 伪装请求头
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}
    # 发起请求
    response = requests.get(url=url, params=param, headers=head)
    # 获取请求结果
    result = response.text
    # 定义储存结果的文件名
    filename = kw+'.html'
    # 存储文件
    with open(filename, 'w', encoding='utf-8') as tem:
        tem.write(result)
    print(filename, '保存成功')