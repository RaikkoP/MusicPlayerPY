import json
import os

class Playlist:
    name: str = ""
   
    def __init__(self, name):
      self.name = name
      if os.path.exists("./data/data.json"):
        with open("./data/data.json", "r") as f:
          data = json.load(f)
      else:
        data = []
      data.append({"name": self.name})

      with open('./data/data.json', 'w') as f:
          json.dump(data, f, indent=2)

    def autism():
      return dict

    def current_path(self):
        return self.path

    def current_name(self):
        return self.name
