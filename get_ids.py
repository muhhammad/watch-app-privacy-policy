import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
IG_USER_ID = '17841472790123391'
BRANDS_TO_FIND = ['rolex', 'audemarspiguet', 'vacheronconstantin']

print("--- 🔍 DISCOVERING BRAND IDS ---")
for brand in BRANDS_TO_FIND:
    url = f"https://graph.facebook.com/v21.0/ig_hashtag_search"
    params = {'user_id': IG_USER_ID, 'q': brand, 'access_token': ACCESS_TOKEN}
    
    res = requests.get(url, params=params, verify=False).json()
    if 'data' in res:
        print(f"ID for #{brand}: {res['data'][0]['id']}")
    else:
        print(f"Error finding {brand}: {res.get('error', {}).get('message')}")