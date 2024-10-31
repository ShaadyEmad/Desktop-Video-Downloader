# Desktop Video Downloader

**Desktop Video Downloader** is a Python application built with PyQt5 for downloading videos from popular social media platforms such as YouTube, TikTok, Twitter, Snapchat, Instagram and Facebook.

## Features

- **URL Input**: Download videos by entering a video URL.
- **Directory Selection**: Choose where to save the downloaded video.
- **Progress Tracking**: See download progress in real-time.
- **Supported Platforms**: YouTube, TikTok, Twitter, Facebook, Snapchat, Instagram.

## Technologies Used

- **Python**: Core programming language.
- **PyQt5**: Used to create the graphical user interface.
- **yt-dlp**: For handling video downloads.
- **QThread**: Ensures downloads don’t freeze the UI.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ShaadyEmad/VideoDownloader.git
   cd VideoDownloader
   
2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt

## Project Structure
   ```bash
VideoDownloader/
├── main.py                  # Main Python script for running the application
├── main_window.ui           # PyQt5 .ui file for the GUI layout
├── README.md                # Project overview, installation, usage, and contributions
├── requirements.txt         # List of required packages for easy installation
├── LICENSE                  # License file (optional, depending on your preference)
└── images/
    ├── tiktok.png           # Image assets used in the application
    ├── twitter.jpg
    ├── facebook.png
    ├── youtube.png
    ├── snapchat.jpg
    └── instagram.jpg  
```

## License
This project is licensed under the MIT License


## Contribution
Contributions are welcome! If you’d like to suggest improvements, report issues, or submit a pull request, please feel free to reach out.
