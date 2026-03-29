# Imports
import argparse
import glob
import numpy as np
import os

from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TIT2, TIT3, TALB, TPE1, TRCK, TYER
from mutagen.mp3 import MP3

file_dir = r"C:\Users\simon\OneDrive\Skrivbord\Musik\Mick Hanly\test\*.mp3"
album = "Born to Run"
artist = "Bruce Springsteen"
album_artist = "Bruce Springsteen"
track_number = 1
year = "1975"

files = glob.glob(file_dir)

for file in files:
    mp3file = MP3(files[track_number - 1], ID3=EasyID3)
    print(mp3file)
    '''mp3file["album"] = album
    mp3file["artist"] = artist
    mp3file["albumartist"] = album_artist
    mp3file["tracknumber"] = str(track_number)
    mp3file["date"] = year    
    mp3file.save()'''
    track_number += 1