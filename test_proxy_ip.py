#coding=utf-8

import requests
import sys
import threading
from time import sleep
import csv


csvfile=open('valid_ip.csv','w')
writer=csv.writer(csvfile)

class test_thread(threading.Thread):
    def __init__(self,ip,port):
        threading.Thread.__init__(self)
        self.ip=ip
        self.port=port
        #self.protocol=protocol
    def run(self):
        s = requests.session()
        s.keep_alive = False
        requests.adapters.DEFAULT_RETRIES = 5
        proxies = {"http": "http://"+self.ip + ":" + str(self.port)}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            'Connection': 'close'
        }
        try:
            maskedIP = str(requests.get("http://icanhazip.com/", headers=headers, timeout=8, proxies=proxies).text).replace("\n","")
        except Exception as e:
            return
        if maskedIP == self.ip:
            writer.writerow([self.ip, self.port])
            print(self.ip+" "+self.port)

def test_proxy(filename):
    reader=csv.reader(open(filename))
    for row in reader:
        ip, port=row[0],row[1]
        while threading.activeCount() >30:
            sleep(2)
        test_thread(ip,port).start()

def main():
    filename=sys.argv[1]
    print("The result will be saved in valid_ip.csv")
    test_proxy(filename)

if __name__ == '__main__':
    main()