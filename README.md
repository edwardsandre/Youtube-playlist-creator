# YouTube Instrumental Playlist Creator

A simple Python automation that scans your YouTube Liked Videos, identifies videos containing specified keywords (such as instrumental music), and automatically creates a dedicated playlist containing those videos.

## Purpose

Many people save instrumentals, lo-fi beats, study music, background tracks, and similar content to their YouTube Liked Videos over time. However, finding those tracks again can be difficult when mixed in with hundreds or thousands of other liked videos.

This tool solves that problem by:

- Reading videos from your YouTube Liked Videos.
- Searching for user-defined keywords.
- Automatically creating a new playlist.
- Adding all matching videos to that playlist.

Perfect for:

- Students
- Developers
- Remote workers
- Content creators
- Anyone who listens to background music while working or studying

## Features

- Connects directly to the YouTube Data API.
- Reads videos from your Liked Videos playlist.
- Searches titles for specific keywords.
- Creates a playlist automatically if it does not already exist.
- Adds matching videos to the playlist.
- Fully customizable keyword filtering.
- Easy to modify for different playlist categories.

## Example Use Cases

### Study Instrumentals

Keywords:

```python
["instrumental", "study beat", "lofi", "lo-fi"]
