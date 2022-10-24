import mysql.connector
import json

from datetime import datetime 
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
    formatted_date = datetime.fromtimestamp(playlist.modifiedAt).strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_date)
    cur.execute("SELECT 'Name' FROM playlists")
    print(cur.fetchall())
    cur.execute(
        "INSERT INTO Playlists ('Name', Description, modifiedAt, numFollowers, numTracks, collaborative) VALUES ('%s','%s','%s','%s','%s','%s')",
        (playlist.name, playlist.description, formatted_date, int(playlist.numFollowers), int(playlist.numTracks), eval(playlist.collaborative))
    )
    spotifyDataBase.commit()

    # # Select playlistId
    # val = ('Test')
    # sql = ("SELECT id FROM Playlists WHERE Name=(%s)")
    # cur.execute(sql, val)
    # playlistId = cur.fetchall()[0]
    # # print(playlistId)

    # for tracks in tracksJson:
    #     # print(tracks['artist_name'])
    #     artist = models.Artists(tracks['artist_name'])
    #     album = models.Albums(tracks['album_name'])
    #     track = models.Tracks(tracks['track_name'], tracks['duration_ms'])

    #     # Insert Artist
    #     print(artist.name)

    #     cur.execute("SELECT * FROM Playlists")
    #     print(cur.fetchall())

    #     cur.execute(
    #         "INSERT INTO Artists (Name) VALUES (%s)", 
    #         (artist.name))
    #     spotifyDataBase.commit()
    #     break
        # cur.execute("SELECT id FROM Artists WHERE Name=(%S)", (artist.name))
        # artistId = cur.fetchall()[0]

        # # Insert Albums
        # cur.execute(
        #     "INSERT INTO Albums (Name, artistId) VALUES (%s)", 
        #     (album.name, artistId))

        # cur.execute("SELECT id FROM Albums WHERE Name=(%s)", (album.name))
        # albumId = cur.fetchall()[0]

        # # Insert Tracks
        # cur.execute(
        #     "INSERT INTO Tracks (Name, albumId, durationMs) VALUES (%s, %s, %s)",
        #     (track.name, albumId, track.durationMs)
        # )

        # cur.execute("SELECT id FROM Tracks WHERE Name=(%s)", (track.name))
        # trackId = cur.fetchall()[0]

        # # Add to TrackPlaylist
        # cur.execute("INSERT INTO TrackPlaylist (trackId, playlistId) VALUES (%s, %s)", (playlistId, trackId))

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
    if spotifyDataBase.is_connected == False:
        print("Connection not working")
        return
    
    # preparing a cursor object
    cursorObj = spotifyDataBase.cursor(prepared=True)
    
    load_data(cursorObj, spotifyDataBase)

    cursorObj.close()
    # Disconnecting from the server
    spotifyDataBase.close()

if __name__ == "__main__":
    main()