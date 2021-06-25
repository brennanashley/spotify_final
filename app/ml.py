""""Machine learning functions"""

import logging
from fastapi import APIRouter
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np


log = logging.getLogger(__name__)
router = APIRouter()


@router.post('/predict')
async def song_choice(song_id):
    """
    Let us help you find new songs using our nearest neighbors model!
    """
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
    new2 = new[['artist_name', 'track_id', 'track_name']].copy()
    return new2.to_json(orient="records")


