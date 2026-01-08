import requests
import json

# --- CONFIGURATION ---
ACCESS_TOKEN = 'EAATnlpsbgD8BQR4Dm5HUQvbZAZCHeocOWTKckHuF318RTp7HYuRG2kIJb4eOiLG7s4Lge7zCQ2AU26I4Sa0oGbNElmqgvt4yZAw0IGisw7wgnZB8NZBV24iu5y1NNZAs5xso0vgJPGlZANMepfHKn8rC3uoLH18e7ZAYoDOCh18NxCn85rXtZAjrMDPWtPMX9pA0jH9RV62mYzI3cTY7ZCERD37HlTqb1ERLEahbDQpbpad4U1IvcYWZBFZBMg74XHty5EAi0nqVzSXpDuV4uZBPwtsBz'
IG_USER_ID = '17841472790123391'

# YOUR PORTFOLIO: Map the brand name to its Hashtag ID
# (You already found Patek's ID: 17841563305082545)
WATCH_PORTFOLIO = {
    'Patek Philippe': '17841563305082545',
    'Rolex': '17841563259834671', 
    'Audemars Piguet': '17841562993070607',
    'Vacheron': '17841563063073357'
}

# Alerts only for high-value keywords
TRADE_SIGNALS = ['unworn', 'tiffany', 'new release', 'waitlist', 'discontinued']

def run_multi_brand_agent():
    print(f"--- 📊 WATCH MARKET INTELLIGENCE AGENT STARTING ---")
    
    for brand_name, hashtag_id in WATCH_PORTFOLIO.items():
        if hashtag_id == 'ADD_ID_HERE': continue # Skip unconfigured brands
        
        print(f"\nScanning {brand_name.upper()} Market...")
        
        url = f"https://graph.facebook.com/v21.0/{hashtag_id}/recent_media"
        params = {
            'user_id': IG_USER_ID,
            'fields': 'caption,like_count,permalink,timestamp',
            'access_token': ACCESS_TOKEN,
            'limit': 10
        }
        
        try:
            response = requests.get(url, params=params, verify=False).json()
            posts = response.get('data', [])
            
            for post in posts:
                caption = post.get('caption', '').lower()
                likes = post.get('like_count', 0)
                
                # Logic: Is this a potential trade signal?
                if any(signal in caption for signal in TRADE_SIGNALS):
                    print(f"🔥 [SIGNAL] {brand_name} - {likes} Likes")
                    print(f"   Link: {post['permalink']}")
                    
        except Exception as e:
            print(f"Error scanning {brand_name}: {e}")

if __name__ == "__main__":
    run_multi_brand_agent()