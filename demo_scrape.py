
from urllib.request import urlopen,Request
import requests
import re
from bs4 import BeautifulSoup as Soup
c = 'http://www.google.com/search?q=~+"actor"+"bollywood" AND "%40gmail.com" -intitle:"profiles" -inurl:"dir/+"+site:www.linkedin.com/in/+OR+site:www.linkedin.com/pub/'
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://92.247.172.149:46176",
}
print(c)
s=requests.get(c,proxies=proxies)
print(s)
f = Soup(s, 'html.parser')
# print(f.text)

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", f.text)
m = set(emails)
# if(m==0):
# break
# for i in m:
# print(i)
print(len(m))
