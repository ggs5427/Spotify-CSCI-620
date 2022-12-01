"""
popularity
 - numfollowers (assc playlists)

how many followers an artist has
 - x: artists 
 - y: followers
how many playlists an artist is on
 - x: artists 
 - y: playlists

 how many popular artist on popular playlists

"""

import pandas as pd
import math
from matplotlib import pyplot as plt

# Make a list of columns
columns = ["trackid", "playlistid", "numfollowers", "artist_name"]

# Read a CSV file
df = pd.read_csv("table_formated_data/albums.csv", usecols=columns)
df = df.head(2000)

# Setting up data
artist = list(df.iloc[:, 3])
numFollowers = list(df.iloc[:, 2])
playlistid = list(df.iloc[:, 1])
trackid = list(df.iloc[:, 0])

# Making dict
artFol = dict()
artPlay = dict()
for i in range(len(artist)):
    # dict of artists followers
    art = artist[i]
    if art in artFol:
        artFol[art].append(numFollowers[i])
    else:
        artFol[art] = [numFollowers[i]]
    # dict of artist playlists
    play = artist[i]
    if play in artPlay:
        artPlay[play].add(playlistid[i])
    else:
        artPlay[play] = {playlistid[i]}

# Calculating Artist Popularity (Followers)
fXY = dict()
for key in artFol:
    lst = artFol[key]
    fXY[key] = (math.ceil(sum(lst)/len(lst)))
fXY = dict(sorted(fXY.items(), key=lambda x: x[1], reverse=True))

# Calculating Artist Popularity (Playlists)
pXY = dict()
for key in artPlay:
    lst = artPlay[key]
    pXY[key] = len(lst)
# pXY = sorted(pXY.items(), key=lambda x: x[1], reverse=True)
y = []
for key in fXY:
    y.append(pXY[key])

# Plot the lines
fig = plt.figure()
ax = fig.add_subplot(111, label="followers")
ax2 = fig.add_subplot(111, label="playlists", frame_on=False)

ax.plot(list(range(200)), list(fXY.values())[:200],
        color="blue", label="followers")
ax.set_xlabel("Artist", color="blue")
ax.set_ylabel("Number of Average Followers", color="blue")
ax.tick_params(axis='x', colors="blue")
ax.tick_params(axis='y', colors="blue")

ax2.bar(list(range(200)), y[:200],
        color="green", label="playlists")
ax2.xaxis.tick_top()
ax2.yaxis.tick_right()
ax2.set_xlabel("Artist", color="green")
ax2.set_ylabel("Number of Playlists", color="green")
ax2.xaxis.set_label_position('top')
ax2.yaxis.set_label_position('right')
ax2.tick_params(axis='x', colors="green")
ax2.tick_params(axis='y', colors="green")

plt.xlabel("Artist")
plt.title("Popularity Anaylsis Based Per Artist")
plt.show()
