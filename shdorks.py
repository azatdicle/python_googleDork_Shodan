import shodan
import requests
import argparse
from functools import partial
from multiprocessing import Pool
from bs4 import BeautifulSoup as bsoup

def google_dork_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    return response.text

def extract_links(text):
    # Düzenli ifade ile linkleri ayıkla
    pattern = re.compile(r'href=["\'](https?://\S+)', re.IGNORECASE)
    links = pattern.findall(text)
    return links

def google_dorks():
    query = input("Google Dork: ")
    result = google_dork_search(query)
    links = extract_links(result)
    
    # Elde edilen linkleri yazdır
    print("Found Links:")
    for link in links:
        print(link)
        
        
def shodan_search(api_key):
    api = shodan.Shodan(api_key)
    query = input("Shodan Search: ")
    try:
        results = api.search(query)
        for result in results['matches']:
            # Sadece IP adresini al
            country = result.get('location', {}).get('country_name', 'N/A')
            ip = result.get('ip', 'N/A')
            print(f"Country {country} IP: {ip}")
    except shodan.APIError as e:
        print(f'Hata: {e}')

print("""
      /| ________________
O|===|* >________________>
      \|                        
Google Dorks and Shodan 
      @azatdicle                               
                                                                      
      """)

use = input("1. Google Dork\n2. Shodan\n:")
if use == "1":
    google_dorks()
elif use == "2":
    api_key = input("YOUR_SHODAN_API_KEY: ")
    shodan_search(api_key)
