import os
import re
import time

import pandas as pd
import requests
from pyquery import PyQuery as pq


def get_page(headers):
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,7.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    html=requests.get(url,headers=headers).text
    doc = pq(html)
    d = re.search('(\d+)',str(doc('.td'))).group(1)
    return d

path = r'C:\Users\MSI-PC\Desktop'
os.chdir(path)
headers = {
    'Referer': 'https://js.51jobcdn.com/in/css/2017/public/base.css?20180408',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
        }
d = get_page(headers)

job_name = []
company_name = []
working_space = []
salary = []
page = 1
while page < int(d)+1 :
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,'+str(page)+'.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    html = requests.get(url,headers=headers).text.encode('iso-8859-1').decode('gbk')
    df = pd.DataFrame(columns = ['职位名','公司名','工作地点','薪酬'])
    doc = pq(html)

    for item in doc('.dw_table .el')[1:]:
        item = pq(item)
        job_name.append(item('.t1').text())
        company_name.append(item('.t2').text())
        working_space.append(item('.t3').text())
        salary.append(item('.t4').text())
    page += 1
    if page%10 == 0:
        time.sleep(5)
        print("已经爬了"+str(page)+"页了")

print('爬完了，一共'+d+'页')
df['职位名'] = job_name
df['公司名'] = company_name
df['工作地点'] = working_space
df['薪酬'] = salary
df.to_excel('result.xlsx',index=False,encoding='utf-8')
