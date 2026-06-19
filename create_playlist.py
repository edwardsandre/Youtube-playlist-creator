from auth import get_youtube_service

PLAYLIST_TITLE = "beats"

youtube = get_youtube_service()

existing_id = None
next_page_token = None

while True:

    response = youtube.playlists().list(
        part="snippet",
        mine=True,
        maxResults=50,
        pageToken=next_page_token
    ).execute()

    for playlist in response["items"]:

        if playlist["snippet"]["title"].lower() == PLAYLIST_TITLE:
            existing_id = playlist["id"]
            break

    if existing_id:
        break

    next_page_token = response.get("nextPageToken")

    if not next_page_token:
        break

if existing_id:
    print("Playlist already exists, skipping creation.")
    print("Playlist ID:", existing_id)
else:
    response = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": PLAYLIST_TITLE,
                "description": "Auto generated beat playlist"
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    ).execute()

    print("Playlist created!")
    print("Playlist ID:", response["id"])
