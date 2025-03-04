import os
import time
import winsound

time.sleep(5)

os.startfile(r"C:\Users\02GABRIEL.WESTRA\Gabriel Westra\Python AI\Python-Learning\prankster\images.jpg")
#Using r before the file path will make it so Python doesn't recognize the \s as escape slashes.
winsound.Playsound(
    r"C:\Users\02GABRIEL.WESTRA\Gabriel Westra\Python AI\Python-Learning\prankster\squeaky-jumpscare-2-102254.mp3",
    flags=winsound.SND_FILENAME
    )
