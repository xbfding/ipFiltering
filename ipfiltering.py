# python3
import re
import os

def openip(ipPath):
    f = open(ipPath, "r", encoding='utf-8').read()
    return f

def ip_screen(ip):  # 从文本中筛选ip
    print("ip地址开始筛选")
    domain = r'(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
    domainlist = re.findall(domain, ip)
    domainList = []
    for i in domainlist:  # ip去重
        if not i in domainList:
            domainList.append(i)
    f = open("./out/ip_out.txt", 'w')    # 将结果写入url_out.txt文件中
    for i in domainList:
        open('./out/ip_out.txt', 'a', encoding='utf-8').write(i + "\n")
    f.close()
    print("ip地址筛选完成\n")
    ip_Nali()   #若不做查询，注释该行即可

def ip_Nali():
    print("ip地址开始查询")
    cmd = './ipNali.sh'
    os.system(cmd)
    print("ip地址查询完成")

if __name__ == '__main__':
    ipPath = 'auth.log'   #需要筛选的文件路径
    ip = openip(ipPath)
    ip_screen(ip)
