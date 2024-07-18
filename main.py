__version__ = "2.1"
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
from Lib.config import Config
# import win10toast
appdata_folder = pathlib.Path(os.environ["APPDATA"])
file_path = os.path.join(appdata_folder, "Mahiro/Sorter/data.conf")
config = Config(file_path)
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

def filepath_appdata(filename="Mahiro/Sorter/data.conf"):
    appdata_folder = pathlib.Path(os.environ["APPDATA"])
    file_path = os.path.join(appdata_folder, filename).replace("\\", "/")
    return file_path

def is_app_already_running():
    """ Check if the app is already running. """
    count = 0
    for proc in psutil.process_iter(['name']):
        if proc.name() == "Sorter.exe":
            count += 1
    if count > 2:
        return True
    return False

def checker(username:str):
    layout = [
        "general",
        "files",
        "Looking Folders"]
    try:
        config.load()
    except FileNotFoundError as e:
        config.set_layout(layout)
        config["general"].update({
            "MainFolderPath": f"C:/Users/{username}/Desktop/Files",
            "Time": 60
        })
        config.create_comment("Here You can Change the Main Folder Path and Name",
                               "general", "MainFolderPath")
        config.create_comment(f"Default: C:/Users/{username}/Desktop/Files",
                               "general", "MainFolderPath")
        config.create_comment("Here You can Change the Time to Sort",
                               "general", "Time")
        config.create_comment(f"Default: 60",
                               "general", "Time")

        config["files"].update({
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
            })
        config.create_comment("Here You can Change the Files sort and the Folder names",
                              "files", ".txt")
        config.create_comment("Like.mp3 Go To Folder Called Sounds",
                              "files", ".txt")
        config.create_comment(".mp3 --> Sounds",
                              "files", ".txt")
        config.create_comment("You can add how many files you want",
                              "files", ".txt")
        config["Looking Folders"]=[
            f"C:/Users/{username}/Desktop",
            f"C:/Users/{username}/Downloads"
        ]
        config.create_comment("Here You can Change The Looking Folders",
                              "Looking Folders", 0)
        config.save(True)
    return config.get_data()
def main():
    # toaster = win10toast.ToastNotifier()
    # toaster.show_toast("Sorter", "The App is Running!", duration=10)
    create_folder_in_appdata("Sorter")
    username = getpass.getuser()
    # config.create_comment("Discord: mahirox36") config.create_comment("Youtube: @Mahiro36")
    data = checker(username)
    
    while Shutdown == False:
        data = checker(username)
        if os.path.exists(data["general"]["MainFolderPath"]) == False:
            os.makedirs(data["general"]["MainFolderPath"])
        main_folder_path = data["general"]["MainFolderPath"]
        for folder in data["Looking Folders"]:
            for file in os.listdir(folder):
                filepath = os.path.join(folder, file).replace("\\", "/")
                if os.path.isfile(filepath):
                    for extension, destination_folder in data["files"].items():
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
        time.sleep(data["general"]["Time"])

def open_file(file_path):
    try:
        os.startfile(file_path)
    except Exception as e:
        print("Error opening file:", e)

def on_settings():
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