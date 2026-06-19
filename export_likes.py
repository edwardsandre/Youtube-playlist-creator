import csv

from auth import get_youtube_service

youtube = get_youtube_service()

videos = []
next_page_token = None

while True:

    response = youtube.playlistItems().list(
        part="snippet",
        playlistId="LL",
        maxResults=50,
        pageToken=next_page_token
    ).execute()

    for item in response["items"]:

        snippet = item["snippet"]

        videos.append([
            snippet["resourceId"]["videoId"],
            snippet["title"],
            snippet.get("videoOwnerChannelTitle", "")
        ])

    next_page_token = response.get("nextPageToken")

    print(f"Collected {len(videos)} videos...")

    if not next_page_token:
        break

with open("liked_videos.csv", "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow([
        "video_id",
        "title",
        "channel"
    ])

    writer.writerows(videos)

print(f"\nFinished. Exported {len(videos)} videos.")
