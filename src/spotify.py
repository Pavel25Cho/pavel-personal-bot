import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

sp = None

def setup():    
    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    #     client_id=os.environ.get('SPOTIFY_CLIENT_ID'),
    #     client_secret=os.environ.get('SPOTIFY_CLIENT_SECRET'),
    #     redirect_uri=os.environ.get('SPOTIFY_REDIRECT_URI'),
    #     scope="user-read-currently-playing"
    # ))
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    
    user = sp.user('Pave1Cho')
    print(user)
    
    current_playback = sp.current_playback('US')
    
    if current_playback and current_playback['is_playing']:
        track_name = current_playback['item']['name']
        artist_name = current_playback['item']['artists'][0]['name']
        new_bio = f"Слушаю: {track_name} - {artist_name} 🎶"
            
    print(f"Био обновлено: {new_bio}")