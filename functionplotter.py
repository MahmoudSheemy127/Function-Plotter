from PyQt5.QtWidgets import QApplication, QMainWindow, QLayout, QLabel,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QWidget,QMessageBox
from PyQt5.QtGui import QIntValidator
from pyqtgraph import plot,PlotWidget
from ArithemticStack import arith
import sys


#Class for the plotter widget
class Plotter(PlotWidget):
    def __init__(self):
        super(Plotter,self).__init__()
        self.xAxis = []
        self.yAxis = []
        self.graph = self.plot()
    #plot function
    def plotFunction(self):
        self.graph.clear()
        self.graph = self.plot(self.xAxis,self.yAxis,pen = 'b')
        
    


#class for the main window of the application
class window(QMainWindow):
    def __init__(self):
        super(window,self).__init__()
        #define widgets that will be used in GUI , such as labels, buttons and text inputs
        self.Xmin = QLineEdit()
        self.Xmax = QLineEdit()
        self.functionText = QLineEdit()
        self.submitBtn = QPushButton("Plot")
        self.plotter = Plotter()
        self.uiInit()
    #function to build the UI
    def uiInit(self):
        self.setWindowTitle("Function Plotter")
        vLayout1 = QVBoxLayout()

        title = QLabel()
        title.setText("Function Plotter")

        self.plotter.setLabel('left','y')
        self.plotter.setLabel('bottom','x')

        hLayout1 = QHBoxLayout()
        function_text_label = QLabel()
        function_text_label.setText("F(x)= ")
        hLayout1.addWidget(function_text_label)
        hLayout1.addWidget(self.functionText)

        hlayout2 = QHBoxLayout()
        vLayout2 = QVBoxLayout()
        vLayout3 = QVBoxLayout()

        XminLabel = QLabel()
        XminLabel.setText("X_min")

        XmaxLabel = QLabel()
        XmaxLabel.setText("X_max")

        self.Xmin.setValidator(QIntValidator())
        self.Xmax.setValidator(QIntValidator())

        self.Xmin.setText("0")
        self.Xmax.setText("100")

        vLayout2.addWidget(XminLabel)
        vLayout2.addWidget(self.Xmin)

        vLayout3.addWidget(XmaxLabel)
        vLayout3.addWidget(self.Xmax)

        hlayout2.addLayout(vLayout2)
        hlayout2.addLayout(vLayout3)

        vLayout1.addWidget(title)
        vLayout1.addWidget(self.plotter)

        vLayout1.addLayout(hLayout1)
        vLayout1.addLayout(hlayout2)

        vLayout1.addWidget(self.submitBtn)
        widget = QWidget()
        widget.setLayout(vLayout1)
        self.setCentralWidget(widget)
        
        #Connect the push button click event with a function 
        self.submitBtn.clicked.connect(self.executeFunction)

    #function to execute the F(X) input from user
    def executeFunction(self):
        
        #validation error : function input is empty
        if(not self.functionText.text()):
            alert = QMessageBox()
            alert.setText("Error: empty function statement")
            alert.exec()
        else:
            #take x-axis boundaries from Xmin and Xmax input fields from User
            xMin = int(self.Xmin.text())
            xMax = int(self.Xmax.text())

            #clear old x-axis vector
            self.plotter.xAxis = []
            #create new x-axis vector
            for i in range(xMin,xMax):
                self.plotter.xAxis.append(i)
            #execute F(x) using function arith() to create vector y[] for y-axis 
            y = arith(self.functionText.text(),self.plotter.xAxis)
            
            #validation error: syntax error conditions like Double signs, variables other than x
            if(not isinstance(y,list)):
                print("Hey")
                alert = QMessageBox()
                alert.setText("Error: "+ str(y))
                alert.exec()
            else:
                #clear old y-axis
                self.plotter.yAxis = []
                #set y-axis vector
                self.plotter.yAxis = y
                #plot x-axis vector with y-axis vector
                self.plotter.plotFunction()
        


def main():
    app = QApplication(sys.argv)
    MyWindow = window()
    MyWindow.show()
    app.exec_()

main()