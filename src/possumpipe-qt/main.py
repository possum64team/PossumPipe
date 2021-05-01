# This Python file uses the following encoding: utf-8
import sys
import os
import glob
from pathlib import Path

from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        uic.loadUi("mainwindow.ui", self)
        self.show()
        self.DLButton.clicked.connect(self.switchDownloadTab)
        self.SubsButton.clicked.connect(self.switchSubTab)
        self.PlaylistsButton.clicked.connect(self.switchPlaylistTab)
        self.loadDLTab()
        self.SearchBox.textChanged.connect(self.searchCurrentTab)
    
    def switchDownloadTab(self):
        self.switchTabs(0)

    def switchSubTab(self):
        self.switchTabs(1)

    def switchPlaylistTab(self):
        self.switchTabs(2)

    def switchTabs(self, tabNumber):
        self.stackedWidget.setCurrentIndex(tabNumber)
    
    def searchCurrentTab(self, text):
        for i in range(self.DownloadList.count()):
            if text == "":
                self.DownloadList.item(i).setHidden(False)
                continue
            elif text in self.DownloadList.item(i).text().lower():
                self.DownloadList.item(i).setHidden(False)
            else:
                self.DownloadList.item(i).setHidden(True)
        QApplication.processEvents()
    
    def loadDLTab(self):
        DOWNLOAD_PATH = str(Path.home()) + "/Videos/possumpipe/"
        os.makedirs(Path(DOWNLOAD_PATH + "imagecache"), exist_ok = True)
        print("Scanning path ")
        types = ('*.mkv', '*.mp4', '*.webm', '*.y4m', '*.avi')
        files_grabbed = []
        for files in types:
            files_grabbed.extend(glob.glob(DOWNLOAD_PATH + "/" + files))
        print("Found movies: ")
        print(files_grabbed)

        for fil in files_grabbed:
            image = "confused-possum.webp"
            if os.path.isfile(DOWNLOAD_PATH + "imagecache/" + os.path.split(fil)[1] + ".webp"):
                image = DOWNLOAD_PATH + "imagecache/" + os.path.split(fil)[1] + ".webp"
            lab = QtWidgets.QListWidgetItem(QtGui.QIcon(image), os.path.split(fil)[1])
            self.DownloadList.addItem(lab)
            
        QApplication.processEvents()
            


if __name__ == "__main__":
    app = QApplication([])
    widget = window()
    sys.exit(app.exec_())
