"""Database functions"""

import os
import sqlite3
import pandas as pd

from dotenv import load_dotenv
from fastapi import APIRouter, Depends
import sqlalchemy

router = APIRouter()


async def get_db() -> sqlalchemy.engine.base.Connection:
    """Get a SQLAlchemy database connection.
    
    Uses this environment variable if it exists:  
    DATABASE_URL=dialect://user:password@host/dbname

    Otherwise uses a SQLite database for initial local development.
    """
    #load_dotenv()
    #database_url = os.getenv('DATABASE_URL', default='sqlite:///temporary.db')
    #engine = sqlalchemy.create_engine(database_url)
    engine = sqlalchemy.create_engine('sqlite:///spotify_songs_db.sqlite3')
    #sq_con = sqlite3.connect('spotify_songs_db.sqlite3')
    #sq_curs = sq_con.cursor()
    # load the data into a pandas dataframe and set the index
    song_data = pd.read_csv('data_o_clean.csv')
    song_data.to_sql('data_o_clean', con=engine, if_exists='replace')
    connection = engine.connect()
    try:
        yield connection
    finally:
        connection.close()


@router.get('/info')
async def get_url(connection=Depends(get_db)):
    """Verify we can connect to the database, 
    and return the database URL in this format:

    dialect://user:password@host/dbname
    
    The password will be hidden with ***
    """
    url_without_password = repr(connection.engine.url)
    return {'database_url': url_without_password}

