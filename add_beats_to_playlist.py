import csv
import time

from googleapiclient.errors import HttpError

from auth import get_youtube_service

PLAYLIST_TITLE = "beats"

youtube = get_youtube_service()

# Find playlist called "beats"

playlist_id = None
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
            playlist_id = playlist["id"]
            break

    if playlist_id:
        break

    next_page_token = response.get("nextPageToken")

    if not next_page_token:
        break

if not playlist_id:
    raise Exception(f"Could not find playlist named '{PLAYLIST_TITLE}'")

print(f"Found playlist: {playlist_id}")

# Collect videos already in the playlist, so re-runs don't add duplicates

existing_ids = set()
next_page_token = None

while True:

    response = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=50,
        pageToken=next_page_token
    ).execute()

    for item in response["items"]:
        existing_ids.add(item["snippet"]["resourceId"]["videoId"])

    next_page_token = response.get("nextPageToken")

    if not next_page_token:
        break

# Read beats.csv

videos = []

with open("beats.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        videos.append(row["video_id"])

to_add = [video_id for video_id in videos if video_id not in existing_ids]
skipped = len(videos) - len(to_add)

print(f"{len(videos)} videos in beats.csv, {skipped} already in playlist, adding {len(to_add)} new")

# Add videos

success = 0
failed = 0

for index, video_id in enumerate(to_add, start=1):

    try:

        youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id
                    }
                }
            }
        ).execute()

        success += 1

        print(f"[{index}/{len(to_add)}] Added {video_id}")

        time.sleep(0.1)

    except HttpError as e:

        failed += 1

        print(f"[{index}/{len(to_add)}] Failed {video_id}")
        print(e)

print("\nFinished")
print(f"Added: {success}")
print(f"Failed: {failed}")
print(f"Skipped (already in playlist): {skipped}")
