﻿# spotify-freemium
 
1) Go to https://developer.spotify.com/dashboard and log in
2) Select Create App and fill in some details, make sure the redirect URL is https://www.google.com/
3) Select Web API
4) Now that you have your credentials, go and add them to your env file as :
    $env:SPOTIPY_CLIENT_ID='your-spotify-client-id'
    $env:SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
    $env:SPOTIPY_REDIRECT_URI='your-app-redirect-url'
5) Now simply run the script and follow the steps
