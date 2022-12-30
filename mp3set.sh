#!/bin/bash

# Colten (Luca) Vance Mikulastik
# working on seeing all the files, somehow bash doesn't see CC as a directory and will halt the function when coming to it...
# this is really awesome :^)

# some global var
GENRES=()
ALBUMS=()
ARTISTS=()

# functions

# based on teh arg will put the file into the "GENRES", "ALBUMS", "ARTISTS" global arrays, argument 2 will be path
function look_for_directories()
{
    echo $2
    echo $(ls $2)
    dir_files=()
    for file in $(ls $2);
    do
        echo "test!!!!!!!!!!! $file"
        # if the file is a directory, so that we don't change the metadata on the python files, etc...
        if [[ -d $file || $file == "CC" ]]
        then
            echo "$file is a directory"
            # if first arg is a _blank_ add it to _blank_ array
            if [[ $1 == "GENRE" ]]
            then
                echo "$file is being added to GENRES array"
                GENRES+=($file)

            elif [[ $1 == "ALBUM" ]]
            then
                echo "$file is being added to ALBUMS array"
                ALBUMS+=($file)
            
            elif [[ $1 == "ARTIST" ]]
            then
                echo "$file is being added to ARTISTS array"
                ARTISTS+=($file)
            else
                echo "$file has not be chosen to be in an array"
            fi
        else
            echo "$file is not a directory"
        fi
    done
    # print the effected files
    echo "${dir_files[@]}"    
}



# notify user that I am currently changing the metadata of the mp3 files
echo "Changing file metadata! :^)"

working_dir=$(pwd)

# find the directories for each genre
look_for_directories "GENRE" $working_dir

# change into those genre's directories 
for genre in $GENRES
do
    echo "GENRE: $genre"
    
    # find the artists in the genre directory
    look_for_directories "ARTIST" $working_dir/$genre
    for artist in $ARTISTS
    do
        echo "ARTIST: $artist"
        
        # find the albums in artist directory
        look_for_directories "ALBUM" $working_dir/$genre/$artist

        # loop through each album
        for album in $ALBUMS
        do
            echo "ALBUM: $album" 
            
            # loop through the songs
            for song in $(ls $working_dir/$genre/$artist/$album)
            do
                echo "$song"
            done
        done
    done

done

cd $working_dir

echo "${GENRES[@]}"
echo "${ALBUMS[@]}"
echo "${ARTISTS[@]}"
