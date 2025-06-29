from tkinter import *;
from tkinter.filedialog import askdirectory
from typing import List
from .directory import Directory
import json
import os

#TODO: Make it support youtube playslits instead
#TODO: Save playlist information in a JSON so we can check, if there are already saved ones
class Directories:
    playlists: List[Directory] = []

    def  __init__(self):
      self.playlists = []
      if (os.path.isFile('../data/data.json') == False):
        self.add_new_directory()

    ## Gets a new directory of songs and saves it"
    def add_new_directory(self):
        path = askdirectory()
        #TODO: TK should open a pop up for the name
        demo = 'demo'
        new_directory = Directory(demo, path)
        self.playlists.append(new_directory)

    def log_directories(self):
        print(f"{self.playlists[0].path} <----")
