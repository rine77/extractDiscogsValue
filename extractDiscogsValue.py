import requests

# Deine API-Daten
user_token = 'YOUR_DISCOGS_API_TOKEN'
username = 'YOUR_DISCOGS_USERNAME'

# URL für die Sammlung
url = f'https://api.discogs.com/users/{username}/collection/value'

# Header mit Authentifizierung
headers = {
    'Authorization': f'Discogs token={user_token}'
}

# Anfrage an die API
response = requests.get(url, headers=headers)

# Überprüfen, ob die Anfrage erfolgreich war
if response.status_code == 200:
    data = response.json()
    estimated_value_low = data['minimum']
    estimated_value_median = data['median']
    estimated_value_high = data['maximum']
    
    print(f"Estimated Collection Value Low: {estimated_value_low}")
    print(f"Estimated Collection Value Median: {estimated_value_median}")
    print(f"Estimated Collection Value High: {estimated_value_high}")
else:
    print(f"Fehler: {response.status_code}")
