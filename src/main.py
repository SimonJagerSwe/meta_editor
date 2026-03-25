# Imports
import argparse
import os
import sys

# Args
directory_arg = ""
performers_arg = ""
artist_arg = ""
album_arg = ""
year_arg = ""
track_nr = 0
genre_arg = ""
name_replacement_arg = ""
name_insert_arg = ""


# Main function
def main():
    print("Hello, editor!")
    args = parse_args(directory_arg)
    # print(type(args))
    print(args)
    file_dir = args[0]
    print(file_dir)
    files_list = find_files(file_dir)
    print(files_list)


# Collect arguments
def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="Album directory")
    parser.add_argument("-p", "--performer", help="Album performer(s)")
    parser.add_argument("-ar", "--artist", help="Album artist")
    parser.add_argument("-al", "--album", help="Album name")
    parser.add_argument("-y", "--year", help="Album year")
    parser.add_argument("-g", "--genre", help="Album year")
    parser.add_argument("-r", "--replacement", help="Characters in song titles to remove")
    parser.add_argument("-i", "--insert", help="Character to be inserted in place of removed character")
    args = parser.parse_args()
    directory_arg = rf"{args.directory}"
    performers_arg = f"{args.performer}"
    artist_arg = f"{args.artist}"
    album_arg = f"{args.album}"
    year_arg = f"{args.year}"
    genre_arg = f"{args.genre}"    
    args_list = [directory_arg, 
                 performers_arg, 
                 artist_arg, 
                 album_arg, 
                 year_arg, 
                 genre_arg]
    if args.replacement is not None:
        name_replacement_arg = f"{args.replacement}"
        args_list.append(name_replacement_arg) # 
        name_insert_arg = f"{args.insert}"
        args_list.append(name_insert_arg)
    return args_list

def find_files(dir):
    song_list = []
    print("Fetching files...")
    for song in os.listdir(dir):
        song = song.title()
        song_list.append(song)
    return song_list

# Execute main function if main
if __name__ == "__main__":
    main()