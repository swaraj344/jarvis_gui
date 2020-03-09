import ctypes
import random
import os
import access_key
import requests
import wget
# import gui
from threading import Thread

def getWallpaper():
    url = 'https://api.unsplash.com/photos/random/?client_id='+access_key.access_key
    params = {
        'query':'HD wallpapers',
        'orientation':'landscape'
    }
    response = requests.get(url,params=params).json()
    image_source = response['urls']['full']
    # gui.speak("Downloading")
    # gui.update("Downloading...... please Wait","green")
    image = wget.download(image_source,'E:/wallpapers/netwallpaper.jpg')
    return image

def setlocalwallpaper():
    wallpapers = os.listdir("E:/wallpapers")
    wallpaper = random.choice(wallpapers)
    path = os.path.join("E:/wallpapers",wallpaper)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)

def setwallpaper():
    wallpaper = getWallpaper()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper , 0)

def IsInternet():
    response = requests.get("http://google.com")
    return response.status_code


def main():
    if IsInternet() == 200:
        # gui.speak("Setting Wallpaper!!")

        try :
            setwallpaper()
            # gui.speak("Setting Wallpaper Successful")
            

        except Exception as e:
            print("Exception :"+e)
    else:
        print("Not Connected to internet")
        # gui.update("You Are Not Connected To the Internet","red")
        # gui.speak("Setting wallpaper locally")
        setlocalwallpaper()
        # gui.speak("Setting Wallpaper Successful")

if __name__ == "__main__":
    main()
    
    