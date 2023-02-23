import requests
from bs4 import BeautifulSoup


baseUrl = 'https://www.autoscout24.fr/'
uri = 'lst/toyota/supra?sort=standard&desc=0&cy=D%2CA%2CB%2CE%2CF%2CI%2CL%2CNL&atype=C&ustate=N%2CU&damaged_listing=exclude&powertype=kw&search_id=1t70ktgmmrj'
html = ".html"



response = requests.get(baseUrl + uri)
print(response)


if response.ok: 
    webpoints = []

    for i in range(1,250):
        webpoints.append(baseUrl + uri + str(i) + html)
    print(webpoints) 
    swoup = BeautifulSoup(response.text, 'html.parser')
    ul = swoup.find('div', {'class': 'ListItem_header__uPzec'})
    lis = swoup.findAll('a', {'class': 'a class="ListItem_title__znV2I Link_link__pju1l"'})
    print(ul)
    print(lis['href'])
    for li in lis:
        a = li.find('a')
        try:
            print(baseUrl + a['href'])
            requests.get(baseUrl + a['href'])
        except:
            pass
       







   # for li in lis: 
     #   a = li.find('a') 

      #  try:
        #    print(baseUrl + a['href'])
           # requests.get(baseUrl + a['href'])
        #except:
         #   pass