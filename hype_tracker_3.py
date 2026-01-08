import requests
import urllib3
import time
import csv
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- CONFIGURATION ---
ACCESS_TOKEN = 'EAATnlpsbgD8BQR4Dm5HUQvbZAZCHeocOWTKckHuF318RTp7HYuRG2kIJb4eOiLG7s4Lge7zCQ2AU26I4Sa0oGbNElmqgvt4yZAw0IGisw7wgnZB8NZBV24iu5y1NNZAs5xso0vgJPGlZANMepfHKn8rC3uoLH18e7ZAYoDOCh18NxCn85rXtZAjrMDPWtPMX9pA0jH9RV62mYzI3cTY7ZCERD37HlTqb1ERLEahbDQpbpad4U1IvcYWZBFZBMg74XHty5EAi0nqVzSXpDuV4uZBPwtsBz'
IG_USER_ID = '17841472790123391'

# YOUR VERIFIED PORTFOLIO
WATCH_PORTFOLIO = {
    'Patek Philippe': '17841563305082545',
    'Rolex': '17841562471110206',
    'Audemars Piguet': '17843671774049203'
}

def save_to_csv(data, csv_file):
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['timestamp', 'brand', 'likes', 'link', 'caption'])
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def watch_agent(media_type, csv_file):
    print(f"--- 📊 WATCH TRADING AGENT: ONLINE ---")
    
    for brand, h_id in WATCH_PORTFOLIO.items():
        print(f"Scanning {brand} for {media_type}...")
        url = f"https://graph.facebook.com/v21.0/{h_id}/{media_type}"
        params = {'user_id': IG_USER_ID, 'fields': 'caption,like_count,permalink,timestamp', 'access_token': ACCESS_TOKEN}
        
        try:
            res = requests.get(url, params=params, verify=False).json()
            for post in res.get('data', []):
                # Save data for every post found
                save_to_csv({
                    'timestamp': post.get('timestamp'),
                    'brand': brand,
                    'likes': post.get('like_count', 0),
                    'link': post.get('permalink'),
                    'caption': post.get('caption', '')[:100].replace('\n', ' ') # Clean snippet
                },
                csv_file)
            print(f"✅ Logged {len(res.get('data', []))} posts for {brand}")
            time.sleep(2) # Prevent rate limiting
            
        except Exception as e:
            print(f"Error on {brand}: {e}")


if __name__ == "__main__":
    watch_agent("recent_media", "recent_market_signals.csv")
    watch_agent("top_media", "top_market_signals.csv")