from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import re
import requests
from bs4 import BeautifulSoup as Soup

ua = UserAgent()
# From here we generate a random user agent
proxies = [] # Will contain proxies [ip, port]
emails=[]
# Main function
def main():
  # Retrieve latest proxies
  proxies_req = Request('https://www.sslproxies.org/')
  proxies_req.add_header('User-Agent', ua.random)
  proxies_doc = urlopen(proxies_req).read().decode('utf8')

  soup = BeautifulSoup(proxies_doc, 'html.parser')
  proxies_table = soup.find(id='proxylisttable')

  # Save proxies in the array
  for row in proxies_table.tbody.find_all('tr'):
    proxies.append(row.find_all('td')[0].string)
  print(len(proxies))
  for i in proxies:
      proxyDict = {
          "http": i,
          "https": i,
          "ftp": i
      }
      c = 'http://www.google.com/search?q=~+"actor"+"bollywood" AND "%40gmail.com" -intitle:"profiles" -inurl:"dir/+"+site:www.linkedin.com/in/+OR+site:www.linkedin.com/pub/'
      s = requests.get(c, proxies=proxyDict)
      f = Soup(s.text, 'html.parser')
      # print(f.text)

      emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", f.text)
      m = set(emails)
      # for i in m:
      # print(i)
      print(m)



















#de#f random_proxy():
  #return random.randint(0, len(proxies) - 1)

if __name__ == '__main__':
  main()
