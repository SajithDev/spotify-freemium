import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from pynput.keyboard import Key, Controller


scope = "user-read-currently-playing"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope)) #auto authenticates profile when token expires

keyboard = Controller()


def restart_app():
    os.system("taskkill /f /im Spotify.exe") #Force terminates the processes
    os.system("Spotify.exe --minimized") #Opens in minimized so current process is not interrupted (focus unchanged) 

def play_song():
    keyboard.press(Key.media_play_pause)
    keyboard.release(Key.media_play_pause)
    

while(1):

    results = sp.current_user_playing_track()

    try:
        if results['currently_playing_type'] == 'track':
            restart_app()
            time.sleep(1.25) # gives time for app to fully open

            play_song()

    except TypeError: # when app is closed
        pass

    time.sleep(1) #checks every second so does not waste CPU resources
