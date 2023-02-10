import spotipy
import sqlite3
import random
from spotipy.oauth2 import SpotifyClientCredentials
from constants import genreList, cid, secret, countryCodes, databaseName, tableName

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#spotify search function only retrieves this many entries per call to search (max 50)
SEARCHLIMIT = 50

#spotify limits to 1000 entries from one query 
# 950 is the offset limit assuming a search with a searchLimit of 50
OFFSETLIMIT = 950 


#Offset to start each search with (if you only wanted the last X artists in a search)
INITIALOFFSET = 0

#Setting up database connection
conn = sqlite3.connect(databaseName)
c = conn.cursor()
createArtistTableCommand = f'''CREATE TABLE {tableName}(id, name, popularity, genres)'''
insertCommand = f'''INSERT INTO {tableName} VALUES(?,?,?,?)'''
removeDupCommand = f'''
    DELETE FROM {tableName}
    WHERE rowid NOT IN (
        SELECT MIN(rowid)
        FROM {tableName}
        GROUP BY id
    )
    '''

#Create tables if no table has been created
try:
    c.execute(createArtistTableCommand)
    c.execute('''CREATE TABLE MissingData(genre, market)''')
except:
    pass

#Randomizing the order of the genre list so that sequential short runs of this script don't always yield duplicate artists
randomGenreList = genreList
random.shuffle(randomGenreList)

#Detecting Keyboard interrupts or errors so if the script is cut off early, it can still commit scraped data to database
try:
    for country in countryCodes:

        for genre in randomGenreList:
            offsetCount = SEARCHLIMIT

            artist_search = sp.search(q='genre:'+'"'+genre+'"', type='artist', limit=SEARCHLIMIT, offset=INITIALOFFSET,  market=country)

            if not artist_search['artists']['items']: 
                print("No artists found in genre: ", genre, "In market:", country)
                continue
    
            for artist in artist_search['artists']['items']:
                genreString = ", ".join(artist['genres'])
                c.execute(insertCommand, (artist['id'], artist['name'], artist['popularity'], genreString))
                

        #Keep searching the same query until reaching the offset limit or recieving an empty search
            while offsetCount <= OFFSETLIMIT:
                artist_search = sp.search(q='genre:'+'"'+genre+'"', type='artist', limit=SEARCHLIMIT, offset=offsetCount,  market=country)
        
                for artist in artist_search['artists']['items']:
                    genreString = ", ".join(artist['genres'])
                    c.execute(insertCommand, (artist['id'], artist['name'], artist['popularity'], genreString))
            

                if not artist_search['artists']['items']: 
                    print("Finished search at genre:",genre,"With offset:", offsetCount, "In market:", country)
                    break
        
                #increase offset by amount searched for
                offsetCount += SEARCHLIMIT

                #If query reaches offset limit, state which genre (and market) the data is insufficent for
                if offsetCount > OFFSETLIMIT:
                    print("Artists not reached from genre: ", genre, "In market:", country)
                    c.execute('''INSERT INTO MissingData VALUES(?,?)''',(genre, country))

        #commit db and remove dups every time market changes
        c.execute(removeDupCommand)
        conn.commit()

    print('Search completed successfully.')
    c.execute(removeDupCommand)
    conn.commit()
    print('Data successfully committed to db')

except KeyboardInterrupt:
    print('Keyboard interrupt detected')
    c.execute(removeDupCommand)
    conn.commit()
    print('Data successfully committed to db')

except Exception as e:
    print('An error occurred:', e)
    c.execute(removeDupCommand)
    conn.commit()
    print('Data successfully committed to db')

