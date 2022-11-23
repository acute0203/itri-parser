# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
payload = {
"do_s_1": 1,
"vKey": "e5a55eb5-862d-4532-8061-9d6afeaa3fab",
"showMode": 1,
"city": "臺北市",
"change_city": 2,
"cityarea": "中正區",
"Street_kind": 1,
"street": "八德路一段",
"street2":"" ,
"lane": "",
"alley":"" ,
"num": 1,
"num_hyphen":"", 
"fl":"",
"hyphen":"", 
"suite":"", 
"list":True,
"checkImange": 7930,
"submit": "查詢"
}

#https://www.vscinemas.com.tw/ShowTimes//ShowTimes/GetShowTimes
response = requests.post("https://www.post.gov.tw/post/internet/Postal/index.jsp?ID=207", data = payload)
soup = BeautifulSoup(response.text, 'html.parser')
#address parse
raw_address = soup.find('td',{'bgcolor':"#FFFFFF"}).text.strip()
raw_address = re.sub(r'\s+', " ", raw_address)
all_codes = soup.find_all(text=re.compile('\d{6}$'))
#print(all_codes)
for code in all_codes:
    address_table = code.parent.parent.parent.parent
    #print(address_table)
    address_table_all_td = address_table.find_all('td')
    if address_table_all_td[-2].text.strip() == '全':
        address_code = address_table_all_td[0].text
        print(re.sub(r'郵遞區號', address_code, raw_address))
