CREATE DATABASE spotify;

CREATE TABLE Playlists(
	id INT PRIMARY KEY,
    Name TEXT NOT NULL,
    Description TEXT,
    modifiedAt datetime DEFAULT current_timestamp ON update current_timestamp,
    numFollowers INT DEFAULT 0,
    numEdits INT DEFAULT 0,
    collaborative bool default false
);

CREATE TABLE Tracks(
	id varchar(255) PRIMARY KEY,
    Name TEXT NOT NULL,
    albumId TEXT,
    durationMs INT
) ;

CREATE TABLE Albums(
    Name TEXT NOT NULL,
    id varchar(255) PRIMARY KEY, 
    artistId INT
); 

CREATE TABLE Artists(
    Name TEXT NOT NULL,
    id varchar(320) PRIMARY KEY 
) ;

CREATE TABLE TrackPlaylist(
	trackId varchar(255),
	playlistId INT,
	foreign key(trackId) references Tracks(id),
    foreign key(playlistId) references Playlists(id)
);