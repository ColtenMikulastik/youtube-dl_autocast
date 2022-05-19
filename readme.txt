Hello!
Creator: Colten (Luca) V. Mikulastik
The goal of this project was to make a pretty simple and automated command-line tool for linux systems that can automatically download youtube videos.
I wrote this code to test my abilities as a programer not to make piracy easier. 
This code uses the "youtube-dl" command line tool as the main dependancy, and the os library to control operating system actions.
This program works by reading the text file "album_dl.txt" and creating directories to represent the feilds in the text files such as genre, artist, album. The format is VERY syntax reliant so do not deviate from the forma (youtube URL;Genre;Artist;Album). once the program is done, there might be songs that threw an error, if an error has been trown on a song that song will be skiped, and I have yet to make a workaround for this problem.

