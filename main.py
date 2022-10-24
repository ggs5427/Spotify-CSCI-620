import mysql.connector
import json

from numpy import place
import models

DB_HOST = "127.0.0.1"
DB_NAME = "spotify"
DB_USER = "root"
DB_PASS = "Fizzladygel1@"

def load_data(cur, spotifyDataBase):
    dataFile = "D:\Spotify-CSCI-620\data\mpd.slice.0-999.json"
    data = []
    
    try:
        file = open(dataFile)
        jsonData = file.read()
        playlistsDatasets = json.loads(jsonData)

        for data in playlistsDatasets['playlists']:
            playlist = models.Playlists(data['name'], "", data['modified_at'], data['num_followers'], data['num_tracks'], data['collaborative'])
            
            save_to_db(cur, playlist, data['tracks'], spotifyDataBase)
            break
        file.close()
    except Exception as err:
        print("Could not read file.")
        return


def save_to_db(cur, playlist, tracksJson, spotifyDataBase):
    # Insert to Playlists if the playlist name doesn't exist
    cur.execute(
        "INSERT INTO PLAYLIST (NAME, DESCRIPTION, MODIFIEDAT, NUMFOLLOWERS, NUMTRACKS, COLLABORATIVE) VALUES (%s, %s, %s, %s, %s, %s)",            (playlist.name, playlist.description, playlist.modifiedAt, playlist.numFollowers, playlist.numTracks, playlist.collaborative)
    )

    # Select playlistId
    cur.execute("SELECT ID FROM PLAYLIATS WHERE NAME=(%s)", (playlist.name))
    playlistId = cur.fetchall()[0]

    for tracks in tracksJson:
        artist = models.Artists(tracks['artist_name'])
        album = models.Albums(tracks['album_name'])
        track = models.Tracks(tracks['track_name'], tracks['duration_ms'])

        # Insert Artist
        cur.execute(
            "INSERT INTO ARTISTS (NAME)\
            VALUES (%s)", 
            (artist.name))

        cur.execute("SELECT ID FROM ARTISTS WHERE NAME=(%S)", (artist.name))
        artistId = cur.fetchall()[0]

        # Insert Albums
        cur.execute(
            "INSERT INTO ALBUMS (NAME, ARTISTID) VALUES (%s)", 
            (album.name, artistId))

        cur.execute("SELECT ID FROM ALBUMS WHERE NAME=(%s)", (album.name))
        albumId = cur.fetchall()[0]

        # Insert Tracks
        cur.execute(
            "INSERT INTO TRACKS (NAME, ALBUMID, DURATIONMS) VALUES (%s, %s, %s)",
            (track.name, albumId, track.durationMs)
        )

        cur.execute("SELECT ID FROM TRACKS WHERE NAME=(%s)", (track.name))
        trackId = cur.fetchall()[0]

        # Add to TrackPlaylist

def fetch_data():
    # gets data from the db
    pass
    

def main():
    spotifyDataBase = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USER,
    passwd = DB_PASS,
    database = DB_NAME
    )
    
    # preparing a cursor object
    cursorObj = spotifyDataBase.cursor()
    
    load_data(cursorObj, spotifyDataBase)

    # Disconnecting from the server
    spotifyDataBase.close()

if __name__ == "__main__":
    main()