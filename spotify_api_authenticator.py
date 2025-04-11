import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import time

# Load your dataset
df = pd.read_csv("Most Streamed Spotify Songs 2024.csv", encoding='ISO-8859-1')

# Set up Spotify API credentials
client_id = '7281387ca35a47689c9b58a18b688bb8'
client_secret = 'b1cc192fa93b4166a8779179262915e8'

# Authenticate
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Function to get album cover URL
def get_album_cover(track, artist):
    try:
        query = f"track:{track} artist:{artist}"
        results = sp.search(q=query, type='track', limit=1)
        items = results['tracks']['items']
        if items:
            return items[0]['album']['images'][0]['url']  # largest image
    except Exception as e:
        print(f"Error for {track} by {artist}: {e}")
    return None

# Add a new column for album cover URLs
df['Album Cover URL'] = df.apply(lambda row: get_album_cover(row['Track'], row['Artist']), axis=1)

# Optional: Save the result to a new CSV
df.to_csv("spotify_with_covers.csv", index=False)
