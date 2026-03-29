# Imports
import argparse
import glob

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

directory_arg = ""


# Main function
def main():
    print("Hello, editor!")
    args = parse_args(directory_arg)
    file_dir = args["album_directory"]
    files_list = find_files(file_dir)
    update_files(files_list, args)
    print("Done!")


# Collect arguments
def parse_args(args):
    print("Parsing args...")
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="Album directory")
    parser.add_argument("-p", "--performer", help="Album performer(s)")
    parser.add_argument("-ar", "--artist", help="Album artist")
    parser.add_argument("-al", "--album", help="Album name")
    parser.add_argument("-y", "--year", help="Album year")
    args = parser.parse_args()
    directory_arg = rf"{args.directory}"
    performers_arg = f"{args.performer}"
    artist_arg = f"{args.artist}"
    album_arg = f"{args.album}"
    year_arg = f"{args.year}" 
    args_dir = {
        "album_directory" : directory_arg,
        "participating_artists" : performers_arg, 
        "album_artist" : artist_arg,
        "album" : album_arg, 
        "year" : year_arg
        }
    print("Returning parsed arguments as list...")
    return args_dir


# Find files from directory argument
def find_files(dir):
    print("Finding files from parsed directory...")
    files = glob.glob(rf"{dir}\*.mp3")
    print("Returning list of files in directory...")
    return files


# Update files in directory with given arguments
def update_files(files, args):
    print("Updating files...")
    track_nr = 1
    for song in files:
        print(f"Updating track # {track_nr}")
        song = MP3(files[int(track_nr - 1)], ID3=EasyID3)
        song["artist"] = args["participating_artists"]
        song["albumartist"] = args["album_artist"]
        song["album"] = args["album"]
        song["date"] = args["year"]
        song["tracknumber"] = str(track_nr)
        song.save()
        track_nr += 1
    print("Files updated! ")

# Execute main function if main
if __name__ == "__main__":
    main()
