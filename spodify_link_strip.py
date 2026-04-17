

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os


load_dotenv("spodify.env")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:3000",
    scope="playlist-read-private playlist-read-collaborative"
))

playlist_ID = "6LCoMDQ5ZtvZJI8lLk0eVY"
results = sp.playlist_tracks(playlist_ID)


with open("playlist_data.txt", "w", encoding="utf-8") as f:
    for item in results['items']:
        track = item.get('track') or item.get('item')
        if track:
            line = f"{track['name']} - {track['artists'][0]['name']} - {track['album']['name']}"
            f.write(line + "\n")

print("Saved to playlist_data.txt")