import requests

def get_location(ip):
    import os
    api_url = os.getenv('API_URL', 'https://freeipapi.com/api/json')
    url = f'{api_url}/{ip}'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return {
        "country": data['countryName'],
        "region": data['regionName'],
        "city": data['cityName']
        }