#coding=utf-8

import requests
from bs4 import BeautifulSoup
from time import sleep
import csv

def xici_ip_spider(start,end):
    url='http://www.xicidaili.com/nn/'
    csvfile=open('xici.csv','w')
    writer=csv.writer(csvfile)
    print("The result will be saved in xici.csv")
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    for num in range(start,end+1):
        sleep(2)
        print('Now downloaing the page' + str(num) + ' ips')
        request=requests.get(url+str(num),headers=headers)
        content=request.text

        soup = BeautifulSoup(content, 'html.parser')
        trs=soup.find_all('tr')
        for item in trs:
            try:
                temp=[]
                tds=item.find_all('td')
                temp.append(tds[1].text)
                temp.append(tds[2].text)
                temp.append(tds[5].text)
                writer.writerow(temp)
            except IndexError:
                pass

def kuaidaili_ip_spider(start,end):
    url='https://www.kuaidaili.com/free/inha/'
    csvfile=open('kuaidaili.csv','w',newline="")
    print("The result will be saved in kuaidaili.csv")
    writer=csv.writer(csvfile)
    s = requests.session()
    s.keep_alive = False
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
             'Connection': 'close'
             }
    for num in range(start,end+1):
        sleep(2)
        print('Now downloa ing the page' + str(num) + ' ips')
        try:
            request=requests.get(url+str(num),headers=headers,timeout=12)
        except Exception as e:
            print(e)
            pass
        content=request.text
        soup=BeautifulSoup(content,'html.parser')
        trs=soup.find_all('tr')
        for item in trs:
            try:
                temp=[]
                tds=item.find_all('td')
                temp.append(tds[0].text)
                temp.append(tds[1].text)
                temp.append(tds[3].text)
                writer.writerow(temp)
            except IndexError:
                pass

def liuliuip_ip_spider(start,end):
    url='http://www.66ip.cn/'
    csvfile=open('66ip.csv','w')
    print("The result will be saved in 66ip.csv")
    writer=csv.writer(csvfile)
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    for num in range(start,end+1):
        sleep(2)
        print('Now downloaing the page' + str(num) + ' ips')
        try:
            request=requests.get(url+str(num)+'.html',headers=headers,timeout=12)
        except Exception as e:
            pass
        content=request.text
        soup=BeautifulSoup(content,'html.parser')
        trs=list(soup.find_all('tr'))
        for item in trs[2:]:
            try:
                temp=[]
                tds=item.find_all('td')
                temp.append(tds[0].text)
                temp.append(tds[1].text)
                writer.writerow(temp)
            except IndexError:
                pass


def main():
    print("Please select the website you want to crawl:")
    print("[1]www.xicidaili.com")
    print("[2]www.kuaidaili.com")
    print("[3]www.66ip.cn")
    answer=input()
    if answer=="1":
        xici_ip_spider(1,100) #可手动更改页数
    elif answer=="2":
        kuaidaili_ip_spider(1,100)
    elif answer=="3":
        liuliuip_ip_spider(1,100)
    else:
        exit()

if __name__ == '__main__':
    main()
