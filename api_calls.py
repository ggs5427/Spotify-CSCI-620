"""
Creates a database using api calls, which will be used for clustering songs
"""

import mysql.connector
import json

from datetime import datetime
import models
import psycopg2
import os
import pandas as pd

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='6fb8ba99218b4880977d28016fef0f0b', client_secret='6cca28d320ce4a05926e5d549e550399')
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

DB_HOST = "localhost"
DB_NAME = "spotify"
DB_USER = "postgres"
DB_PASS = "eshaandeshpande"

DIR = 'data'

def main():
    # Establishing a connection with the DB
    df = pd.DataFrame(columns = ['track_name', 'track_uri', 'duration', 'danceability', 'energy', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'])
    spotifyDataBase = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port = 5432
    )
    try:
        # preparing a cursor object
        cursorObj = spotifyDataBase.cursor()
        cursorObj.execute('''SELECT * from tracks''')
        result = cursorObj.fetchall();
        for row in result:
            res = sp.audio_features(row[2])[0]
            df = df.append({'track_name' : row[1], 'track_uri' : row[2], 'duration' : row[4], 'danceability' : res.get("danceability"), 'energy' : res.get("energy"), 'loudness' : res.get("loudness"), 'mode' : res.get("mode"), 'speechiness' : res.get("speechiness"), 'acousticness' : res.get("acousticness"), 'instrumentalness' : res.get("instrumentalness"), 'liveness' : res.get("liveness"), 'valence' : res.get("valence"), 'tempo' : res.get("tempo")},ignore_index = True)
            print(row)
        df.drop_duplicates()
        compression_opts = dict(method='zip', archive_name='out.csv')  
        df.to_csv('api_data.zip', index=False, compression=compression_opts)
        print(df.head())
    finally:
        if spotifyDataBase is not None:
            spotifyDataBase.close()


if __name__ == "__main__":
    main()