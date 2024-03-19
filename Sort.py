import os
import json
import time
import getpass
import math
os.system("cls")
username = getpass.getuser()
filedata = f"C:/Users/{username}/Documents/Sorter/data.json"
os.makedirs(f"C:/Users/{username}/Documents/Sorter",exist_ok=True)
data = {
    "Comments": [
        "You Can Change The Files sort and the Folder names",
        "Like .mp3 Go To Folder Called Sounds",
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
        ".txt"    : "Text Files",
        ".mp3"    : "Sounds",
        ".wav"    : "Sounds",
        ".mpeg"   : "Sounds",
        ".ogg"    : "Sounds",
		".m4a"    : "Sounds",
        ".mp4"    : "Videos",
        ".mov"    : "Videos",
		".webm"   : "Videos",
		".mkv"    : "Videos",
        ".png"    : "Images",
        ".jpg"    : "Images",
		".jpeg"   : "Images",
        ".pdf"    : "Pdfs",
        ".exe"    : "Apps",
        ".zip"    : "Zips",
        ".gif"    : "gifs",
        ".ttf"    : "Fonts",
		".msi"    : "Installers",
		".docx"   : "Word",
		".json"   : "Json",
		".xlsx"   : "Excel",
		".xltx"   : "Excel",
		".xls"    : "Excel",
		".jar"    : "Minecraft/Mods",
		".mcaddon": "Minecraft/Addons",
		".mcworld": "Minecraft/Worlds",
		".mcpack" : "Minecraft/Packs"
    },
    "Looking Folders":[
        f"C:/Users/{username}/Desktop",
        f"C:/Users/{username}/Downloads"
    ],
    "Time": 60
}
while True:
    main = data["Main Folder Path"]
    try:
        with open(filedata) as filee: 
            data = json.load(filee)
    except:
        with open(filedata,'w') as filee:
            json.dump(data, filee, indent=4)
    os.makedirs(main,exist_ok=True)
    for i in data["Looking Folders"]:
        for j in os.listdir(i):
            try:
                j = str(j)
                k = f"{i}/{j}"
                if os.path.isfile(k):
                    for key, vaalue in data["Files"].items():
                        os.makedirs(f"{main}/{vaalue}",exist_ok=True)
                        if j.lower().endswith(key):
                            if os.path.exists(f"{main}/{vaalue}/{j}"):
                                j = j.split(".")
                                last_item = j[-1]
                                j.remove(last_item)
                                h = ""
                                num = 1
                                for l in j:
                                    h = f"{h}{l}."
                                for jkl in range(math.inf):
                                    j = f"{h}{num}.{last_item}"
                                    if os.path.exists(f"{main}/{vaalue}/{j}"):
                                        num+=1
                                        continue
                                    break
                                
                                os.rename(k, f"{main}/{vaalue}/{j}")
                                break
                            os.rename(k, f"{main}/{vaalue}/{j}")
                            break
            except:
                continue

    time.sleep(data["Time"])