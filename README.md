# METADATA EDITOR 
## This script will run through .mp3 files in a designated folder, and edit their metadata according to the arguments given to the command line, which are:
### "-d" is the path to the directory containing the files to be edited.
### "-p" is the name of the performers on the album.
### "-ar" are the artists on the album.
### "-al" is the name of the album.
### "-y" is the year the album was released

## Usage example:
Given that the performer and artist is the same, and we assume we are editing files for the album "2112" by Rush we will use the following cmd line structure:<br>
python main -d "C:/.../Music/Rush/1976 - 2112" -p Rush -ar Rush -al 2112 -y 1976<br>
NOTE: artists/performers with more than one word in their names need the arguments enclosed in double quotation marks ("")!<br><br>
# Possible future additions
* Add the possibility of fetching performer, band/artist name, album name and year from the file name structure (requires user to have a structured file system, which OBVIOUSLY you have, right?)