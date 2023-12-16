# yt-dlp_autocast
Creator: Colten (Luca) V. Mikulastik  
The goal of this project was to make a simple automated command-line tool for Linux systems that can automatically download YouTube albums.  
I wrote this code to test my abilities as a programmer not to make piracy easier.  
This code uses the "[yt-dlp](https://github.com/yt-dlp/yt-dlp)" library.

## Syntax for download file
This program works by reading the text file "album_dl.txt" and creating directories to represent the fields in the text files such as genre, artist, album. The format is VERY syntax reliant so do not deviate from the form.
```
"youtube URL";"Genre";"Artist";"Album"
```

## Requirements
Required Bash CLI tools:
    -id3tag
Installing Python requirements is as easy as:
``` pip3 install -r requirements.txt ```
