@REM git pull origin
git add .
git commit -m "Updating Sorter"
git push origin
pyinstaller --noconfirm --onefile --windowed --icon "G:/My Drive/TwinPixel/Icon/Normal/Icon.ico" --name "Sorter" --clean "N:/python/Sorter/main.py" --add-data "N:/python/Sorter/Icon.ico;." --hidden-import=_thread --hidden-import=win10toast --hidden-import=pkg_resources --hidden-import=pystray --hidden-import=psutil
python make.py