import matplotlib
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np
import seaborn as sns
import base64
import io
import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib as mpl

import matplotlib.pyplot as plt


def song_choice(song_id):
    df = pd.read_csv("https://raw.githubusercontent.com/brennanashley/DS-Build-3-Spotify/main/spotify_data.csv")
    # columns to drop for fitting
    c = ["duration_ms", "index", "genre", "artist_name", "track_id", "track_name", "key", "mode"]
    # get song from user input
    song = df[df["track_id"] == song_id].iloc[0]
    df_selected = df.copy()
    if not pd.isnull(song["genre"]): # If genre, set subset to only genre
        df_selected = df[df["genre"] == song["genre"]]
    # nearest neighbors
    nn = NearestNeighbors(n_neighbors=11, algorithm="kd_tree")
    nn.fit(df_selected.drop(columns=c))
    song = song.drop(index=c)
    song = np.array(song).reshape(1, -1)
    new = df_selected.iloc[nn.kneighbors(song)[1][0][1:11]]
    new2 = new[['artist_name', 'track_id', 'track_name']].copy()
    return new2.to_json(orient="records")

#csv2 = csv1[['Acceleration', 'Pressure']].copy()
#['artist_name', 'track_id', 'track_name']

#     result = df_selected.iloc[nn.kneighbors(song)[1][0][1:11]].to_json(orient="records")# Return results as json
#     parsed = json.loads(result)
#     return json.dumps(parsed, indent=2)
# .to_json(orient="index")

#print(song_choice('7FFfYM4JE1vj5n4rhHxg8q'))

# try to save png


def doublecheck(song_id):
    df = pd.read_csv("https://raw.githubusercontent.com/brennanashley/DS-Build-3-Spotify/main/spotify_data.csv")
    # columns to drop for fitting
    c = ["duration_ms", "index", "genre", "artist_name", "track_id", "track_name", "key", "mode"]
    # get song from user input
    song = df[df["track_id"] == song_id].iloc[0]
    df_selected = df.copy()
    if not pd.isnull(song["genre"]):  # If genre, set subset to only genre
        df_selected = df[df["genre"] == song["genre"]]
    # nearest neighbors
    nn = NearestNeighbors(n_neighbors=11, algorithm="kd_tree")
    nn.fit(df_selected.drop(columns=c))
    song = song.drop(index=c)
    song = np.array(song).reshape(1, -1)
    new = df_selected.iloc[nn.kneighbors(song)[1][0][1:11]]
    new2 = new[
        ['energy', 'danceability', 'key', 'popularity', 'acousticness', 'instrumentalness', 'liveness', 'loudness',
         'mode', 'tempo', 'speechiness', 'valence']].copy()

    fig = plt.figure()
    fig, ax = plt.subplots(1, 1, figsize=(10, 30))
    heatplot = ax.imshow(new2, cmap='YlGn')
    ax.set_xticklabels(new.track_name)
    ax.set_yticklabels(new2.columns)
    plt.xticks(rotation=45)
    tick_spacing = 1
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.set_title("Spotify Recommendation Comparisons")
    ax.set_xlabel('Track Name')
    ax.set_ylabel('Attributes')
    pic_bytes = io.BytesIO()
    plt.savefig(pic_bytes, format="png")
    pic_bytes.seek(0)
    data = base64.b64encode(pic_bytes.read()).decode("ascii")
    return heatplot
    #  plt.clf()
   # return "<img src='data:image/png;base64,{}'>".format(data).to_json()



#  return fig # .to_json()
# ['index', 'artist_name', 'track_id', 'track_name', 'acousticness',
#        'danceability', 'duration_ms', 'energy', 'instrumentalness', 'key',
#        'liveness', 'loudness', 'mode', 'speechiness', 'tempo',
#        'time_signature', 'valence', 'popularity', 'genre'],
#       dtype='object')
print(doublecheck('7FFfYM4JE1vj5n4rhHxg8q'))