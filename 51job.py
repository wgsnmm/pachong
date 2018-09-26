from bs4 import BeautifulSoup
import requests
import xlwt

file = xlwt.Workbook() #新建一个excel文件
table = file.add_sheet('51job信息') #增加一个子表
table_row = 0 #这是行数，从0行开始写入

page = 1
while page < 10:
    url = "http://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,"+str(page)+".html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    r = requests.get(url)
    text = r.text.encode('iso-8859-1').decode('gbk')
    bs = BeautifulSoup(text, "html.parser")
    jobs = bs.select("#resultList > .el")
    for i in jobs:
        job_name = i.select(".t1")[0].text.strip()
        table.write(table_row, 0, job_name) #将职位名存储

        company_name = i.select(".t2")[0].text.strip()
        table.write(table_row, 1, company_name) #将公司名存储

        working_space = i.select(".t3")[0].text.strip()
        table.write(table_row, 2, working_space) #将工作地点存储

        salary = i.select(".t4")[0].text.strip()
        table.write(table_row, 3, salary) #将薪酬存储

        table_row = table_row + 1 #每循环以此行数就要增加，新的数据就会存储到下一行

        print(job_name, company_name, working_space, salary)
    page = page + 1

file.save('职位信息.xlsx')