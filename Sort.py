import os
import json
import time
import getpass
import math

def main():
    username = getpass.getuser()
    filedata = f"C:/Users/{username}/Documents/Sorter/data.json"
    os.makedirs(f"C:/Users/{username}/Documents/Sorter", exist_ok=True)
    data = {
        "Comments": [
            "You Can Change The Files sort and the Folder names",
            "Like.mp3 Go To Folder Called Sounds",
            ".mp3 --> Sounds",
            "And You Don't need to close The app to use the new data",
            "the app will do it for you",
            "And if you want to change the time to sort",
            "like every 20 sec or 60 sec or 120 sec",
            "it's Only sec, The Defult 60 sec",
            "so that's it BYE",
            "Discord: unziv",
            "Youtube: Unziv"
        ],
        "Main Folder Path": f"C:/Users/{username}/Desktop/Files",
        "Files": {
            ".txt": "Text Files",
            ".mp3": "Sounds",
            ".wav": "Sounds",
            ".mpeg": "Sounds",
            ".ogg": "Sounds",
            ".m4a": "Sounds",
            ".mp4": "Videos",
            ".mov": "Videos",
            ".webm": "Videos",
            ".mkv": "Videos",
            ".png": "Images",
            ".jpg": "Images",
            ".jpeg": "Images",
            ".pdf": "Pdfs",
            ".exe": "Apps",
            ".zip": "Zips",
            ".gif": "gifs",
            ".ttf": "Fonts",
            ".msi": "Installers",
            ".docx": "Word",
            ".json": "Json",
            ".xlsx": "Excel",
            ".xltx": "Excel",
            ".xls": "Excel",
            ".jar": "Minecraft/Mods",
            ".mcaddon": "Minecraft/Addons",
            ".mcworld": "Minecraft/Worlds",
            ".mcpack": "Minecraft/Packs"
        },
        "Looking Folders": [
            f"C:/Users/{username}/Desktop",
            f"C:/Users/{username}/Downloads"
        ],
        "Time": 60
    }

    with open(filedata, "r") as file_object:
        data = json.load(file_object)

    while True:
        main_folder_path = data["Main Folder Path"]
        for folder in data["Looking Folders"]:
            for file in os.listdir(folder):
                filepath = os.path.join(folder, file)
                if os.path.isfile(filepath):
                    for extension, destination_folder in data["Files"].items():
                        if file.lower().endswith(extension):
                            new_filepath = os.path.join(main_folder_path, destination_folder, file)
                            if os.path.exists(new_filepath):
                                filename_parts = file.split(".")
                                filename_base, filename_ext = ".".join(filename_parts[:-1]), filename_parts[-1]
                                counter = 2
                                while os.path.exists(os.path.join(main_folder_path, destination_folder, f"{filename_base} ({counter}).{filename_ext}")):
                                    counter += 1
                                os.rename(filepath, os.path.join(main_folder_path, destination_folder, f"{filename_base} ({counter}).{filename_ext}"))
                            else:
                                os.rename(filepath, new_filepath)
        time.sleep(data["Time"])

if __name__ == "__main__":
    main()