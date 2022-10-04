# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:44:19 2022

@author: 劉佳怡
"""

import urllib.request as req
import json
import csv

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
request = req.Request(url, headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

data = json.loads(data)
attractions = data["result"]["results"]

file_name = "week3-1.csv"

for i in range(len(attractions)):
    attraction_date = attractions[i]["xpostDate"].split("/")
    attraction_date = int(attraction_date[0])
    
    if(attraction_date >= 2015):
        attraction_name = attractions[i]["stitle"]
        
        attraction_longitude = attractions[i]["longitude"]
        attraction_latitude = attractions[i]["latitude"]
        
        
        attraction_area = attractions[i]["address"].split()
        attraction_area = attraction_area[1][0:3]
        
        
        attraction_picture = attractions[i]["file"].split("https")
        del attraction_picture[0]
        attraction_picture = "https" +attraction_picture[0]
        
        clean_data = [attraction_name, attraction_area ,attraction_longitude , attraction_latitude  , attraction_picture]
        print(clean_data)

        file = open("ans1.csv","a",newline="")
        output_write = csv.writer(file)
        output_write.writerow(clean_data)
        file.close()
  

    