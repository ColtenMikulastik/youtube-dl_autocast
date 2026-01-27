# Luca (Colten) Mikulastik: 3/13/2022

import csv
import os
import yt_dlp
import requests
import time
import glob
from mutagen.easyid3 import EasyID3
from mutagen.id3 import APIC
from mutagen.mp3 import MP3
import mutagen.id3

# from bs4 import BeautifulSoup

class Album:
    def __init__(self, line: str):
        """ creates an album class """
        fields = line.split(';')
        nline = fields[3]
        nline = list(nline)
        nline.pop()
        fields[3] = ''.join(nline)
        self.URL = fields[0]
        self.Genre = fields[1]
        self.Artist = fields[2]
        self.Name = fields[3]
        self.Path = os.path.join(self.Genre, self.Artist, self.Name)

    def download_album(self):
        """ calls download function on album """
        yt_dlp_download(self.URL, self.Path)


def album_cover_art_dl(a: Album, max_releases):
    """ downloads an album cover for a specific album and artist """
    # re map our vairables to the class memeber variables
    var_working_path = a.Path
    var_artist = a.Artist
    var_album = a.Name
    # also set this...
    a.Album_cover_path = ""

    params = {
        "fmt": "json"
    }
    try:
        reply = requests.get("http://musicbrainz.org/ws/2/release/?query=release:\"" + var_album + "\" AND artist:\"" + var_artist + "\"", params=params)
    except:
        print("issue with musicbrainz api")
        return

    print("downloading album cover art")
    # make sure that we got a good request
    if reply.status_code == 200:
        reply_dict = reply.json()
        if reply_dict["count"] == 0:
            print("no matching albums found by MusicBrainz")
            return

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
                    a.Album_cover_path = os.path.join(var_working_path, "albumcover.jpg")
                    time.sleep(1.1)
                    img = requests.get(img_url)
                    if img.status_code == 200:
                        with open(a.Album_cover_path, "wb") as img_file:
                            img_file.write(img.content)
                            # leave loop
                            break  # could remove line to keep bunch of art
                    else:
                        print("Failure Occured when requesting Image")
                else:
                    print("Cover Art Archive api request failure")
    else:
        print("Musicbrainz api request failure")


def mp3_metadata_set(a: Album):
    """ sets the mp3 tags using id3tag in python """

    # grab all the files
    songs = glob.glob(a.Path + "/*.mp3")

    # figure out max track
    # take max value
    max_track = max(songs)
    # grabs the first letter of the fourth part of the path
    max_track = max_track.split('/')[3][0]

    album_exists = False
    # set a flag for if there is an album cover downloaded
    if a.Album_cover_path != "":
        album_exists = True

    for song in songs:
        try:
            id3 = EasyID3(song)
        except mutagen.id3.ID3NoHeaderError:
            id3 = mutagen.File(song, easy=True)
            id3.add_tags()

        title = song.split('/')[3]
        id3['title'] = title
        id3['artist'] = a.Artist
        id3['album'] = a.Name
        id3['genre'] = a.Genre
        track_num = song.split('/')[3][0]
        id3['tracknumber'] = track_num + '/' + max_track

        id3.save()
        print("metadata fixed for: " + song)
        # finish with the album art
        if album_exists:
            audio = MP3(song)
            with open(a.Album_cover_path) as albumart:
                audio.tags.add(APIC(data=albumart.read()))
            audio.save()
            print("and album art...")


def yt_dlp_download(youtube_url, varPath):
    """ calls and downloads youtube videos with yt-dlp """
    # options need to be specified based on audio quality
    yt_options = {
            "outtmpl": varPath + "/%(playlist_index)s %(title)s.%(ext)s",
            "format": "bestaudio",
            "ignoreerrors": True,
            "retries": 10,
            "extractor-args":"youtube:player_client=tv",
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
            a = Album(line)
            a.download_album()
            album_cover_art_dl(a, max_releases=10)
            mp3_metadata_set(a)
            # a.set_mp3_metadata()

def init_for_testing():
    """ test function for loading an album without calling download """
    with open('album-dl.txt', 'r') as f_in:
        for line in f_in:
            a = Album(line)
            return a


if __name__ == "__main__":
    main()
