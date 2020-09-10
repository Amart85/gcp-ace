from __future__ import print_function
import pickle
import os.path
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class GSuiteUser():
    def __init__(self, FirstName, LastName, pw, email):
        self.name = {"familyName": LastName, "givenName": FirstName}
        self.password = pw
        self.primaryEmail = email
        self.service = ""
        super().__init__()
    
    def CreateUser(self):
        # If modifying these scopes, delete the file token.pickle.
        SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']
        creds = None
        # The file supersecret.token stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('supersecret.token'):
            with open('supersecret.token', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('supersecret.token', 'wb') as token:
                pickle.dump(creds, token)

        self.service =  build('admin', 'directory_v1', credentials=creds)
        try:
            results = self.service.users().insert(body=self.__dict__).execute()
        except:
            print(f"User {self.name} already exits.")

def Main():
    jb = GSuiteUser("Jack", "Black", "SuperSecret1234!@#$", "jackblack@elsersmusings.com")
    jb.CreateUser()

Main()