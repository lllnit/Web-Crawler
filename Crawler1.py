#觀察進入網站的程序，模仿他
#f12/application/cookies/over18   按下over18同意,此cookie就會出現,並記錄 讓我們下次進入網站不用再點選
#f12/Network/index.html/Headers/Request Headers/Cookies/over18 = 1, 把存放在遊覽器中的cookies送回伺服器，讓伺服器判斷是否要再顯示一次確認畫面

import urllib.request as req
url = "https://www.ptt.cc/bbs/Gossiping/index.html"


#建立request物件，附加Request Header的資訊
#f12/network/index.html/Headers/user agent  Request Headers = 一般使用者使用連線時會發送的資訊，ppt才會認為我們是正常的使用者
request = req.Request(url, headers = {
    "cookie":"over18=1",  #模擬完成跳躍視窗的選取，進入主畫面
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

#抓取上一頁的連結
nextLink = root.find("a", string = "‹ 上頁")     #找到內文是‹ 上頁的 a 標籤
print(nextLink["href"])     #抓取標籤內的href屬性