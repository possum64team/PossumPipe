print("Baaah")
#!/usr/bin/env python3
import mpv
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Test(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.container = QWidget(self)
        self.setCentralWidget(self.container)
        self.container.setAttribute(Qt.WA_DontCreateNativeAncestors)
        self.container.setAttribute(Qt.WA_NativeWindow)
        player = mpv.MPV(wid=str(int(self.container.winId())), vo='gpu')
        player.play('https://youtu.be/ej9N6cJovwQ')

app = QApplication(sys.argv)

# This is necessary since PyQT stomps over the locale settings needed by libmpv.
# This needs to happen after importing PyQT before creating the first mpv.MPV instance.
import locale
locale.setlocale(locale.LC_NUMERIC, 'C')
win = Test()
win.show()
sys.exit(app.exec_())

"""
import youtube_dl

class MyLogger(object):
	def debug(self, msg):
		pass
	def warning(self, msg):
		pass
	def error(self, msg):
		print(msg)

def my_hook(d):
	if d['status'] == 'finished':
		print('Done downloading, now converting ...')

ydl_opts = {
	'format': 'best',
#	'postprocessors': [{
#		'key': 'FFmpegExtractAudio',
#		'preferredcodec': 'mp3',
#		'preferredquality': '192'
#	}],
	'logger': MyLogger(),
	'progress_hooks': [my_hook]
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download(['https://youtu.be/ej9N6cJovwQ'])
"""
