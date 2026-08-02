import json  
import os    


class Storage:

    def load_data(self, file_name):

        if not os.path.exists(file_name):
            return []
        with open(file_name, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    def save_data(self, filename, data):

        with open(filename, "w") as file:
            json.dump(data, file, indent=3)