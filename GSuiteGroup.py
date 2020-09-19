from __future__ import print_function
import pickle
import os.path
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class GSuiteGroup():
    def __init__(self, email, description, displayname, DirectoryAPIService):
        self.email = email
        self.description = description
        self.name = displayname
        self.id = ""
        super().__init__()
    
    def CreateGroup(self, DirectoryAPIService):
        try:
            results = DirectoryAPIService.groups().insert(body=self.__dict__).execute()
            self.id = results.get("id", [])
        except Exception as e:
            print(e)
            print(f"Group {self.name} already exits.")
    
    def AddMember(self, id, DirectoryAPIService):
        if id == "":
            bre
        try:
            body = {
                    "id": id,
                    "role": "MEMBER"
                }
            
            print(body)
            results = DirectoryAPIService.members().insert(groupKey=self.id, body=body).execute()
        except Exception as e:
            print(e)
            print(f"Something went wrong adding member with ID: {id}")
    
    def AddOwner(self, id, DirectoryAPIService):
        try:
            body = {
                    "id": id,
                    "role": "OWNER"
                }
            
            print(body)
            results = DirectoryAPIService.members().insert(groupKey=self.id, body=body).execute()
        except Exception as e:
            print(e)
            print(f"Something went wrong adding owner with ID: {id}")
    
    @staticmethod
    def NewGSuiteGroup(email, description, displayname, DirectoryAPIService):
        g = GSuiteGroup(email, description, displayname, DirectoryAPIService)
        g.CreateGroup(DirectoryAPIService)
        return g
        
