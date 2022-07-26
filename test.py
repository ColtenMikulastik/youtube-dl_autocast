import yt_dlp

def yt_dlp_download(youtube_url):
    # options need to be specified
    yt_options = {
            "outtmpl": "testdir/%(playlist_index)s %(title)s.%(ext)s",
            "format": "bestaudio/best",
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
    test_url = "https://www.youtube.com/playlist?list=PLv0jjxv5Ng1FNkrmKzUIdxYNqiE4W3-J5"
    yt_dlp_download(test_url)
    print("done")

main()
