from tkinter import *;
from tkinter.filedialog import askdirectory
from typing import List
from .directory import Directory

class Directories:
    current_directories: List[Directory] = []

    def  __init__(self):
        self.current_directories = []
        self.add_new_directory()

    ## Gets a new directory of songs and saves it
    def add_new_directory(self):
        path = askdirectory()
        #TODO: TK should open a pop up for the name
        demo = 'demo'
        new_directory = Directory(demo, path)
        self.current_directories.append(new_directory)

    def log_directories(self):
        print(f"{self.current_directories[0].path} <----")