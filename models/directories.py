from tkinter.filedialog import askdirectory;

class Directories:
    def  __init__(self, name):
        self.name = name

    def get_new_directory():
        path = askdirectory();
        print(path);
