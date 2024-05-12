__version__ = "2.0"
import os
import json
import pathlib
import time
import getpass
from tkinter import messagebox
import sys
import threading
from PIL import Image
from pystray import MenuItem as item
import pystray
import psutil
# import win10toast

Shutdown = False

def create_popup(title ,message, status:str = "info"):
    if status == "info":
        messagebox.showinfo(title, message)
    elif status == "warning":
        messagebox.showwarning(title, message)
    elif status == "error":
        messagebox.showerror(title, message)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def create_folder_in_appdata(folder_name):
    appdata_folder = pathlib.Path(os.environ["APPDATA"])
    new_folder_path = appdata_folder / folder_name

    try:
        os.makedirs(new_folder_path,exist_ok=True)
    except Exception as e:
        print("Error creating folder:", e)
def write_to_appdata(data, filename="Sorter/data.json"):
    appdata_folder = pathlib.Path(os.environ["APPDATA"])
    file_path = appdata_folder / filename

    try:
        with open(file_path, "w") as file_object:
            json.dump(data, file_object, indent=4)
    except Exception as e:
        print("Error writing to file:", e)
def read_from_appdata(filename="Sorter/data.json"):
    appdata_folder = pathlib.Path(os.environ["APPDATA"])
    file_path = appdata_folder / filename

    try:
        with open(file_path, "r") as file_object:
            return json.loads(file_object.read())
    except FileNotFoundError as e:
        return False
    except Exception as e:
        print("Error writing to file:", e)
def filepath_appdata(filename="Sorter/data.json"):
    appdata_folder = pathlib.Path(os.environ["APPDATA"])
    file_path = appdata_folder / filename
    return file_path


def is_app_already_running():
    """ Check if the app is already running. """
    for proc in psutil.process_iter(['name']):
        if proc.name() == "Sorter.exe":
            return True
    return False


def main():
    # toaster = win10toast.ToastNotifier()
    # toaster.show_toast("Sorter", "The App is Running!", duration=10)
    create_folder_in_appdata("Sorter")
    
    username = getpass.getuser()
    Main_data = {
        "Comments": [
            "You Can Change The Files sort and the Folder names",
            "Like.mp3 Go To Folder Called Sounds",
            ".mp3 --> Sounds",
            "And You Don't need to close The app to use the new data",
            "the app will do it for you",
            "And if you want to change the time to sort",
            "like every 20 sec or 60 sec or 120 sec",
            "it's Only sec, The Default 60 sec",
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
            ".pdf": "PDF",
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
    data = read_from_appdata()
    if data != False:
        pass
    else:
        write_to_appdata(Main_data)
        data = Main_data

    while Shutdown == False:
        if os.path.exists(data["Main Folder Path"]) == False:
            os.makedirs(data["Main Folder Path"])
        main_folder_path = data["Main Folder Path"]
        for folder in data["Looking Folders"]:
            for file in os.listdir(folder):
                filepath = os.path.join(folder, file).replace("\\", "/")
                if os.path.isfile(filepath):
                    for extension, destination_folder in data["Files"].items():
                        if file.lower().endswith(extension):
                            if os.path.exists(os.path.join(main_folder_path, destination_folder).replace("\\", "/")) == False:
                                os.makedirs(os.path.join(main_folder_path, destination_folder).replace("\\", "/"))
                            new_filepath = os.path.join(main_folder_path, destination_folder, file).replace("\\", "/")
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




def open_file(file_path):
    try:
        os.startfile(filepath_appdata())
    except Exception as e:
        print("Error opening file:", e)


def on_settings():
    print(filepath_appdata())
    open_file(filepath_appdata())
def on_quit():
    icon.visible = False
    global Shutdown
    Shutdown = True
    icon.stop()
    thread.join()

if __name__ == "__main__":
    if is_app_already_running() == True:
        create_popup("Sorter", "The App is Already Running","warning")
    else:    
        thread = threading.Thread(target=main)
        thread.start()
        image = Image.open(resource_path("icon.ico"))
        menu = (
            item('Settings', on_settings),
            item('Quit', on_quit)
            )
        icon = pystray.Icon("Sorter", image, "Sorter", menu)
        icon.run()
