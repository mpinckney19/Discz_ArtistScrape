#Helper function used to determine which ISO country codes were valid to use in a spotify search

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from constants import countryCodes
cid = '48c0bd997a754a46a4871d8c4902823e'
secret = 'af92fc0377d447f98cd2692b7db02b5f'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

notWorking = []

for countries in countryCodes:
    try:
        artist_search = sp.search(q='year:2023', type='artist', limit=50, offset=0,  market=countries)
    except:
        notWorking.append(countries)
        print(countries)
    finally:
        pass

print(notWorking)