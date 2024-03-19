# Sorter
This App Will Sort Your Files In Folders

## Requirements
Python 3.10 or higher
Windows Operating System


## How to use
1.
Download the latest version of the Sorter App from the [releases page](https://github.com/Unziv/Sorter/releases).
2.
Extract the downloaded file to a directory of your choice.
3.
Double click on the ```Sorter.exe``` file to start the app.
4.
If you are prompted to enter a time interval, enter the number of seconds you want the app to wait before sorting again. The default value is 60 seconds.
5.
To adjust the settings, you need to modify the ```data.json``` file located at ```C:/Users/{username}/Documents/Sorter/data.json```.
6.
That's it! The app will now sort your files into folders according to the settings.


## How it works
The Sorter App scans the specified folders and looks for files with the specified extensions. It then renames the files to include a unique number, if a file with the same name already exists in the destination folder. This process is repeated until a unique name is found for the file.

## Contributing
If you find a bug or have an idea for a new feature, please open an issue or a pull request on the [GitHub repository](https://github.com/Unziv/Sorter).

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Unziv/Sorter/blob/main/LICENSE) file for details.
