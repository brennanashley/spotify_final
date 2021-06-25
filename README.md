# Lambda Build Project

- [Spotify Sleuths](#spotify-sleuths)
  - [Usage](#usage)
    - [Suggestion of 10 songs based on one track_id given](#retrieve-10-songs-suggested-based-on-one-track_id-given)
    - [Heatmap comparison of suggestions one track_id given](#heatmap-comparison-of-suggestions-on-one-track_id-given)

## Spotify Sleuths

https://spotifysleuths.herokuapp.com/

A FastAPI Framework hosted on Heroku that suggests 10 songs based on user input of song_id.

---

## Usage

#### Retrieve 10 songs suggested based on one track_id given

Example:

Input:

    input track_id : '7FFfYM4JE1vj5n4rhHxg8q'
    Babe by Sugarland (featuring Taylor Swift)

Returns:

    "[{\"artist_name\":\"Jordan Davis\",\"track_id\":\"4CZ0nzD7AsWeSEElxKodqq\",\"track_name\":\"Leaving New Orleans\"},
    {\"artist_name\":\"Kelsea Ballerini\",\"track_id\":\"6DeMC9qUOznRorpgNW6dYe\",\"track_name\":\"Unapologetically\"},
    {\"artist_name\":\"Upchurch\",\"track_id\":\"1WcpvgQNOUHW7nPMFvCox6\",\"track_name\":\"Rattlin Chains\"},
    {\"artist_name\":\"Jordan Davis\",\"track_id\":\"2k4Chj6SG01uoySJzBK1lO\",\"track_name\":\"Made That Way\"},
    {\"artist_name\":\"Tenille Townes\",\"track_id\":\"7GW2dqJ13S3UutqzSuvzlR\",\"track_name\":\"Somebody's Daughter\"},
    {\"artist_name\":\"Upchurch\",\"track_id\":\"6YobhoXBNMa2RgiofR8g3S\",\"track_name\":\"Spotlight\"},
    {\"artist_name\":\"Jayne Denham\",\"track_id\":\"6yP7HwfEOE3lIex6XcOWR8\",\"track_name\":\"Hung up on You\"},
    {\"artist_name\":\"Dolly Parton\",\"track_id\":\"3jyVsxt4UNU4PEZR0klPAK\",\"track_name\":\"Holdin' On To You - from the Dumplin' Original Motion Picture Soundtrack\"},
    {\"artist_name\":\"RaeLynn\",\"track_id\":\"2zye2YstssP0sUw0uRk6N3\",\"track_name\":\"Tailgate\"},
    {\"artist_name\":\"George Strait\",\"track_id\":\"2bnza4qcST8dtKKOUKqvuS\",\"track_name\":\"Codigo\"}]"

---


#### Heatmap comparison of suggestions on one track_id given

Example:

Input:

    input track_id : '7FFfYM4JE1vj5n4rhHxg8q'
    Babe by Sugarland (featuring Taylor Swift)

Returns:

    ![img.png](img.png)
    

---
