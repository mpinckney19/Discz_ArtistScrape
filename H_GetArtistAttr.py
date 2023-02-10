#Program used to familiarize myself with the basics of the spotify API and finding an artist's attributes

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
cid = '48c0bd997a754a46a4871d8c4902823e'
secret = 'af92fc0377d447f98cd2692b7db02b5f'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

artist_name = []
artistID = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
artist = sp.artist(artistID)
print(type(artist))
print(artist['name'])
print(artist['id'])
print(artist['genres'])
print(artist['popularity'])

