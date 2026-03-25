# Imports
import argparse
import os
import sys

# Constants

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
    args = parse_args(performers_arg)
    print(args)


# Collect arguments
def parse_args():
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
    directory_arg = f"{args.directory}"
    performers_arg = f"{args.performer}"
    artist_arg = f"{args.artist}"
    album_arg = f"{args.album}"
    year_arg = f"{args.year}"
    genre_arg = f"{args.genre}"
    name_replacement_arg = f"{args.replacement}"
    name_insert_arg = f"{args.insert}"
    return [
        directory_arg,
        performers_arg,
        artist_arg,
        album_arg,
        year_arg,
        genre_arg,
        name_replacement_arg,
        name_insert_arg
        ]

# Execute main function if main
if __name__ == "__main__":
    main()