# Luca (Colten) Mikulastik: 3/13/2022

import csv
import os
import yt_dlp
# import requests
# from bs4 import BeautifulSoup


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


# def download_album_cover(var_url, var_path, var_album):
#     """downloads thumbnail image for a youtube music playlist non-functional"""
#     # set the headers that I think that youtube music wants
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#
#     # get the html page
#     page = requests.get(var_url, headers=headers)
#     soup = BeautifulSoup(page.content, 'html.parser')
#
#     # turn the soup type into a string, so I can parse it for information
#     stringsoup = str(soup)
#
#     # look for keyword "thumbnails"
#     stringsoup = stringsoup[stringsoup.find("thumbnails"):]
#
#     # find the link after the thumbnails keyword
#     stringsoup = stringsoup[stringsoup.find("https"):]
#
#     # remove the uninportant information from the end
#     sub_stringsoup = stringsoup[: stringsoup.find("\\x")]
#
#     # replace the strange \\/ characters that seem to be used in the html page
#     sub_stringsoup = sub_stringsoup.replace("\\/", "/")
#
#     # go to link's resource and request it
#     image_req = requests.get(sub_stringsoup)
#
#     # create the path that I want the image to be saved into
#     path_for_img = var_path + "/ablum_cover.jpg"
#
#     # then write the bites of the requested image into the file
#     with open(path_for_img, "wb") as file:
#         file.write(image_req.content)


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
            # download_album_cover(varURL, varPath, varAlbum)
            mp3set(varGenre, varArtist, varAlbum)


if __name__ == "__main__":
    main()
