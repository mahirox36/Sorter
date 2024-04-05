@REM git pull origin
git add .
git commit -m "Updating Sorter"
git push origin
pyinstaller --noconfirm --onefile --windowed --icon "G:/My Drive/TwinPixel/Icon/Normal/Icon.ico" --name "Sorter" --clean "N:/python/Sorter/Sort.py" --hidden-import=_thread --hidden-import=win10toast --hidden-import=pkg_resources
python make.py