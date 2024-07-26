import requests
from tkinter import messagebox
__version__ = "2.2"
needUpdate = False
url = "https://raw.githubusercontent.com/mahirox36/Sorter/main/Version.txt"
try:
    # Fetch the remote version
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    remote_version = response.text.strip()  # Remove any extra whitespace
    
    # Compare versions
    if float(remote_version) > float(__version__):
        print("Updating")
        needUpdate = True

except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching the remote version: {e}")

if needUpdate == False:
    messagebox.showinfo("No Update Found","You are in the latest update")
else:
    #TODO: Continue this file later
    pass