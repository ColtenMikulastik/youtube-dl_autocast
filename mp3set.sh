#!/bin/bash

# save the directory that we are working in
working_dir=$(pwd)

# loop through all directories and change the appropriate material
for genre in $working_dir/*
do
    if [[ -d "$genre" ]]
    then
        for artist in "$genre"/*
        do
            for album in "$artist"/*
            do
                for song in "$album"/*
                do
                    unpathed_genre=$(echo "$genre" | awk -F'/' '{print $NF}')
                    unpathed_artist=$(echo "$artist" | awk -F'/' '{print $NF}')
                    unpathed_album=$(echo "$album" | awk -F'/' '{print $NF}')
                    unpathed_song=$(echo "$song" | awk -F'/' '{print $NF}')
                    song_number=$(echo "$unpathed_song" | awk -F' ' '{print $1}')
                    song_name=$(echo "$unpathed_song" | cut -c 4-)
                    echo "$song_name is song number ($song_number) on the album: $unpathed_album by $unpathed_artist in the genre $unpathed_genre"
                    id3tool --set-title="$song_name" --set-album="$unpathed_album" --set-artist="$unpathed_artist" --set-genre-word="$unpathed_genre" --set-track="$song_number" "$song"
                done
            done
        done
    fi

done


