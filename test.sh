#!/bin/bash

GENRE=()
ARTIST=()
ALBUMS=()

function tester()
{

    dir_files=""
    for file in $(ls);
    do
        if [ -d $file ]
        then
            echo "$file is a directory"
            if [[ $1 == "GENRE" ]]
            then
                echo "$file is being added to GENRE array"
                GENRE+=($file)
            fi
        fi
    done
    echo "${dir_files[@]}"
}

tester "GENRE"

echo "${GENRE[@]}"
echo "${ARTIST[@]}"
echo "${ALBUMS[@]}"
