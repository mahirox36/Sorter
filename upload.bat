@REM git pull origin
git add .
git commit -m "Updating Sorter"
git push origin
pyinstaller --noconfirm --onefile --windowed --icon "G:/My Drive/TwinPixel/Icon/Normal/Icon.ico" --name "Sorter" --clean --hidden-import=_thread --hidden-import=win10toast --hiden-import=pkg_resources "N:/python/Sorter/Sort.py"
python make.py