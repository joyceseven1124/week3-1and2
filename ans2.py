# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:02:07 2022

@author: 劉佳怡
"""

import urllib.request as req
import bs4 

good = []
bad =[]
usually =[]
def getData(url):
    request = req.Request(url,headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response :
        data = response.read().decode("utf-8")
        
    root = bs4.BeautifulSoup(data,"html.parser")
    titles = root.find_all("div", class_="title")
    
    
    for title in titles:
        if title.a != None :
            talk_title = title.a.string
            talk_title = talk_title.replace("Re: ","")
            if "[好雷]" in  talk_title:
                good.append(talk_title)
                good.append("\n")
                
            elif "[普雷]" in  talk_title:
                usually.append(talk_title)
                usually.append("\n")
                
            elif "[負雷]" in  talk_title:
                bad.append(talk_title)
                bad.append("\n")
             
    
    nextLink = root.find("a",string="‹ 上頁")
    return nextLink["href"]
 

count = 0 
pageURL = "https://www.ptt.cc/bbs/movie/index.html"
while count <= 10:
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    count += 1
    
with open("data.txt",mode="w",encoding="utf-8") as file:
        file.writelines(good)
        file.writelines(usually)
        file.writelines(bad)

