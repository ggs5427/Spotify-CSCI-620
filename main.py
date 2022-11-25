import mysql.connector
import json

from datetime import datetime
import models
import psycopg2
import os

DB_HOST = "localhost"
DB_NAME = "spotify"
DB_USER = "postgres"
DB_PASS = "gelilasahle"

DIR = 'data'

def load_data(cur, spotifyDataBase):
    dataFile = "mpd.slice.10000-10999.json"
    data = []

    try:
        for filename in os.listdir(DIR):
            f = os.path.join(DIR, filename)
            file = open(f)
            jsonData = file.read()
            playlistsDatasets = json.loads(jsonData)

            for data in playlistsDatasets['playlists']:
                playlist = models.Playlists(data['name'], "-", data['modified_at'], data['num_followers'],
                                            data['num_tracks'], data['collaborative'])

                save_to_db(cur, playlist, data['tracks'], spotifyDataBase)
                break
            file.close()
            print("Done loading data for : " + f)
    except Exception as err:
        print("Could not read file.")
        return


def save_to_db(cur, playlist, tracksJson, spotifyDB):
    try:
        # Insert to Playlists if the playlist name doesn't exist
        formatted_date = datetime.fromtimestamp(playlist.modifiedAt).strftime('%Y-%m-%d %H:%M:%S')
        collaborative = True if (playlist.collaborative=="true") else False
        cur.execute(
            "INSERT INTO playlists (playlist_name, modifiedAt, numFollowers, numTracks, collaborative) VALUES (%s,%s,%s,%s,%s) RETURNING id;",
            (playlist.name, formatted_date , int(playlist.numFollowers), int(playlist.numTracks),
             collaborative)
        )
        playlist_id = cur.fetchone()[0]
        spotifyDB.commit()

        for tracks in tracksJson:
            artist = models.Artists(tracks['artist_name'])
            album = models.Albums(tracks['album_name'])
            track = models.Tracks(tracks['track_name'], tracks['duration_ms'])

            # Insert Artist
            cur.execute(
                "SELECT artist_name FROM artists WHERE artist_name=(%s);",
                (artist.name,))
            name = cur.fetchone()[0]
            if name == "":
                cur.execute(
                    "INSERT INTO artists (artist_name) VALUES (%s) RETURNING id;",
                    (artist.name,))
                artistId = cur.fetchone()[0]
                spotifyDB.commit()
            else:
                cur.execute(
                "SELECT id FROM artists WHERE artist_name=(%s);",
                (artist.name,))
                artistId = cur.fetchone()[0]

            # Insert Album
            cur.execute(
                "SELECT Name FROM albums WHERE Name=(%s);",
                (album.name,))
            name = cur.fetchone()[0]
            if name == "":
                cur.execute(
                    "INSERT INTO albums (Name, artistId) VALUES (%s, %s) RETURNING id;", 
                    (album.name, artistId))
                albumId = cur.fetchone()[0]
                spotifyDB.commit()
            else:
                cur.execute(
                "SELECT id FROM albums WHERE Name=(%s);",
                (album.name,))
                albumId = cur.fetchone()[0]
            # Insert Track
            cur.execute(
                "SELECT track_name FROM tracks WHERE track_name=(%s);",
                (track.name,))
            name = cur.fetchone()[0]
            if name == "":
                cur.execute(
                    "INSERT INTO tracks (track_name, albumId, durationMs) VALUES (%s, %s, %s) RETURNING id;",
                    (track.name, albumId, track.durationMs)
                )
                trackId = cur.fetchone()[0]
                spotifyDB.commit()
            else:
                cur.execute(
                "SELECT id FROM tracks WHERE track_name=(%s);",
                (track.name,))
                trackId = cur.fetchone()[0]

            # Add to TrackPlaylist
            cur.execute("INSERT INTO trackPlaylists (trackId, playlistId) VALUES (%s, %s);", (trackId, playlist_id))
            spotifyDB.commit()
    except Exception as err:
        print(err)
    finally:
        spotifyDB.commit()

def create_tables(cur):
    # Queries for creating tables
    commands = (
        """
        DROP TABLE IF EXISTS trackPlaylists
        """,
        """
        DROP TABLE IF EXISTS artists
        """,
        """
        DROP TABLE IF EXISTS playlists
        """,
        """
        DROP TABLE IF EXISTS albums
        """,
        """
        DROP TABLE IF EXISTS tracks
        """,
        """
        CREATE TABLE playlists (
            id SERIAL PRIMARY KEY ,
            playlist_name TEXT NOT NULL,
            modifiedAt TIMESTAMP WITHOUT TIME ZONE,
            numFollowers INTEGER DEFAULT 0,
            numTracks INTEGER DEFAULT 0,
            collaborative BOOLEAN DEFAULT false
        )
        """,
        """
        CREATE TABLE tracks(
            id SERIAL PRIMARY KEY,
            track_name TEXT NOT NULL,
            albumId INTEGER,
            durationMs INTEGER
        )
        """,
        """
        CREATE TABLE albums(
            Name TEXT NOT NULL,
            id SERIAL PRIMARY KEY, 
            artistId INT
        )
        """,
        """
        CREATE TABLE artists(
            artist_name TEXT NOT NULL,
            id SERIAL PRIMARY KEY 
        ) 
        """,
        """
        CREATE TABLE trackPlaylists(
            trackId INTEGER,
            playlistId INTEGER,
            CONSTRAINT fk_tracks FOREIGN KEY (trackId) REFERENCES tracks(id),
            CONSTRAINT fk_playlists FOREIGN KEY (playlistId) REFERENCES playlists(id)
        )
        """
    )
    try:
        for query in commands:
            cur.execute(query)
    except (Exception, psycopg2.DatabaseError) as err:
        print(err)


def main():
    # Establishing a connection with the DB
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

        # Creating table
        #create_tables(cursorObj)

        # loads data from json files to respective tables
        load_data(cursorObj, spotifyDataBase)
        #cursorObj.execute("""SELECT COUNT(*) FROM trackPlaylists;""")
        #print(cursorObj.fetchone())
        # Commiting all changes made and disconnecting from the server
        cursorObj.close()
        spotifyDataBase.commit()
        spotifyDataBase.close()
        print("done :)")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if spotifyDataBase is not None:
            spotifyDataBase.close()


if __name__ == "__main__":
    main()
