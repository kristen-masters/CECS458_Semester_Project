"""
Polished UI for product. 
Streamlit is used for User Interface.
"""

import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from google import genai
from google.genai import types
from dotenv import load_dotenv
import json
import sys
import os
import re

st.set_page_config(page_title="AI Song & Caption Generatror", page_icon="🎶", layout="centered")

def load_API():
    load_dotenv("spodify.env")

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        redirect_uri="http://127.0.0.1:3000",
        scope="playlist-read-private playlist-read-collaborative"
    ))
    return sp

def fetch_playlist_ID(url): 
    playlist_ID = url.split("/playlist/")[1].split("?")[0]
    return playlist_ID

def strip_playlist(sp,playlist_ID):
    playlist_songs = []
    results = sp.playlist_tracks(playlist_ID)
    for item in results['items']:
            track = item.get('track') or item.get('item')
            if track:
                song = f"{track['name']}"
                artist = f"{track['artists'][0]['name']}"
                album =f" {track['album']['name']}"

                track_info = [song, artist, album]
                playlist_songs.append(track_info)
    return(playlist_songs)

def generate_songs_recs(playlist, prompt):
    get_api_key = None

    try:
        if "GEMINI_API_KEY" in st.secrets:
            get_api_key = st.secrets["GEMINI_API_KEY"]
    except FileNotFoundError:
        pass
    except Exception:
        pass

    if get_api_key is None:
        load_dotenv("spodify.env")

        get_api_key = os.getenv("GEMINI_API_KEY")

def main():
    st.title("🎶 AI Song & Caption Generator")
    st.markdown("" \
    "**Spodify Playlist Upload:**" \
    "\n   - Needs the **FULL URL** to fetch a playlist." \
    "\n   - Playlist needs to be **public** and less than 100 tracks.")

    st.markdown("**Post Information:**\n\n - Give a short description of what your post is about.")

main()