import requests
import re
from bs4 import BeautifulSoup as Soup
#limit=int(input("enter number of emails to scrape"))
occ=input("enter ocupation")
keyword=input("enter keyword")
c = 'http://www.google.com/search?q=~+' +keyword+ '+'+occ+ 'AND "%40gmail.com" -intitle:"profiles" -inurl:"dir/+"+site:www.linkedin.com/in/+OR+site:www.linkedin.com/pub/&num=100'
print (c)
s=requests.get(c)
f=Soup(s.text,'html.parser')
#print(f.text)

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", f.text)
m=set(emails)
#for i in m:
    #print(i)
print(len(m))


