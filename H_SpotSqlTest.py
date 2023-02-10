#Program written to test writing sptofiy data so an SQLite database

import spotipy
import sqlite3
import pandas as pd
from constants import databaseName, tableName, xlFileName
from spotipy.oauth2 import SpotifyClientCredentials

cid = '48c0bd997a754a46a4871d8c4902823e'
secret = 'af92fc0377d447f98cd2692b7db02b5f'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


conn = sqlite3.connect(databaseName)
c = conn.cursor()

dropTable = f'''DROP TABLE {tableName}'''
createTable = f'''CREATE TABLE {tableName}(id, name, popularity, genres)'''
#c.execute(dropTable)
#c.execute(createTable)

artist_search = sp.search(q='genre:"pop"', type='artist', limit=50, offset=0,  market='US')

for artist in artist_search['artists']['items']:
    artistName = artist['name']
    artistID = artist['id']
    artistGenres = artist['genres']
    genreString = ", ".join(artistGenres)
    artistPop = artist['popularity']
    c.execute('''INSERT INTO ArtistInfo VALUES(?,?,?,?)''', (artistID, artistName, artistPop, genreString))

#conn.commit()

#c.execute('''SELECT * FROM ArtistInfo ORDER BY name ASC, id ASC''')

#c.execute('''SELECT * FROM ArtistInfo''')
#results = c.fetchall()

#print(results)

c.execute('''
DELETE FROM ArtistInfo
WHERE rowid NOT IN (
  SELECT MIN(rowid)
  FROM ArtistInfo
  GROUP BY id
)
''')

c.execute('''SELECT * FROM ArtistInfo ORDER BY name ASC, id ASC''')
results = c.fetchall()

dataFrame = pd.read_sql_query('SELECT * FROM ArtistInfo ORDER BY name ASC, id ASC', conn)

dataFrame.to_excel(xlFileName, index=False)

print(results)





