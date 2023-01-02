Hello!  
Creator: Colten (Luca) V. Mikulastik  

The goal of this project was to make a pretty simple and automated command-line tool for Linux systems that can automatically download YouTube videos.  
I wrote this code to test my abilities as a programmer not to make piracy easier.  
This code uses the "[youtube-dl](https://youtube-dl.org/)" command line tool to run in safe mode.
It also use the "[yt-dlp](https://github.com/yt-dlp/yt-dlp)" library to run the code in fast mode.
In safe mode the program will error check and retry files that threw a network error. 
This is not true in fast mode, however the download speeds are greatly increased.
This program works by reading the text file "album_dl.txt" and creating directories to represent the fields in the text files such as genre, artist, album. The format is VERY syntax reliant so do not deviate from the form
when adding your lines to the "album_dl_.txt" file do not use spaces or special characters.
```
"youtube URL";"Genre";"Artist";"Album"
```
Now with error checking in safe mode!
Required Bash CLI tools:
    -id3tool
Required Python Libraries:
	-os
	-yt_dlp	
