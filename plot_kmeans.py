"""
This code uses KMeans to  cluster the data into 10 different datasets
This code required the file created by api_calls.py
"""

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
path = "\\table_formated_data\out.csv"

df = pd.read_csv(path)
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

x, y = plot_df

plt.scatter(x, y, c=y_kmeans, s=50, cmap='viridis')

centers = model.cluster_centers_
#plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
plt.show()