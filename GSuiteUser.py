from __future__ import print_function
import pickle
import os.path
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class GSuiteUser():
    def __init__(self, FirstName, LastName, pw, email, DirectoryAPIService):
        self.name = {"familyName": LastName, "givenName": FirstName}
        self.password = pw
        self.primaryEmail = email
        self.id = ""
        super().__init__()
        
    
    def CreateUser(self, DirectoryAPIService):
        try:
            results = DirectoryAPIService.users().insert(body=self.__dict__).execute()
            self.id = results.get("id", [])
        except Exception as e:
            print(f"User {self.name} already exits.")
    
    @staticmethod
    def NewGSuiteUser(FirstName, LastName, pw, email, DirectoryAPIService):
        g = GSuiteUser(FirstName, LastName, pw, email, DirectoryAPIService)
        g.CreateUser(DirectoryAPIService)
        return g
        


