import os, random
from pathlib import Path

### Config:

wallpapers_PATH = f"{Path.home()}/Pictures/wallpapers"

######

wallpaper = random.choice(os.listdir(wallpapers_PATH))
wallpaper_PATH = f"{wallpapers_PATH}/{wallpaper}"

string = f"gsettings set org.gnome.desktop.background picture-uri-dark file:///{wallpaper_PATH}"

os.system(string)
