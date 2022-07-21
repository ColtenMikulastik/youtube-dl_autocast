Hello!  
Creator: Colten (Luca) V. Mikulastik  

The goal of this project was to make a pretty simple and automated command-line tool for Linux systems that can automatically download YouTube videos.  
I wrote this code to test my abilities as a programmer not to make piracy easier.  
This code uses the "[youtube-dl](https://youtube-dl.org/)" command line tool as the main dependancy, and the python os library to control operating system actions.  
This program works by reading the text file "album_dl.txt" and creating directories to represent the fields in the text files such as genre, artist, album. The format is VERY syntax reliant so do not deviate from the form
```
youtube URL;Genre;Artist;Album
```
Once the program is done, there might be songs that threw an error, if an error has been thrown on a song that song will be skipped, and I have yet to make a workaround for this problem.

