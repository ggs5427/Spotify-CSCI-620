# y axis - amount of followers
# x axis - amount of tracks
# Cluster 1 - collaboration = true
# Cluster 2 - collaboartion = false

import pandas as pd
import math
from matplotlib import pyplot as plt

# Make a list of columns
columns = ['numfollowers', 'numtracks']

# Read a CSV file
dfT = pd.read_csv("table_formated_data/playlists_true.csv", usecols=columns)
dfF = pd.read_csv("table_formated_data/playlists_false.csv", usecols=columns)

# Setting up data
tpFol = list(dfT.iloc[:, 0])
tpTra = list(dfT.iloc[:, 1])
fpFol = list(dfF.iloc[:, 0])
fpTra = list(dfF.iloc[:, 1])

# Calculate average


def avgerage(fol, tra):
    c = fol[0]
    x = [c]
    y = []
    t = []
    for i in range(len(fol)):
        if(fol[i] == c):
            t.append(tra[i])
        else:
            y.append(math.ceil(sum(t) / len(t)))
            c = fol[i]
            x.append(c)
            t = [tra[i]]
    y.append(math.ceil(sum(t) / len(t)))
    return x, y


tpX, tpY = avgerage(tpFol, tpTra)
fpX, fpY = avgerage(fpFol, fpTra)


# Plot the lines
fig = plt.figure()
ax = fig.add_subplot(111, label="false")
ax2 = fig.add_subplot(111, label="true", frame_on=False)

ax.scatter(fpX, fpY, color="red", label="false")
ax.set_xlabel("False: Number of Followers", color="red")
ax.set_ylabel("False: Number of Tracks", color="red")
ax.tick_params(axis='x', colors="red")
ax.tick_params(axis='y', colors="red")

ax2.scatter(tpX, tpY, color="green", label="true")
ax2.xaxis.tick_top()
ax2.yaxis.tick_right()
ax2.set_xlabel("True: Number of Followers", color="green")
ax2.set_ylabel("True: Number of Tracks", color="green")
ax2.xaxis.set_label_position('top')
ax2.yaxis.set_label_position('right')
ax2.tick_params(axis='x', colors="green")
ax2.tick_params(axis='y', colors="green")

plt.title("Popularity Anaylsis Based On Collaborativity")

plt.show()
