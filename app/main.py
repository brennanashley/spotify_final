from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app import db, ml, viz

description = """
Deploys a nearest neighbors model on the [Spotify](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=tracks.csv) dataset.

To use these interactive docs:
- Click on an endpoint below
- Click the **Try it out** button
- Edit the Request body with your song choice
- Click the **Execute** button
- Scroll down to see the server response code & details
"""

app = FastAPI(
    title='🎵Spotify Sleuths🎵',
    description=description,
    docs_url='/',
)

# app.include_router(db.router, tags=['Database'])
app.include_router(ml.router, tags=['Machine Learning'])
app.include_router(viz.router, tags=['Visualization'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
