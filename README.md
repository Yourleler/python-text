#人生的第一次python爬虫（doge
  此仓库储存的为三个爬虫，在下是初学者，如有不足，请多多包涵，如果没有安装python，可直接在EXE文件夹中下载应用直接使用，如果想调试，参考的使用库在末尾
## 知乎热榜爬虫
  此爬虫可定时爬取知乎小时热榜：[知乎热点](https://www.zhihu.com/creator/hot-question/hot/0/hour "知乎热点")，可生成包含相关一系列内容的Excel表格，以及显示今日热点的词云。
  **注意，克隆仓库的时候，请不要删除各个文件夹下的bj.jpg和simhei黑体字体及Stopwards，词云生成依赖此三者路径**



## 哔哩哔哩关注列表爬虫
此爬虫可以根据您输入的两者uid，从而找出两者的共同关注，同时会在表格的三个sheet中，分别展现共同关注列表以及两者的关注列表
*但是请注意，由于B站本身限制，只能抓取两人的可公开的前100关注，如果未显示共同关注，并不意味着实际上两者没有任何交集关注[责任全在B方（bushi）]*


## 沙袋本科院学术新闻抓取
可定时抓取[学术快讯](https://www.bkjx.sdu.edu.cn/index/jxkx.htm "学术快讯")上的内容
*本来应该是新闻网的但是我不在学校，山大把校外屏蔽了，挂梯子也不行，只能看到学术快讯，问了任哥就换这个了QAQ*


## 库列表
~~使用pip下载~~
Package                   Version
------------------------- -----------
- altgraph                  0.17.3
- async-generator           1.10
- attrs                     22.1.0
- beautifulsoup4            4.11.1
- bs4                       0.0.1
- certifi                   2022.9.24
- cffi                      1.15.1
- charset-normalizer        2.1.1
- contourpy                 1.0.5
- cycler                    0.11.0
- et-xmlfile                1.1.0
- exceptiongroup            1.0.0rc9
- fonttools                 4.37.4
- future                    0.18.2
- h11                       0.14.0
- idna                      3.4
- jieba                     0.42.1
- kiwisolver                1.4.4
- lxml                      4.9.1
- matplotlib                3.6.1
- numpy                     1.23.3
- openpyxl                  3.0.10
- outcome                   1.2.0
- packaging                 21.3
- pandas                    1.5.0
- pefile                    2022.5.30
- Pillow                    9.2.0
- pip                       22.2.2
- pycparser                 2.21
- trio                      0.22.0
- trio-websocket            0.9.2
- urllib3                   1.26.12
- wordcloud                 1.8.2.2
- wsproto                   1.2.0
- XlsxWriter                3.0.3
- xlwt                      1.3.0
