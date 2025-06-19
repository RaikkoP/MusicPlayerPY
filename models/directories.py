from tkinter import *;
from tkinter.filedialog import askdirectory
from utils.helpers import get_text_input_from_display

class Directories:

    current_directories = []
    display = Tk()
    display.geometry("300x300")
    display.title("Name the directory")

    def  __init__(self):
        self.get_new_directory()

    def display_get_directory_name(self):
        label = Label(text= "Type in a name for directory:")
        window = Text(self.display, height=10
                      , width=24)
        def on_confirm():
            return get_text_input_from_display(window)
        button = Button(self.display, height = 2,
                width=20,
                text="Confirm",
                command=on_confirm)

        label.pack()
        window.pack()
        button.pack()

        return

    def get_new_directory(self):
        path = askdirectory()
        self.add_new_directory(path)

    def add_new_directory(self, directory):
        ## get name for new directory of songs
        name = self.display_get_directory_name()
        self.current_directories.append(directory)

    def log_directories(self):
        print(self.current_directories) 
