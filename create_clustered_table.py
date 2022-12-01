import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import mysql.connector
import json

from datetime import datetime
import models
import psycopg2
import os

DB_HOST = "localhost"
DB_NAME = "spotify"
DB_USER = "postgres"
DB_PASS = "eshaandeshpande"

insert_command = """INSERT INTO trackType (track_name, label) VALUES (%s, %s);"""

df = pd.read_csv("D:\BD Project\Spotify-CSCI-620-main\Spotify-CSCI-620-main\out\out.csv")
print("\n  There are",len(df),"songs in the dataset\n")

pca = PCA(2)
 
#Transform the data

features = ['duration', 'danceability', 'energy', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
pca_df = pca.fit_transform(df[features])
scaler = preprocessing.StandardScaler(with_mean=True, with_std=True)
# Fit your data on the scaler object
dfz = scaler.fit_transform(df[features])
dfz = pd.DataFrame(dfz, columns=features)
dfz['track_name']=df['track_name']
model = KMeans(n_clusters=10)
model.fit(dfz[features])
#print(model.labels_)
y_kmeans = model.predict(dfz[features])
dfz['label'] = model.labels_
#print(dfz.head())
plot_df = list(map(list, zip(*pca_df)))

final_df = pd.DataFrame()
final_df['track_name'] = df['track_name']
final_df['label'] = dfz['label']

print(final_df.head())

print("Insterting data into trackType")

spotifyDataBase = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port = 5432
)
cursorObj = spotifyDataBase.cursor()
for index, row in final_df.iterrows():
    cursorObj.execute(insert_command,(row["track_name"], row["label"]))
cursorObj.close()
spotifyDataBase.commit()
spotifyDataBase.close()
print("done :)")
