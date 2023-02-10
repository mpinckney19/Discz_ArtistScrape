#Program used to familiarize myself with the spotify search function and getting a searched artist's attributes
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from constants import genreList
cid = '48c0bd997a754a46a4871d8c4902823e'
secret = 'af92fc0377d447f98cd2692b7db02b5f'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

genreSearch = "pop"
artist_search = sp.search(q='genre:'+'"'+genreSearch+'"', type='artist', limit=50, offset=0,  market='US')

artist_names = []

print(artist_search['artists']['items']) #is an empty list when search doesn't find anything

if(artist_search['artists']['items']):
    print(artist_search['artists']['items'][0]['name']) #first artist searched's name

for artists in artist_search['artists']['items']:
    print(artists['genres'])
    artist_names.append(artists['name'])

print(artist_names)

