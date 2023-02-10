MAX PINCKNEY
02/09/2023

PURPOSE: 
	Python scripts and helper scripts to use the spotify API to scrape through all artists' id, name, genres, and popularity score.

KNOWN BUGS: 
	Does not reach every single artist on spotify. Reaches a maximum of 1000 artists per combination of genre and market.

DESCRIPTION:
		In this directory you will find several python scripts, most not needed for the main purpose described above. I have included
	certain scripts that I used along the way to familiarize myself with the spotify API as well as other tools I used such as SQLite and Pandas.
	These scripts are marked with an 'H_' before their name to indicate that they are helper functions and not pertaining to the main script: 
	ArtistScrape.py. They were included to show the steps I took to reach my final script.

		ArtistScrape.py - Required library installations: spotipy	
		To run this program, open a Python terminal and execute the script. The program will search the Spotify API for artists based on 
	a combination of genre and market. The algorithm starts by setting up an SQLite database and table if they do not exist. Then, it performs a
	nested for-loop, iterating through each combination of genre and market code (ISO 3166-1 alpha-2 codes). The program then queries Spotify for
 	all songs with that combination, up to a limit of 1000 each, using the Spotify "Search for Item" function.
		Every time the program is run, the list of genres is randomized to avoid repeating results. If a genre-market combination reaches the 
	limit, the program outputs that combination to another table in the same database, indicating where artist data may be missing. To maintain data
 	cleanliness, the program commits changes to the database and removes any duplicates every time the market changes (every ~1300 queries). 
		Exception statements have also been included in the code to ensure that any data gathered until that point can still be committed to 
	the database in the event of an early termination, such as from a keyboard interrupt or unexpected error, preventing any loss of data.

		constants.py - 
		I used this python program to store various consant values used in ArtistScrape.py. 
	These values include: 	Spotify client id
			   	Spotify client secret
				Database name 
				Table name for storing artist information 
				Excel file name for outputting data
				List of valid country codes used in Spotify searches
				List of ~1300 spotify genres 
		Note: Although the Spotify API provides a function to get a list of genres, the list was found to be incomplete, so a hard-coded list 
	of genres from an external source was used instead.

		dbDataVis - Required library installations: pandas, openpyxl
		This file contains several functions that the user can utilize if they are not familiar with SQLite such as outputting the data to excel,
	removing a table from the database, and removing tables from the database.
		To run any of these functions, uncomment the desired function and provide values for the arguments 'dbName,' 'tblName,' and 'fileName.'

