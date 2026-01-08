import requests
import json

# --- CONFIGURATION ---
ACCESS_TOKEN = 'EAATnlpsbgD8BQa5gpPfA9KH143mOgXFd2ZB4eyZA8L5SxCwXMZBsMU6kVaVe7SPwqjjm662pdDLAJrHXaCOPnHZCV6O7w5K36da0n2zZCmnl3F78D2Ygg9AYTQFqKjovMnGy8pPpZBNK4noxRAZBoeR2HwudIaXU6gg5JDWb3ar0ajcBuT0jQUttndSl7OwkXk3g1y2FPCPcLukVedLkAHnUDMJ3gHoZCeNbrsflXFZCiDglyBbj2yZAVPLMU1Y0qyoOrUN8UU3frnIJA5hsay5TLhaAZDZD'
INSTAGRAM_ACCOUNT_ID = '17841472790123391'
HASHTAG_NAME = 'rolex'  # No '#' symbol

def get_hashtag_id(hashtag):
    url = f"https://graph.facebook.com/v21.0/ig_hashtag_search"
    params = {
        'user_id': INSTAGRAM_ACCOUNT_ID,
        'q': hashtag,
        'access_token': ACCESS_TOKEN
    }
    response = requests.get(url, params=params, verify=False)
    data = response.json()
    
    # DIAGNOSTIC CHECK:
    if 'error' in data:
        print(f"--- META API ERROR ---")
        print(f"Message: {data['error'].get('message')}")
        print(f"Type: {data['error'].get('type')}")
        print(f"Code: {data['error'].get('code')}")
        return None
        
    return data['data'][0]['id']

def get_hashtag_data(hashtag_id):
    """Pulls recent media from a specific hashtag ID."""
    # We ask for caption (sentiment), like_count (demand), and permalink
    url = f"https://graph.facebook.com/v21.0/{hashtag_id}/recent_media"
    params = {
        'user_id': INSTAGRAM_ACCOUNT_ID,
        'fields': 'id,caption,media_type,comments_count,like_count,permalink,timestamp',
        'access_token': ACCESS_TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()

# --- EXECUTION ---
try:
    print(f"Searching for ID for #{HASHTAG_NAME}...")
    h_id = get_hashtag_id(HASHTAG_NAME)
    
    print(f"Found ID: {h_id}. Pulling recent market data...")
    market_data = get_hashtag_data(h_id)
    
    # Simple display of the first 5 results
    for post in market_data.get('data', [])[:5]:
        likes = post.get('like_count', 0)
        caption = post.get('caption', 'No caption')[:50] + "..."
        print(f"[{likes} Likes] | {caption} | {post['permalink']}")

except Exception as e:
    print(f"Error: {e}")