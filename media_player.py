from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl
# from PyQt5 import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Media Player")
        self.setGeometry(350, 100, 700, 500)


        p =self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

        self.la_base()


        self.show()


    def la_base(self):

        #On crée l'objet du player
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)


        #On crée l'outil  videowidget dans la variable

        videowidget = QVideoWidget()


        #On crée le bouton pour importer le fichier en .MPG
        openBtn = QPushButton('selectionnez votre video')
        openBtn.clicked.connect(self.ouvrir)



        #On crée le bouton play
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)



        #On crée le slider pour
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.position_slider)



        #On crée un label qui crée un tableau pour afficher
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)


        #On crée le hbox layout qui est un emplacement horizontale
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0,0,0,0)

        #On met les outils dans les box crées
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider)



        #On crée le Vbox layout qui est un emplacement verticale
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)


        self.setLayout(vboxLayout)

        self.mediaPlayer.setVideoOutput(videowidget)


        #Affiche les changement fait au media player par exemple le bouton pause et play ou quand le slider change

        self.mediaPlayer.stateChanged.connect(self.pause_play	)
        self.mediaPlayer.positionChanged.connect(self.position)
        self.mediaPlayer.durationChanged.connect(self.duree)


    def ouvrir(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Selectionnez votre Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)


    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()


    def pause_play(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def position(self, position):
        self.slider.setValue(position)


    def duree(self, duration):
        self.slider.setRange(0, duration)


    def position_slider(self, position):
        self.mediaPlayer.setPosition(position)





# path du fichier
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())