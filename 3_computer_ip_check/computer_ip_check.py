#컴퓨터 내외부 아이피 확인용
import socket
import requests
import re

inner_ad = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
inner_ad.connect(("www.google.co.kr",443))
print("In_ip:",inner_ad.getsockname()[0])

req=requests.get("http://ipconfig.kr")
#out_ad = re.search(r'IP Address:(.*)', req.text)
out_ad = re.search(r'IP Address:\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)
out_ad = out_ad.group(1)
print("Out IP:",out_ad)
