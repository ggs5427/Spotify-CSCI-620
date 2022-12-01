# y axis - amount of followers
# x axis:
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
fpFol = list(dfF.iloc[:, 0])
tpTra = list(dfT.iloc[:, 1])
fpTra = list(dfF.iloc[:, 1])

# Plot the lines
# plt.bar(["True", "False"], [(sum(tpFol)/len(tpFol)),
#                            (sum(fpFol)/len(fpFol))], color=["green", "red"])


fdf = pd.DataFrame({"Followers": ((sum(tpFol)/len(tpFol)), (sum(fpFol)/len(fpFol))), "Tracks": (
    ((sum(tpTra)/len(tpTra))/8), ((sum(fpTra)/len(fpTra))/8))}, index=["True", "False"])

bar = fdf.plot.bar(rot=0, title="Popularity Anaylsis Based On Collaborativity")
bar.set_xlabel("Collaborative")
bar.set_ylabel("Average (x8 for tracks)")

plt.show(block=True)
