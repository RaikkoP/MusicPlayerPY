import os;
import pathlib;
from models import Directories

## TODO: Access files from a folder where songs should be located
## TODO: Identify the audio files 

def main():
    test = Directories()
    test.log_directories()

if __name__ == "__main__":
    main();