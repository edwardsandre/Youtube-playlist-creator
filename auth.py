import os
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube"]
TOKEN_PATH = "token.pickle"
CREDENTIALS_PATH = "credentials.json"


def get_youtube_service():
    credentials = None

    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, "rb") as token:
            credentials = pickle.load(token)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            credentials = flow.run_local_server(port=0)

        with open(TOKEN_PATH, "wb") as token:
            pickle.dump(credentials, token)

    return build("youtube", "v3", credentials=credentials)
