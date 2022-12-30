#!/bin/bash

# Colten (Luca) Vance Mikulastik

# some global var
GENRES=()
ALBUMS=()
ARTISTS=()

# functions

# based on teh arg will put the file into the "GENRES", "ALBUMS", "ARTISTS" global arrays
function look_for_directories()
{
    dir_files=""
    for file in $(ls);
    do
        # if the file is a directory, so that we don't change the metadata on the python files, etc...
        if [ -d $file ]
        then
            echo "$file is a directory"
            # if first arg is a _blank_ add it to _blank_ array
            if [[ $1 == "GENRE" ]]
            then
                echo "$file is being added to GENRES array"
                GENRES+=($file)
            fi
            if [[ $1 == "ALBUM" ]]
            then
                echo "$file is being added to ALBUMS array"
                ALBUMS+=($file)
            fi
            if [[ $1 == "ARTIST" ]]
            then
                echo "$file is being added to ARTISTS array"
                ARTISTS+=($file)
            fi
        fi
    done
    # print the effected files
    echo "${dir_files[@]}"    
}

# notify user that I am currently changing the metadata of the mp3 files
echo "Changing file metadata! :^)"

# find the directories for each genre
look_for_directories "GENRE"
look_for_directories "ARTIST"
look_for_directories "ALBUM"

# change into those directories 
for genre in $GENRES
do
    # change into that directory
    echo "GENRE: $genre"

    for artist in $ARTISTS
    do
        echo "ARTIST: $artist"

        for album in $ALBUMS
        do 
            echo "ALBUM: $album"
        done
 
    done

done

