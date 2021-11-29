#抓取ptt stock的html
import urllib.request as req
url = "https://www.ptt.cc/bbs/Stock/index.html"


#建立request物件，附加Request Header的資訊
#f12/network/index.html/Headers/user agent  Request Headers = 一般使用者使用連線時會發送的資訊，ppt才會認為我們是正常的使用者
request = req.Request(url, headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
})


with req.urlopen(request) as response:  #利用request物件打開網址
    data = response.read().decode("utf-8")

# print(data)         #延伸問題: 如果網頁跳出18歲選項，如何選擇18以上後再取得網頁資料???
#解析原始碼取得每篇文章的標題

import bs4
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_= "title")   #尋找class = title(篩選條件) 的 div 標籤
for title in titles:
    if title.a != None:         #如果標題包含a標籤(沒有被刪除)，印出來
        print(title.a.string)
