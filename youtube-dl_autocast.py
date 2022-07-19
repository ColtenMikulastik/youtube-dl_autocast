#Luca (Colten) Mikulastik: 3/13/2022
# so we are just going to read from a text file and then past that information on to a command line basically
# 3/16/2022: now were going to fix the problems of the other youtube-dl program; mainly there is only an option
# to quit, or to fail open (just move past the problem) this isn't really greate because you can be missing
# tracks if you are trying to download music which is fucking annoying... so we want to 
import os

def cmdable(inps):
    inps_l = list(inps)
    inps_l_len = len(inps_l)

    for i in range(0,inps_l_len):
        if inps_l[i] == ' ':
            inps_l[i] = '\\ '
        elif inps_l[i] == '\'':
            inps_l[i] = '\\\''
        elif inps_l[i] == '(':
            inps_l[i] = '\('
        elif inps_l[i] == ')':
            inps_l[i] = '\)'
        elif inps_l[i] == ',':
            inps_l[i] = '\,'
        elif inps_l[i] == '?':
            inps_l[i] = '\?'
        elif inps_l[i] == '!':
            inps_l[i] = '\!'
    r_inps = ''.join(inps_l)
    return r_inps

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
                if word == "ERROR:":
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
def was_main_now_no(retry_index):
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

# so now I have to add the text parsing part of the program
# the file goes "URL;Genre;Artist;Album"
for line in open('album-dl.txt', 'r'):
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
    varPath = makedirstruc(varGenre, varArtist, varAlbum)
    
    # this is so that you can review the informtion about what the program actually downloaded search for ERROR:
    # os.system("touch errorout")
    #  this is the harder part here, to actually download the url
    os.system("youtube-dl -ix --audio-format mp3 --output " + varPath + '/\'%(playlist_index)s %(title)s.%(ext)s\' ' + varURL)
    
    # this is the old params for the checking stuff lel
    #    os.system("youtube-dl -ix --audio-format mp3 --output " + varPath + '/\'%(playlist_index)s %(title)s.%(ext)s\' ' + varURL + " &>>errorout")

    ##  check thing
    ## in order to do this we need an example of the error I keep getting (collected)
    # retry_index = search_error()
    # was_main_now_no(retry_index)

# make noise
print('\a')
