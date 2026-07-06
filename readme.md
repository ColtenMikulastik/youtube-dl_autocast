# yt-dlp_autocast
Creator: Colten V. Mikulastik  
This project is a python/flask based webapp which downloads albums from a given playlist url from youtube, *youtube music also works*.
This code uses the "[yt-dlp](https://github.com/yt-dlp/yt-dlp)" library.

## Features:
- Download entire YouTube playlists or albums
- applies metadata to downloaded music
- downloads album cover
- Supports both YouTube and YouTube Music
- Web-based interface for easy use
- Automatic album organization
- Docker containerization for easy deployment

## Usage:
This project is started via a downloading the container from docker hub [coltenmikulastik/youtube_dl_autocast](https://hub.docker.com/repository/docker/coltenmikulastik/youtube_dl_autocast).
You can run the container using the given docker-compose in this repo, main configuration change might be where you want the albums to be downloaded to.

### Docker Run:
```bash
docker run -d \
  --name yt-dlp_autocast \
  -p 5000:5000 \
  -v /path/to/download/directory:/app/downloads \
  coltenmikulastik/youtube_dl_autocast
```

### Local Setup:
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Access the web interface at `http://localhost:5000`

### Project Structure:
```
.
├── app.py              # Main Flask application
├── docker-compose.yaml  # Docker composition
├── dockerfile        # Docker image build configuration
├── readme.md         # This file
├── requirements.txt      # Python dependencies
├── templates/      # HTML templates for web interface
└── Music/            # Default download directory
```

## Configuration:
The application uses the following environment variables:
- `DOWNLOAD_DIR`: Directory where downloads are saved (default: `/app/downloads`)
- `PORT`: Port number for the web server (default: 5000)

## How to Use:
1. Start the container using docker-compose or docker run
2. Navigate to `http://localhost:5000` in your browser
3. Enter a YouTube playlist URL
4. Click "Download" and wait for the process to complete

## Requirements:
- Python 3.7+
- yt-dlp library
- Flask web framework

