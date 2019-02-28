import urlfetch
import json
import pandas as pd
from pathlib import Path

# items(track.name,track.id, track.preview_url)  SPOTIFY API

playlist_id = "1GbHiQYx862B3t3BMtQ4kP"

token = "Bearer BQATEiqjGWbP21xcMF91JNy4U76UcUkO31dl-u0s644pQzjLiWJdWxKE300N_sLx-uhrlfK7kXs-bCycjrM" \
        "SkQPhq1opW0y6-hZb1b4QV1PwaMaqEV8yyq9DRoQ2eEy14xf8HJyMrL_wvoPUXuA1nPn4fVhDB9U9LmXhXl9PkbnJLo4hPlE"

header = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": token

}
resp = urlfetch.get(
    'https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks?fields=items(track.name%2Ctrack.id%2C%20track.preview_url)',
    headers=header
)

lib = json.loads(resp.content)['items']

pre_df = []

for track in lib:
    id = track['track']['id']
    name = track['track']['name']

    response = urlfetch.get(
        "https://api.spotify.com/v1/audio-features/" + id,
        headers=header
    )

    v_a = json.loads(response.content)

    valence = v_a['valence']
    arousal = v_a['energy']

    pre_df.append([id, name, valence, arousal])

df = pd.DataFrame(pre_df, columns=['id', 'name', 'valence', 'arousal'])
df.set_index('id', inplace=True)

df.to_json(Path('../emotions_spotify_api') / 'db.json', orient='index')
