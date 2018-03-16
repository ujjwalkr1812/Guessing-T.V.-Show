import sys
import random
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()   #This is mandarory
        self.setGeometry(300,150,1500,800)
        self.setStyleSheet("background-color: rgb(22, 20, 61); color: rgb(255, 255, 255)")
        self.setWindowTitle('Guessing the T.V. Show')
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        #ADDING MENU BAR
        mainMenu = self.menuBar()
        mainMenu.setStyleSheet("background-color: white;")
        #Add quit option
        exitMenubar = QtGui.QAction("&Exit App",self)
        exitMenubar.setShortcut("Ctrl+Q")
        exitMenubar.setStatusTip('Leave The App')
        exitMenubar.triggered.connect(self.close_application)
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(exitMenubar)

        #Adding Rules (HELP)
        helpRules = QtGui.QAction("&Show Rules", self)
        helpRules.setShortcut("Ctrl+H")
        helpRules.setStatusTip('Game Rules')
        helpRules.triggered.connect(self.help_rules)
        fileMenu = mainMenu.addMenu('&Rules')
        fileMenu.addAction(helpRules)

        #Adding shows
        self.shows = ['the walking dead','game of thrones','the flash','grey\'s anatomy','jessica jones']
        self.shows.extend(['this is us','altered carbon','homeland','arrow','black mirror'])
        self.shows.extend(['supernatural','vikings','shameless','agents of s.h.i.e.l.d.','seven seconds'])
        self.shows.extend(['lucifer','gotham','the blacklist','riverdale','strange things'])
        self.shows.extend(['money heist','american crime story','criminal minds','peaky blinkers','the good doctor'])
        self.shows.extend(['designated survivor','friends','legends of tomorrow','the office','the big bang theory'])
        
        #Creating the basic application window
        self.statusBar()
        self.home()


    def home(self):

        #ADDING TOOL BAR
        
        fullScreen = QtGui.QAction(QtGui.QIcon('maximize.jpg'), 'Maximize', self)
        fullScreen.triggered.connect(self.maximize)
        fullScreen.setShortcut("Ctrl+Shift+M")
        self.toolBar = self.addToolBar("Enter full screen")
        self.toolBar.setStyleSheet("background-color: rgb(239, 236, 232);")
        self.toolBar.addAction(fullScreen)

        exitFullScreen = QtGui.QAction(QtGui.QIcon('minimize.png'), 'Minimize', self)
        exitFullScreen.triggered.connect(self.minimize)
        exitFullScreen.setShortcut("Ctrl+M")
        self.toolBar = self.addToolBar("Exit full screen")
        self.toolBar.setStyleSheet("background-color: rgb(239, 236, 232);")
        self.toolBar.addAction(exitFullScreen)

        replay = QtGui.QAction(QtGui.QIcon('replay.png'), 'Replay', self)
        replay.triggered.connect(self.replay_game)
        replay.setShortcut("Ctrl+R")
        self.toolBar = self.addToolBar("Replay the Game")
        self.toolBar.setStyleSheet("background-color: rgb(239, 236, 232);")
        self.toolBar.addAction(replay)

        #ADDING HEADING
        self.heading = QtGui.QLabel("GAME - GUESSING THE T.V. SHOW",self)
        self.heading.resize(700,50)
        self.heading.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.heading.setStyleSheet('font-size: 26pt; font-family: algerian; color: rgb(140, 31, 23); background-color: white')        
        self.heading.move(400,75)

        #STARTING THE GAME
        self.new_game()

        #SUBMIT BUTTON
        self.submit = QtGui.QPushButton('SUBMIT', self)
        self.submit.resize(200,50)
        self.submit.setStyleSheet('font-size: 22pt; font-family: georgia; color: rgb(15, 86, 20); background-color: rgb(45, 17, 99)')        
        self.submit.move(650,650)
        self.submit.clicked.connect(self.result)

        #REPLAY BUTTON
        self.replay = QtGui.QPushButton('REPLAY', self)
        self.replay.resize(0,0)
        self.replay.setStyleSheet('font-size: 22pt; font-family: georgia; color: rgb(15, 86, 20); background-color: rgb(45, 17, 99)')        
        self.replay.move(650,700)
        self.replay.clicked.connect(self.replay_game)

        #DISPLAYING RESULT
        self.finalResult = QtGui.QLabel(self)
        self.finalResult.resize(0,0)
        self.finalResult.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.finalResult.setStyleSheet('font-size: 30pt; font-family: georgia; color: rgb(140, 31, 23); background-color: rgb(238, 244, 66);')
        self.finalResult.move(100,150)

        #Code that is must to show the created window
        self.show()

    def close_application(self):
        print('Exitting now!!!')
        sys.exit()

    def help_rules(self):
        self.rules = "Write the correct T.V. show name to earn points (1 point for each correct answer).\n"
        self.rules += "If you want to replay click replay or third icon from the left in the toolbar."
        choice = QtGui.QMessageBox.question(self, 'Game Rules',
                                            self.rules,
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print('Now you know the rules!!!')
        else:
            print('Better if you read the rules')

    def maximize(self):
        self.setGeometry(0,35,1920,1080)

    def minimize(self, state):
        self.setGeometry(300,150,1500,800)

    def new_game(self):
        random.shuffle(self.shows)
        print(self.shows)
        self.question()
        self.answer()

    def question(self):
        self.output1 = QtGui.QLabel(self.pull_show(0),self)
        self.output1.resize(300,50)
        self.output1.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 102, 0);')        
        self.output1.move(100,150)
        self.output2 = QtGui.QLabel(self.pull_show(1),self)
        self.output2.resize(300,50)
        self.output2.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 102, 0);')        
        self.output2.move(100,250)
        self.output3 = QtGui.QLabel(self.pull_show(2),self)
        self.output3.resize(300,50)
        self.output3.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 102, 0);')        
        self.output3.move(100,350)
        self.output4 = QtGui.QLabel(self.pull_show(3),self)
        self.output4.resize(300,50)
        self.output4.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 102, 0);')        
        self.output4.move(100,450)
        self.output5 = QtGui.QLabel(self.pull_show(4),self)
        self.output5.resize(300,50)
        self.output5.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 102, 0);')        
        self.output5.move(100,550)
        self.output6 = QtGui.QLabel(self.pull_show(5),self)
        self.output6.resize(300,50)
        self.output6.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 102, 0);')        
        self.output6.move(800,150)
        self.output7 = QtGui.QLabel(self.pull_show(6),self)
        self.output7.resize(300,50)
        self.output7.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 102, 0);')        
        self.output7.move(800,250)
        self.output8 = QtGui.QLabel(self.pull_show(7),self)
        self.output8.resize(300,50)
        self.output8.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 102, 0);')        
        self.output8.move(800,350)
        self.output9 = QtGui.QLabel(self.pull_show(8),self)
        self.output9.resize(300,50)
        self.output9.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 102, 0);')        
        self.output9.move(800,450)
        self.output10 = QtGui.QLabel(self.pull_show(9),self)
        self.output10.resize(300,50)
        self.output10.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 102, 0);')        
        self.output10.move(800,550)

    def pull_show(self, x):
        self.name_array = self.shows[x].split()
        print('\n')
        for i in range(0,len(self.name_array)):
            print(self.name_array[i])
            l = list(self.name_array[i])
            random.shuffle(l)
            self.name_array[i] = ''.join(l)
        self.output_name = ' '.join(self.name_array)
        print('\n')
        return (self.output_name)

    def answer(self):
        self.input1 = QtGui.QLineEdit(self)
        self.input1.resize(300,50)
        self.input1.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 216, 0); background-color: rgb(17, 66, 112)')        
        self.input1.move(400,150)
        self.input2 = QtGui.QLineEdit(self)
        self.input2.resize(300,50)
        self.input2.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 216, 0); background-color: rgb(17, 66, 112)')        
        self.input2.move(400,250)
        self.input3 = QtGui.QLineEdit(self)
        self.input3.resize(300,50)
        self.input3.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 216, 0); background-color: rgb(17, 66, 112)')        
        self.input3.move(400,350)
        self.input4 = QtGui.QLineEdit(self)
        self.input4.resize(300,50)
        self.input4.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 216, 0); background-color: rgb(17, 66, 112)')        
        self.input4.move(400,450)
        self.input5 = QtGui.QLineEdit(self)
        self.input5.resize(300,50)
        self.input5.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 216, 0); background-color: rgb(17, 66, 112)')        
        self.input5.move(400,550)
        self.input6 = QtGui.QLineEdit(self)
        self.input6.resize(300,50)
        self.input6.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 216, 0); background-color: rgb(17, 66, 112)')        
        self.input6.move(1100,150)
        self.input7 = QtGui.QLineEdit(self)
        self.input7.resize(300,50)
        self.input7.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 216, 0); background-color: rgb(17, 66, 112)')        
        self.input7.move(1100,250)
        self.input8 = QtGui.QLineEdit(self)
        self.input8.resize(300,50)
        self.input8.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 216, 0); background-color: rgb(17, 66, 112)')        
        self.input8.move(1100,350)
        self.input9 = QtGui.QLineEdit(self)
        self.input9.resize(300,50)
        self.input9.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 216, 0); background-color: rgb(17, 66, 112)')        
        self.input9.move(1100,450)
        self.input10 = QtGui.QLineEdit(self)
        self.input10.resize(300,50)
        self.input10.setStyleSheet('font-size: 16pt; font-family: comic sans ms; color: rgb(255, 216, 0); background-color: rgb(17, 66, 112)')        
        self.input10.move(1100,550)

    def result(self):
        self.points = 0
        if(self.shows[0]==str(self.input1.text()).lower()):
            self.points+=1
        if(self.shows[1]==str(self.input2.text()).lower()):
            self.points+=1
        if(self.shows[2]==str(self.input3.text()).lower()):
            self.points+=1
        if(self.shows[3]==str(self.input4.text()).lower()):
            self.points+=1
        if(self.shows[4]==str(self.input5.text()).lower()):
            self.points+=1
        if(self.shows[5]==str(self.input6.text()).lower()):
            self.points+=1
        if(self.shows[6]==str(self.input7.text()).lower()):
            self.points+=1
        if(self.shows[7]==str(self.input8.text()).lower()):
            self.points+=1
        if(self.shows[8]==str(self.input9.text()).lower()):
            self.points+=1
        if(self.shows[9]==str(self.input10.text()).lower()):
            self.points+=1
        print(self.points)

        setoutput = "You Scored: "+str(self.points)
        self.finalResult.setText(setoutput)
        self.finalResult.resize(1300,550)
        self.replay.resize(200,50)
        
        '''#QUIT BUTTON
        self.quit = QtGui.QPushButton('QUIT', self)
        self.quit.resize(200,50)
        self.quit.setStyleSheet('font-size: 22pt; font-family: georgia; color: rgb(15, 86, 20); background-color: rgb(45, 17, 99)')        
        self.quit.move(900,650)
        self.quit.clicked.connect(self.close_application)'''
    def replay_game(self):
        random.shuffle(self.shows)
        print(self.shows)
        
        self.output1.setText(self.pull_show(0))
        self.output2.setText(self.pull_show(1))
        self.output3.setText(self.pull_show(2))
        self.output4.setText(self.pull_show(3))
        self.output5.setText(self.pull_show(4))
        self.output6.setText(self.pull_show(5))
        self.output7.setText(self.pull_show(6))
        self.output8.setText(self.pull_show(7))
        self.output9.setText(self.pull_show(8))
        self.output10.setText(self.pull_show(9))
        
        self.input1.clear()
        self.input2.clear()
        self.input3.clear()
        self.input4.clear()
        self.input5.clear()
        self.input6.clear()
        self.input7.clear()
        self.input8.clear()
        self.input9.clear()
        self.input10.clear()

        self.finalResult.clear()
        self.finalResult.resize(0,0)
        self.replay.resize(0,0)
        

#Class ends here


#Like main() of c++ Note:- not compulsary to use run() you can use any name for the function
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

#calling the function to create application
run()
