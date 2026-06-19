import csv

BEAT_KEYWORDS = [
    "type beat",
    "beat",
    "instrumental",
    "[free]",
    "free beat",
    "free type beat",
    "prod.",
    "prod by",
]

filtered = []

with open("liked_videos.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:

        title = row["title"].lower()

        if any(keyword in title for keyword in BEAT_KEYWORDS):
            filtered.append(row)

with open("beats.csv", "w", newline="", encoding="utf-8") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=["video_id", "title", "channel"]
    )

    writer.writeheader()
    writer.writerows(filtered)

print(f"Found {len(filtered)} likely beat videos")