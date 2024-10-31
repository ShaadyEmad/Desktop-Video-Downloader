import sys
import os
import yt_dlp
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication


# Worker class for handling download in a separate thread
class DownloadWorker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)

    def __init__(self, url, location):
        super().__init__()
        self.url = url
        self.location = location

    def run(self):
        try:
            ydl_opts = {
                'outtmpl': os.path.join(self.location, '%(title)s.%(ext)s'),
                'progress_hooks': [self.hook],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
            self.finished.emit("Download completed!")
        except Exception as e:
            self.finished.emit(f"Download failed: {str(e)}")

    def hook(self, d):
        print(f"dddddd:{d}")
        if d['status'] == 'downloading':
            if d.get('total_bytes_estimate') or d.get('total_bytes'):
                downloaded = d.get('downloaded_bytes', 0)
                total = d.get('total_bytes_estimate') or d.get('total_bytes')
                progress = int(downloaded / total * 100)
                self.progress.emit(progress)
        elif d['status'] == 'finished':
            self.progress.emit(100)

# Main Window class
class DownloaderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("downloader.ui", self)

        # Connect UI elements to backend functions
        self.pushButton.clicked.connect(self.start_download)
        self.pushButton_2.clicked.connect(self.select_location)
        self.progressBar.setValue(0)
        self.download_location = ""

    def select_location(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Download Directory")
        if directory:
            self.download_location = directory

    def start_download(self):
        url = self.lineEdit.text().strip()
        if not url or not self.download_location:
            QMessageBox.warning(self, "Error", "Please provide both a valid URL and download location.")
            return
        if not self.is_supported_link(url):
            QMessageBox.warning(self, "Error", "The URL provided is not supported.")
            return

        self.pushButton.setEnabled(False)  # Disable download button during download
        self.statusbar.showMessage("Starting download...")
        self.progressBar.setValue(0)

        # Start the worker thread for downloading
        self.worker = DownloadWorker(url, self.download_location)
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.download_finished)
        self.worker.start()

    def is_supported_link(self, url):
        supported_sites = ["youtube.com", "youtu.be", "facebook.com", "twitter.com", "tiktok.com", "x.com", "snapchat.com"]
        return any(site in url for site in supported_sites)

    def update_progress(self, value):
        self.progressBar.setValue(value)
        QCoreApplication.processEvents()  # Process events to update UI

    def download_finished(self, message):
        self.statusbar.showMessage(message)
        self.pushButton.setEnabled(True)  # Re-enable download button after download completes
        QMessageBox.information(self, "Download", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    downloader = DownloaderApp()
    downloader.show()
    sys.exit(app.exec_())
