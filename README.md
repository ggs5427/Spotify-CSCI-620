# Spotify-CSCI-620
Song recommendation system for Spotify. We use users' playlist tracks list to tailor song recommendations that will fit their playlist. This recommendation system will be mainly focusing on suggesting new songs, providing an estimate on the possible popularity of a playlist, giving users the option to generate a playlist based on a popular song and giving users the option to create a playlist of frequently added songs.

### What we have done so far
For the first phase of the code implementation, we planned on working towards loading the database with records from the online Spotify dataset. While we were downloading the dataset, we ran into the issue of our machines not having enough space to unzip the data for parsing the json file. Eventually, we decided to focus on one json file at a time since our machines could work with it. Before we could start to load data to the database, we needed to create a database server.. Using Postgres, we created a database connection server to host our Spotify playlist data.

After setting up the necessary tables, we started working on the code that parses the json file and loads the data to our database. The json file included metadata about the playlist and tracks. A sample data of playlists can be found in `sampleData.json` file. The following is a snippet of the json file

```
{
        "name": "musical",
        "collaborative": "false",
        "pid": 5,
        "modified_at": 1493424000,
        "num_albums": 7,
        "num_tracks": 12,
        "num_followers": 1,
        "num_edits": 2,
        "duration_ms": 2657366,
        "num_artists": 6,
        "tracks": [
            {
                "pos": 0,
                "artist_name": "Degiheugi",
                "track_uri": "spotify:track:7vqa3sDmtEaVJ2gcvxtRID",
                "artist_uri": "spotify:artist:3V2paBXEoZIAhfZRJmo2jL",
                "track_name": "Finalement",
                "album_uri": "spotify:album:2KrRMJ9z7Xjoz1Az4O6UML",
                "duration_ms": 166264,
                "album_name": "Dancing Chords and Fireflies"
            },
```
From the json file, we took all the necessary information for filling up the database. The code that handles the parsing of the json file and loading of the data is in `main.py` file. We divided the playlist data found in the json to be represented as `Tracks`, `Artists`, `Albums`, `Playlists` and `TrackPlaylists` to help us keep track of all the songs and artists so that we can easily recommend songs based on users interest. `models.py` file has all the class definition for each entity. We also created an Entity Relationship Diagram to highlight the relationship between entities. `

![Spotify ERD drawio (1)](https://user-images.githubusercontent.com/47192431/197652946-26e37d0e-6fa9-4622-a953-52e5094116de.png)

Now the database holds around 1 million records.
