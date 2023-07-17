import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLayout, QLabel,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QWidget,QMessageBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from calculate import execute


ERROR = -1


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        #define widgets that will be used in GUI , such as labels, buttons and text inputs
        #init main widgets to be entered in the application
        self.Xmin = QLineEdit()
        self.Xmax = QLineEdit()
        self.functionText = QLineEdit()
        self.submitBtn = QPushButton("Plot")
        self.fig = plt.figure()
        self.plotter = self.fig.add_subplot(111) 
        self.alert = QMessageBox()
        self.uiInit()
    #function to build the UI
    def uiInit(self):
        self.setWindowTitle("Function Plotter")
        vLayout1 = QVBoxLayout()

        #build title label
        title = QLabel()
        title.setText("Function Plotter")

        #build plot figure widget
        self.canvas = FigureCanvas(self.fig)

        #build statement input text field
        function_text_label = QLabel()
        function_text_label.setText("F(x)= ")

        #group some widgets together
        hLayout1 = QHBoxLayout()
        hLayout1.addWidget(function_text_label)
        hLayout1.addWidget(self.functionText)

        hlayout2 = QHBoxLayout()
        vLayout2 = QVBoxLayout()
        vLayout3 = QVBoxLayout()

        #build min input text field
        XminLabel = QLabel()
        XminLabel.setText("X_min")

        #build max input text field
        XmaxLabel = QLabel()
        XmaxLabel.setText("X_max")
        #set default values
        self.Xmin.setText("0")
        self.Xmax.setText("100")

        #group some labels
        vLayout2.addWidget(XminLabel)
        vLayout2.addWidget(self.Xmin)

        vLayout3.addWidget(XmaxLabel)
        vLayout3.addWidget(self.Xmax)

        hlayout2.addLayout(vLayout2)
        hlayout2.addLayout(vLayout3)

        vLayout1.addWidget(title)
        vLayout1.addWidget(self.canvas)

        vLayout1.addLayout(hLayout1)
        vLayout1.addLayout(hlayout2)

        vLayout1.addWidget(self.submitBtn)
        widget = QWidget()
        widget.setLayout(vLayout1)
        self.setCentralWidget(widget)
        
        # Connect the push button click event with a function 
        self.submitBtn.clicked.connect(self.executeFunction)

    def executeFunction(self):
        #validation check whether function input is empty
        if(not self.functionText.text()):
            self.alert.setText("Error: empty function statement")
            self.alert.exec()
            return

        #validation check for xMin and xMax numerical value
        try:
            #take x-axis boundaries from Xmin and Xmax input fields from User
            xMin = int(self.Xmin.text())
            xMax = int(self.Xmax.text())
            x_axis = [i for i in range(xMin,xMax)]
            result = execute(x_axis,self.functionText.text())
        except:
            #either xMin or xMax label contains a non-numerical value
            self.alert.setText("Error: X-axis range should be numerica value")
            self.alert.exec()
            return

        #validation check whether function statement is invalid
        if result == ERROR:
            #function statement is invalid
            self.alert.setText("Error: Invalid Statement")
            self.alert.exec()
            return

        #validation check whether result contain complex number or there exists a logical error during execution
        try:
            #Result is valid to plot
            self.plotter.cla()
            self.plotter.plot(x_axis,result)            
            self.canvas.draw()
        except:
            #Result is invalid to plot
            self.alert.setText("Error: can't plot please check function")
            self.alert.exec()
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

