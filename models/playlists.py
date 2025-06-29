from tkinter import *;
from .playlist import Playlist
import os

#TODO: Make it support youtube playslits instead
#TODO: Save playlist information in a JSON so we can check, if there are already saved ones
class Playlists:
    playlists = []

    def  __init__(self):
      if (os.path.exists('./data/data.json') == False):
        os.makedirs("./data", exist_ok=True)
        self.add_new_directory()
      else:
        return

    ## Gets a new directory of songs and saves it"
    def add_new_directory(self):
        #TODO: TK to ask for the URL of the playlist
        demo = "test"
        Playlist(demo)

    def log_directories(self):
        print(f"{self.playlists[0].path} <----")
