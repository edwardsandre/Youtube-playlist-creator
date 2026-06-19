from auth import get_youtube_service

youtube = get_youtube_service()

response = youtube.channels().list(
    part="snippet",
    mine=True
).execute()

print("Connected successfully!")
print("Channel Name:", response["items"][0]["snippet"]["title"])
