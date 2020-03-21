import requests
from lxml import etree

Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}

url = "https://www.xicidaili.com/nn"

html = requests.get(url=url,headers=Headers)
xmlContent = etree.HTML(html.content)

# 爬虫获取代理ip
def get_ip_agent():
    with open("ip_agent.txt","w") as f:
        for i in range(2,102):
            path_0 = "//*[@id='ip_list']/tr[" + str(i) + "]/td[2]/text()"
            path_1 = "//*[@id='ip_list']/tr[" + str(i) + "]/td[3]/text()"
            result_0 = xmlContent.xpath(path_0)
            result_1 = xmlContent.xpath(path_1)
            ip = str(result_0[0])
            port = str(result_1[0])
            # print(type(port))
            # 合并字符串
            ip_agent = ip+":"+port+"\n"
            # 存入txt文件中
            f.write(ip_agent)

get_ip_agent()