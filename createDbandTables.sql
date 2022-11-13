CREATE DATABASE spotify;

CREATE TABLE Playlists(
	id INT PRIMARY KEY AUTO_INCREMENT,
    Name TEXT NOT NULL,
    Description TEXT,
    modifiedAt datetime DEFAULT current_timestamp ON update current_timestamp,
    numFollowers INT DEFAULT 0,
    numTracks INT DEFAULT 0,
    collaborative bool default false
);

CREATE TABLE Tracks(
	id INT PRIMARY KEY AUTO_INCREMENT,
    Name TEXT NOT NULL,
    albumId INT,
    durationMs INT
) ;

CREATE TABLE Albums(
    Name INT NOT NULL,
    id INT PRIMARY KEY AUTO_INCREMENT, 
    artistId INT
); 

CREATE TABLE Artists(
    Name TEXT NOT NULL,
    id INT PRIMARY KEY AUTO_INCREMENT 
) ;

CREATE TABLE TrackPlaylist(
	trackId INT,
	playlistId INT,
	foreign key(trackId) references Tracks(id),
    foreign key(playlistId) references Playlists(id)
);