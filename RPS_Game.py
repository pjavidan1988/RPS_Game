import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
from random import randint

computerScore = 0
playerScore = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors Game")
        self.setMinimumSize(655, 408)
        self.setMaximumSize(655, 408)
        self.UI_DESIGN()

    def UI_DESIGN(self):
        #######################################start button#####################################
        start = QPushButton('Start', self)
        start.setGeometry(200, 240, 121, 51)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        start.setFont(font)
        start.setObjectName("start")
        start.clicked.connect(self.start)
        #######################################stop button######################################
        stop = QPushButton('Stop', self)
        stop.setGeometry(340, 240, 111, 51)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        stop.setFont(font)
        stop.setObjectName("stop")
        stop.clicked.connect(self.stop)
        ######################################computer score label#######################################
        self.computer_score = QLabel('computer score : ', self)
        self.computer_score.setGeometry(100, 30, 181, 31)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.computer_score.setFont(font)
        self.computer_score.setObjectName("computer_score")
        ######################################player score###################################################
        self.player_score = QLabel('player score : ', self)
        self.player_score.setGeometry(390, 30, 181, 31)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.player_score.setFont(font)
        self.player_score.setObjectName("player_score")
        #######################################image computer#############################################
        self.imageComputer = QLabel(self)
        self.imageComputer.setGeometry(130, 90, 101, 101)
        self.imageComputer.setText("")
        self.imageComputer.setPixmap(QPixmap("images/rock_com.png"))
        self.imageComputer.setScaledContents(True)
        self.imageComputer.setObjectName("imagecomputer")
        #######################################image game###################################################
        self.imagegame = QLabel(self)
        self.imagegame.setGeometry(270, 90, 111, 101)
        self.imagegame.setText("")
        self.imagegame.setPixmap(QPixmap("images/game.png"))
        self.imagegame.setScaledContents(True)
        self.imagegame.setObjectName("imagegame")
        #########################################image player################################################
        self.imagePlayer = QLabel(self)
        self.imagePlayer.setGeometry(420, 90, 101, 101)
        self.imagePlayer.setText("")
        self.imagePlayer.setPixmap(QPixmap("images/rock_player.png"))
        self.imagePlayer.setScaledContents(True)
        self.imagePlayer.setObjectName("label_3")
        ########################################Timer###############################################
        self.timer = QTimer(self)
        self.timer.setInterval(80)
        self.timer.timeout.connect(self.playGame)

        self.show()

    ###########################################Start function###################################################
    def start(self):
        self.timer.start()

        ############################################Start Game function############################################

    def playGame(self):
        self.rndcom = randint(1, 3)
        self.rndplayer = randint(1, 3)

        if self.rndcom == 1:
            self.imageComputer.setPixmap(QPixmap("images/rock_com.png"))
        elif self.rndcom == 2:
            self.imageComputer.setPixmap(QPixmap("images/paper_com.png"))
        else:
            self.imageComputer.setPixmap(QPixmap("images/scissors_com.png"))

        if self.rndplayer == 1:
            self.imagePlayer.setPixmap(QPixmap("images/rock_player.png"))

        elif self.rndplayer == 2:
            self.imagePlayer.setPixmap(QPixmap("images/paper_player.png"))
        else:
            self.imagePlayer.setPixmap(QPixmap("images/scissors_player.png"))

    def stop(self):
        global computerScore
        global playerScore
        self.timer.stop()

        if self.rndcom == 1 and self.rndplayer == 1:
            Messbox = QMessageBox.information(self, 'Result', 'Draw in the match')

        elif self.rndcom == 1 and self.rndplayer == 2:
            Messbox = QMessageBox.information(self, 'Information', 'Player win')
            playerScore += 1
            self.player_score.setText(f'player score: {playerScore}')

        elif self.rndcom == 1 and self.rndplayer == 3:
            Messbox = QMessageBox.information(self, 'Information', 'Computer win')
            computerScore += 1
            self.computer_score.setText(f'computer score: {computerScore}')

        elif self.rndcom == 2 and self.rndplayer == 1:
            Messbox = QMessageBox.information(self, 'Information', 'Computer win')
            computerScore += 1
            self.computer_score.setText(f'computer score: {computerScore}')

        elif self.rndcom == 2 and self.rndplayer == 2:
            Messbox = QMessageBox.information(self, 'Information', 'Draw in the match')

        elif self.rndcom == 2 and self.rndplayer == 3:
            Messbox = QMessageBox.information(self, 'Information', 'Player win')
            playerScore += 1
            self.player_score.setText(f'player score: {playerScore}')

        elif self.rndcom == 3 and self.rndplayer == 1:
            Messbox = QMessageBox.information(self, 'Information', 'Player win')
            playerScore += 1
            self.player_score.setText(f'player score: {playerScore}')

        elif self.rndcom == 3 and self.rndplayer == 2:
            Messbox = QMessageBox.information(self, 'Information', 'Computer win')
            computerScore += 1
            self.computer_score.setText(f'computer score: {computerScore}')

        elif self.rndcom == 3 and self.rndplayer == 3:
            Messbox = QMessageBox.information(self, 'Information', 'Draw in the match')

        if computerScore == 3 or playerScore == 3:
            Messbox = QMessageBox.information(self, 'Result', 'Game over')

            if computerScore > playerScore:
                mbox = QMessageBox.information(self, 'Result', "Computer win game")

            else:
                mbox = QMessageBox.information(self, 'Result', "Player win game")

            sys.exit()


def main():
    App = QApplication(sys.argv)
    window = Window()
    window.start()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
