import pandas as pd
from youtubesearchpython import VideosSearch

df = pd.read_csv("My Spotify Library.csv")

results = []

for _, row in df.iterrows():
    query = f"{row['Track name']} {row['Artist name']}"
    search = VideosSearch(query, limit=1)
    res = search.result()
    
    if res["result"]:
        yt = res["result"][0]["link"]
    else:
        yt = "NOT FOUND"
        
    results.append(yt)

df["youtube_url"] = results
df.to_csv("spotify_youtube_links.csv", index=False)