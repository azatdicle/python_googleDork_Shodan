import shodan
from googlesearch import search

def google_search(query):
    try:
        search_results = search(query)
        return search_results
    except Exception as e:
        print(f"Hata: {e}")
        return []

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

if __name__ == "__main__":
    print("""
      /| ________________
O|===|* >________________>
      \|
Google Dorks and Shodan 
      @azatdicle                               
                                                                      
      """)

    use = input("1. Google Dork\n2. Shodan\n:")
    if use == "1":
        search_query = input("Dork:")
        search_results = google_search(search_query)

        print("Google Search Results:")
        for result in search_results:
            print(result)
            
    elif use == "2":
        api_key = input("YOUR_SHODAN_API_KEY: ")
        shodan_search(api_key)
