import ctypes

directory = r"C:\Users\JGarza\Pictures"
imagePath = directory + "\Windows_10.jpg"

def changeBG(imagePath):
    # SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, imagePath , 3)
    return;

changeBG(imagePath)