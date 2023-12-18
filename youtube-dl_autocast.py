# Luca (Colten) Mikulastik: 3/13/2022

import csv
import os
import yt_dlp
import requests
import time
# from bs4 import BeautifulSoup


def album_cover_art_dl(var_working_path, var_artist, var_album, max_releases):
    """ downloads an album cover for a specific album and artist """
    params = {
        "fmt": "json"
    }
    reply = requests.get("http://musicbrainz.org/ws/2/release/?query=release:\"" + var_album + "\" AND artist:\"" + var_artist + "\"", params=params)

    print("downloading album cover art")
    # make sure that we got a good request
    if reply.status_code == 200:
        reply_dict = reply.json()

        # loop through releases until we go past 10, or we find a cover
        releases = reply_dict["releases"]
        for release in releases[:max_releases]:
            if release["score"] == 100:
                # sleep so we don't get blocked
                time.sleep(1.1)

                # use releases' id and change to dict
                cover_reply = requests.get("http://coverartarchive.org/release/" + release["id"])
                if cover_reply.status_code == 200:
                    cover_reply = cover_reply.json()

                    # get img url from cover reply
                    img_url = cover_reply["images"][0]["image"]

                    # make file name and write image to file
                    file_name = os.path.join(var_working_path, "albumcover.jpg")
                    time.sleep(1.1)
                    img = requests.get(img_url)
                    if img.status_code == 200:
                        with open(file_name, "wb") as img_file:
                            img_file.write(img.content)
                            # leave loop
                            break  # could remove line to keep bunch of art
                    else:
                        print("Failure Occured when requesting Image")
                else:
                    print("Cover Art Archive api request failure")
    else:
        print("Musicbrainz api request failure")


def mp3set(genre, artist, album):
    """ sets the mp3 tags with id3tag """
    # dictionary that holds mappings of genre str to id3 int value
    id3_genre_conv = {}

    # unload the csv with the mappings of the id3 genre tags, omtting weird key
    with open("id3_conv.csv", newline='') as conv_file:
        reader = csv.reader(conv_file)
        for feild in reader:
            id3_genre_conv[feild[1]] = int(feild[0])

    # get path, and all songs
    active_path = os.path.join(os.curdir, genre, artist, album)
    songs = os.listdir(active_path)

    # attempt to convert genre, if not found default to None=255
    try:
        id3_genre = id3_genre_conv[genre]
        pass
    except KeyError:
        print("Genre not recognized, default None")
        id3_genre = id3_genre_conv["None"]

        os.path

    # loop through each song, and !!!!album art!!!!
    for song_file in songs:
        # fix formatting of song and data
        # remove the number
        song = song_file.split(" ")
        song_num = song[0]

        # parse song name from file name
        song[-1] = song[-1].split(".")[0]
        song_name = " ".join(song[1:])

        # craft our bash command
        cmd = "id3tag -s \"" + song_name + "\" -t " + str(song_num) + " -a \"" + artist + "\" -A \"" + album + "\" -g " + str(id3_genre) + " \"" + os.path.join(active_path, song_file) + "\""
        # send command
        os.system(cmd)


def yt_dlp_download(youtube_url, varPath):
    """ calls and downloads youtube videos with yt-dlp """
    # options need to be specified based on audio quality
    yt_options = {
            "outtmpl": varPath + "/%(playlist_index)s %(title)s.%(ext)s",
            "format": "bestaudio",
            "ignoreerrors": True,
            "retries": 10,
            "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192"
                    }
                ]
        }
    # creating an instance of the YoutubeDL object
    # put options in the constructor's parameters
    with yt_dlp.YoutubeDL(yt_options) as ydl:
        ydl.download(youtube_url)


def main():
    # tell the user what is happening
    print("You are running youtube-dl_autocast...")

    # so now I have to add the text parsing part of the program
    # the file's syntax is: "URL;Genre;Artist;Album"
    with open('album-dl.txt', 'r') as f_in:
        for line in f_in:

            readline = line
            variables = readline.split(';')

            # remove the new line
            nline = variables[3]
            nline = list(nline)
            nline.pop()
            variables[3] = ''.join(nline)
            varURL = variables[0]
            varGenre = variables[1]
            varArtist = variables[2]
            varAlbum = variables[3]
            varPath = os.path.join(varGenre, varArtist, varAlbum)
            # implementation of yt_dlp, faster at downloading
            yt_dlp_download(varURL, varPath)
            # download album art
            album_cover_art_dl(varPath, varArtist, varAlbum, max_releases=10)
            # download_album_cover(varURL, varPath, varAlbum)
            mp3set(varGenre, varArtist, varAlbum)


if __name__ == "__main__":
    main()
