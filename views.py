
# python3 抓取bing今日美图的所有背景图片
import requests
from pyquery import PyQuery as pq
 
def download(p):
    url = "http://bing.plmeizi.com/show/"+str(p)
    res = requests.get(url).text
    doc = pq(res)
    img_url = doc.find('#picurl').attr("href")
    print(i, img_url)
    if img_url:
        right = img_url.rindex('/')
        right1 = img_url.rindex('Z')
        name = img_url[right + 1:right1 - 1] + ".jpg"     # 修改图片名,去掉多余字段.
        img = requests.get(img_url).content
        with open(".\\Bing_Photos\\" + name, "wb") as f:     # 手动在程序同目录下建一个文件夹Bing_Photos,用于放置图片.
            f.write(img)
 
for i in range(890, 820, -1):     # 设置爬取天数，800对应日期20180805，依次增减即可。
    download(i)
 

