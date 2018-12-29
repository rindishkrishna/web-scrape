import requests
import re
from bs4 import BeautifulSoup as Soup
from fake_useragent import UserAgent
emails=[]

#limit=int(input("enter number of emails to scrape"))
occ=input("enter ocupation")
ua = UserAgent()
proxies = {
  "http": "10.10.1.10:3128",
  "https": "10.10.1.10:1080",
}



headers = {'User-Agent': ua.random}

keyword=input("enter keyword")
l=['www.instagram.com',]
for i in range(0,500,100):
    c = 'http://www.google.com/search?q=~+'+'"'+keyword+'"'+'+'+'"'+occ+'"'+'AND "%40gmail.com" -intitle:"profiles" -inurl:"dir/+"+site:www.linkedin.com/in/+OR+site:www.linkedin.com/pub/&num=100&start='+str(i)
    print(c)
    s = requests.get(c,headers=headers,proxies=proxies)
    f = Soup(s.text, 'html.parser')
    # print(f.text)

    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", f.text)
    m = set(emails)
    #if(m==0):
        #break
    # for i in m:
    # print(i)
    print(len(m))

