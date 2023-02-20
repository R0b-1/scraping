import requests
from bs4 import BeautifulSoup
import time

baseUrl = 'https://www.allocine.fr'
uri = '/film/'
html = ".html"
uri2 = "/film/fichefilm_gen_cfilm="


response = requests.get(baseUrl + uri)
print(response)


if response.ok: 
    webpoints = []

    for i in range(1,60000):
        webpoints.append(baseUrl + uri2 + str(i) + html)
    print(webpoints) 
    swoup = BeautifulSoup(response.text, 'html.parser')
    ul = swoup.find('ul', {'class': 'gd-col-middle'})
    lis = swoup.findAll('a', {'class': 'meta-title-link'})
    print(ul)
    print(lis['href'])
    for li in lis:
        a = li.find('a')
        try:
            print(baseUrl + a['href'])
            requests.get(baseUrl + a['href'])
        except:
            pass
        time.sleep(0.9) 







   # for li in lis: 
     #   a = li.find('a') 

      #  try:
        #    print(baseUrl + a['href'])
           # requests.get(baseUrl + a['href'])
        #except:
         #   pass