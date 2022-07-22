import yt_dlp

def yt_dlp_download(youtube_url):
    # options need to be specified
    yt_options = {
            "outtmpl" : "%(playlist_index)s %(title)s.%(ext)s",
            "format" : "bestaudio",
            "audio_format" : "mp3"
        }
    # creating an instance of the YoutubeDL object
    # put options in the constructor's parameters
    yt_downloader = yt_dlp.YoutubeDL(yt_options)
    yt_downloader.download(youtube_url)
    


def main():
    test_url = "https://www.youtube.com/playlist?list=PLVciB1OCnYiUgKLUU5hOtCk-yCdM4x2x_"
    yt_dlp_download(test_url)
    print("done")

main()
