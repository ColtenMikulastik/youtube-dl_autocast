# Luca (Colten) Mikulastik: 3/13/2022
# so we are just going to read from a text file and then past that information on to a command line basically
# 3/16/2022: now were going to fix the problems of the other youtube-dl program;
# !!!!! BUG: in dir creation, creates dir correct dir, then creates dir with '\'
# chars in spaces and stores items there

import os
import yt_dlp
import requests
from bs4 import BeautifulSoup


def download_album_cover(var_url, var_path, var_album):
    # set the headers that I think that youtube music wants
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    
    page = requests.get(var_url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    stringsoup = str(soup)
    
    stringsoup = stringsoup[stringsoup.find("thumbnails"):]
    
    stringsoup = stringsoup[stringsoup.find("https"):]
    
    sub_stringsoup = stringsoup[: stringsoup.find("\\x")]
    
    sub_stringsoup = sub_stringsoup.replace("\\/","/")
    print(sub_stringsoup)
    
    image_req = requests.get(sub_stringsoup)
    
    path_for_img = var_path + var_album + "ablum_cover.jpg"

    with open(path_for_img, "wb") as file:
        file.write(image_req.content)


def yt_dlp_download(youtube_url, varPath):
    # options need to be specified based on audio quality
    yt_options = {
            "outtmpl" : varPath + "/%(playlist_index)s %(title)s.%(ext)s",
            "format" : "bestaudio",
            "ignoreerrors" : True,
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
    


def makedirstruc(varGenre, varArtist, varAlbum):
    #  make files genre/artist/album, if it already exist than i think it will skip but idk
    #first make them cmdable
    varGenre = cmdable(varGenre)
    varArtist = cmdable(varArtist)
    varAlbum = cmdable(varAlbum)
    
    path_m = os.path.join(varGenre, varArtist, varAlbum)
    # create file system
    os.system("mkdir -p " + path_m)
    return path_m


def search_error():
    #this would litterally work amazing with a fifo queue, no it doesn't thanks tho list pls!
    q = []
    error_nubns = []
    # so I think I will open the file, read the information into a buffer for three lines
    with open('errorout') as file:
        is_error = False #  this will likely need to be moved
        # look for "ERROR:"
        for line in file:
            l_line = line.split(' ')
            for word in l_line:
                # so here I am also going to check the type of error message
                if word == "ERROR:" and l_line[-1] == "Forbidden\n":
                    is_error = True
                    #look for the number connected to the error
                    num_line = q[1]
                    l_num_line = num_line.split(' ')
                    index_of_num = l_num_line.index('video') + 1
                    error_nubns.append(int(l_num_line[index_of_num]))
            # put line in to q for later use

            if len(q) < 3:
                q.append(line)
            else:
                q.append(line)
                q.pop(0)
    return error_nubns


# I'm goning to make this thing that was in main, now into a function so that I can comment it out without loosing the code
def retry_func(retry_index):
        if retry_index != None: 
            # because python is stupid
            # make all the int into strings
            form_retry_index = []
            for i in retry_index:
                form_retry_index.append(str(i))
    
            # join together with a coma inbetween
            nums = ','.join(form_retry_index)
            #put those nums into the command to try and download them again 
            os.system("youtube-dl -ix --audio-format mp3 --playlist-items " + nums + " --output " + varPath + "/\'%(playlist_index)s %(title)s.%(ext)s\' " + varURL)
            # remove errorout
            os.system("rm errorout")
        else:
            pass

def call_bash_script():
    # use the os lib to run the bash script
    os.system("chmod a+x mp3set.sh")
    # run the bash tool that I wrote
    os.system("./mp3set.sh")
    # function should change the metadata on all the files in genre directorys


def main():
    # I'm gonna add an option so that the user gets to choose what why to run program
    print("You are running youtube-dl_autocast...")
    print("would you like to run in fast or safe mode?")
    print("quick mode = q")
    print("safe mode = s")
    mode_input = input("...:")
    # will default run in fast mode
    if mode_input == 's':
        use_yt_dlp = False
    else:
        use_yt_dlp = True

    # so now I have to add the text parsing part of the program
    # the file goes "URL;Genre;Artist;Album"
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
            if use_yt_dlp:
                yt_dlp_download(varURL, varPath)
            else:
        
                # this is so that you can review the informtion about what the program actually downloaded search for ERROR:
                os.system("touch errorout")
                #  this is the harder part here, to actually download the url
            
                # old functional downloader cmd
                # os.system("youtube-dl -ix --audio-format mp3 --output " + varPath + '/\'%(playlist_index)s %(title)s.%(ext)s\' ' + varURL)
                # this is the old params for the checking stuff lel
                os.system("youtube-dl -ix --audio-format mp3 --output " + varPath + '/\'%(playlist_index)s %(title)s.%(ext)s\' ' + varURL + " > errorout 2>&1")
            
                # this is were I'm going to add a new function
                ##  check thing
                ## in order to do this we need an example of the error I keep getting (collected)
                retry_index = search_error()
                # before we actually try to fix, we need to make sure this function working properly
                retry_func(retry_index)
                print(retry_index)
    
    # make noise
    # call bash script at the end of this script
    call_bash_script()
    print('\a')


if __name__ == "__main__":
    main()
