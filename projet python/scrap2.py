import requests
from bs4 import BeautifulSoup
import csv

baseurl = "https://www.autoscout24.fr"
def parse_voiture():
    ratios = []
    
    for page_number in range(1, 15):
        url = f"https://www.autoscout24.fr/lst/toyota/supra?sort=standard&desc=0&cy=D%2CA%2CB%2CE%2CF%2CI%2CL%2CNL&atype=C&ustate=N%2CU&powertype=kw&search_id=1t70ktgmmrj%3D104&page={page_number}"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        voitures = soup.find_all('div', class_='ListItem_wrapper__J_a_C')

        for voiture in voitures:
            nom_elem = voiture.find('a', class_='ListItem_title__znV2I Link_link__pjU1l')
            nom = nom_elem.text if nom_elem is not None else ''
            prix_elem = voiture.find('p', class_='Price_price__WZayw')
            prix = prix_elem.text if prix_elem is not None else ''
            km_elem = voiture.find('span', class_='VehicleDetailTable_item__koEV4')
            kilometrage = km_elem.text if km_elem is not None else ''
            lien_elem = voiture.find('a', class_='ListItem_title__znV2I Link_link__pjU1l')
            lien = lien_elem.get('href') if lien_elem is not None else ''

            ratio = {
                "nom": nom,
                "prix": prix,
                "kilometrage": kilometrage,
                "lien": baseurl+lien
            }
            ratios.append(ratio)
            print(ratio)

    with open('supra.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["nom", "prix", "kilometrage", "lien"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for ratio in ratios:
            writer.writerow(ratio)

    return ratios

print(parse_voiture())
