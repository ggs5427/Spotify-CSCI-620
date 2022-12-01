from datetime import datetime
import models
import psycopg2
import os

DB_HOST = "localhost"
DB_NAME = "spotify"
DB_USER = "postgres"
DB_PASS = "eshaandeshpande"

query_for_track_label = """
SELECT trackType.label, trackType.track_name
FROM trackType
INNER JOIN tracks
ON tracks.track_name = trackType.track_name
INNER JOIN trackPlaylists
ON tracks.id = trackPlaylists.trackId
AND trackPlaylists.playlistid = {0}
        """
        
query_for_recommendation = """ 
SELECT trackType.track_name
FROM trackType
WHERE trackType.label = (%s)
"""

query_playlist = """
SELECT *
FROM playlists
"""


def most_frequent(List):
    return max(set(List), key = List.count)
 

spotifyDataBase = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port = 5432
)
cursorObj = spotifyDataBase.cursor()
cursorObj.execute(query_playlist)
all_playlists = cursorObj.fetchall()
print("Playlist id      |       Playlist Name")
for row in all_playlists:
    print(str(row[0]) + "   |   " + str(row[1]))
p_id = input("Enter the id of the playlist you would like recommendations for: ")
cursorObj.execute(query_for_track_label.format(p_id))
result = cursorObj.fetchall()

final_result_list = list(map(list, zip(*result)))
label, name = final_result_list;
playlist_label = most_frequent(label)
cursorObj.execute(query_for_recommendation, str(playlist_label))
number = 0
final_predictions = []
while number < 3:
    temp = cursorObj.fetchone()
    if temp[0] not in name:
        number = number + 1
        final_predictions.append(temp[0])
print("The song recommendations for your playlist are:-")
for f in final_predictions:
    print(f)

