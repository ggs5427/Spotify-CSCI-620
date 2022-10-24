CREATE DATABASE spotify;

CREATE TABLE Playlists(
	id INT PRIMARY KEY,
    Name TEXT NOT NULL,
    Description TEXT,
    modifiedAt datetime DEFAULT current_timestamp ON update current_timestamp,
    numFollowers INT DEFAULT 0,
    numTracks INT DEFAULT 0,
    collaborative bool default false
);

CREATE TABLE Tracks(
	id INT PRIMARY KEY,
    Name TEXT NOT NULL,
    albumId TEXT,
    durationMs INT
) ;

CREATE TABLE Albums(
    Name TEXT NOT NULL,
    id INT PRIMARY KEY, 
    artistId varchar(320)
); 

CREATE TABLE Artists(
    Name TEXT NOT NULL,
    id INT PRIMARY KEY 
) ;

CREATE TABLE TrackPlaylist(
	trackId INT,
	playlistId INT,
	foreign key(trackId) references Tracks(id),
    foreign key(playlistId) references Playlists(id)
);