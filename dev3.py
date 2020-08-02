from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import mysql.connector
import numpy as np
import cv2 as cv
from PIL import Image, ImageChops

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1302, 938)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(50, 650, 1201, 241))
        # self.tableView.setObjectName("tableView")
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox1.setGeometry(QtCore.QRect(50, 30, 1201, 251))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox1.setFont(font)
        self.groupBox1.setObjectName("groupBox1")
        self.LastInitialCount = QtWidgets.QLabel(self.groupBox1)
        self.LastInitialCount.setGeometry(QtCore.QRect(40, 70, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LastInitialCount.setFont(font)
        self.LastInitialCount.setObjectName("LastInitialCount")
        self.TxtLastInitialcount = QtWidgets.QPlainTextEdit(self.groupBox1)
        self.TxtLastInitialcount.setGeometry(QtCore.QRect(200, 60, 141, 41))
        self.TxtLastInitialcount.setObjectName("TxtLastInitialcount")
        self.LastDormentSeeds = QtWidgets.QLabel(self.groupBox1)
        self.LastDormentSeeds.setGeometry(QtCore.QRect(40, 130, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LastDormentSeeds.setFont(font)
        self.LastDormentSeeds.setObjectName("LastDormentSeeds")
        self.TxtLastDormentSeeds = QtWidgets.QPlainTextEdit(self.groupBox1)
        self.TxtLastDormentSeeds.setGeometry(QtCore.QRect(200, 120, 141, 41))
        self.TxtLastDormentSeeds.setObjectName("TxtLastDormentSeeds")
        self.LastGerminatedSeeds = QtWidgets.QLabel(self.groupBox1)
        self.LastGerminatedSeeds.setGeometry(QtCore.QRect(400, 130, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LastGerminatedSeeds.setFont(font)
        self.LastGerminatedSeeds.setObjectName("LastGerminatedSeeds")
        self.TxtLastGerminatedSeeds = QtWidgets.QPlainTextEdit(self.groupBox1)
        self.TxtLastGerminatedSeeds.setGeometry(QtCore.QRect(590, 120, 141, 41))
        self.TxtLastGerminatedSeeds.setObjectName("TxtLastGerminatedSeeds")
        # self.LastTimeEdit = QtWidgets.QTimeEdit(self.groupBox1)
        # self.LastTimeEdit.setGeometry(QtCore.QRect(200, 180, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        # self.LastTimeEdit.setFont(font)
        # self.LastTimeEdit.setObjectName("LastTimeEdit")
        # self.LastDateEdit = QtWidgets.QDateEdit(self.groupBox1)
        # self.LastDateEdit.setGeometry(QtCore.QRect(590, 180, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        # self.LastDateEdit.setFont(font)
        # self.LastDateEdit.setObjectName("LastDateEdit")
        self.LastTimeUpdate = QtWidgets.QLabel(self.groupBox1)
        self.LastTimeUpdate.setGeometry(QtCore.QRect(40, 190, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LastTimeUpdate.setFont(font)
        self.LastTimeUpdate.setObjectName("LastTimeUpdate")
        self.LastDateUpdate = QtWidgets.QLabel(self.groupBox1)
        self.LastDateUpdate.setGeometry(QtCore.QRect(200, 190, 170, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LastDateUpdate.setFont(font)
        self.LastDateUpdate.setObjectName("LastDateUpdate")
        self.LastUpdateImage = QtWidgets.QLabel(self.groupBox1)
        self.LastUpdateImage.setGeometry(QtCore.QRect(840, 40, 301, 181))
        self.LastUpdateImage.setText("")
        self.LastUpdateImage.setPixmap(QtGui.QPixmap("seed.jpg"))
        self.LastUpdateImage.setScaledContents(True)
        self.LastUpdateImage.setObjectName("LastUpdateImage")
        self.groupBox2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox2.setGeometry(QtCore.QRect(50, 300, 1201, 311))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox2.setFont(font)
        self.groupBox2.setObjectName("groupBox2")
        self.CurrentInitialCount = QtWidgets.QLabel(self.groupBox2)
        self.CurrentInitialCount.setGeometry(QtCore.QRect(40, 70, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CurrentInitialCount.setFont(font)
        self.CurrentInitialCount.setObjectName("CurrentInitialCount")
        self.TxtCurrentInitialcount = QtWidgets.QPlainTextEdit(self.groupBox2)
        self.TxtCurrentInitialcount.setGeometry(QtCore.QRect(200, 60, 141, 41))
        self.TxtCurrentInitialcount.setObjectName("TxtCurrentInitialcount")
        self.CurrentDormentSeeds = QtWidgets.QLabel(self.groupBox2)
        self.CurrentDormentSeeds.setGeometry(QtCore.QRect(40, 130, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CurrentDormentSeeds.setFont(font)
        self.CurrentDormentSeeds.setObjectName("CurrentDormentSeeds")
        self.TxtCurrentDormantSeeds = QtWidgets.QPlainTextEdit(self.groupBox2)
        self.TxtCurrentDormantSeeds.setGeometry(QtCore.QRect(200, 120, 141, 41))
        self.TxtCurrentDormantSeeds.setObjectName("TxtCurrentDormantSeeds")
        self.CurrentGerminatedSeeds = QtWidgets.QLabel(self.groupBox2)
        self.CurrentGerminatedSeeds.setGeometry(QtCore.QRect(400, 130, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CurrentGerminatedSeeds.setFont(font)
        self.CurrentGerminatedSeeds.setObjectName("CurrentGerminatedSeeds")
        self.TxtCurrentGerminatedSeeds = QtWidgets.QPlainTextEdit(self.groupBox2)
        self.TxtCurrentGerminatedSeeds.setGeometry(QtCore.QRect(590, 120, 141, 41))
        self.TxtCurrentGerminatedSeeds.setObjectName("TxtCurrentGerminatedSeeds")
        # self.CurrentTimeEdit = QtWidgets.QTimeEdit(self.groupBox2)
        # self.CurrentTimeEdit.setGeometry(QtCore.QRect(200, 180, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        # self.CurrentTimeEdit.setFont(font)
        # self.CurrentTimeEdit.setObjectName("CurrentTimeEdit")
        # self.CurrentDateEdit = QtWidgets.QDateEdit(self.groupBox2)
        # self.CurrentDateEdit.setGeometry(QtCore.QRect(590, 180, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        # self.CurrentDateEdit.setFont(font)
        # self.CurrentDateEdit.setObjectName("CurrentDateEdit")
        # self.CurrentTimeUpdate = QtWidgets.QLabel(self.groupBox2)
        # self.CurrentTimeUpdate.setGeometry(QtCore.QRect(40, 190, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        # self.CurrentTimeUpdate.setFont(font)
        # self.CurrentTimeUpdate.setObjectName("CurrentTimeUpdate")
        # self.CurrentDateUpdate = QtWidgets.QLabel(self.groupBox2)
        # self.CurrentDateUpdate.setGeometry(QtCore.QRect(400, 190, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        # self.CurrentDateUpdate.setFont(font)
        # self.CurrentDateUpdate.setObjectName("CurrentDateUpdate")
        self.CurrentUpdateImage = QtWidgets.QLabel(self.groupBox2)
        self.CurrentUpdateImage.setGeometry(QtCore.QRect(840, 40, 301, 181))
        self.CurrentUpdateImage.setText("")
        self.CurrentUpdateImage.setPixmap(QtGui.QPixmap("seed.jpg"))
        self.CurrentUpdateImage.setScaledContents(True)
        self.CurrentUpdateImage.setObjectName("CurrentUpdateImage")
        self.BtnGenerate = QtWidgets.QPushButton(self.groupBox2)
        self.BtnGenerate.setGeometry(QtCore.QRect(400, 250, 111, 41))
        # added event attacment #############################################################
        
        self.BtnRefresh = QtWidgets.QPushButton(self.groupBox2)
        self.BtnRefresh.setGeometry(QtCore.QRect(600, 250, 130, 41))
        self.BtnGenerate.clicked.connect(self.generateBtnClick)
        self.BtnRefresh.clicked.connect(self.refreshClick)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BtnGenerate.setFont(font)
        self.BtnGenerate.setObjectName("BtnGenerate")
        self.BtnRefresh.setFont(font)
        self.BtnRefresh.setObjectName("BtnRefresh")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1302, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.populateFields()
        self.populateTable()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Detector"))
        self.groupBox1.setTitle(_translate("MainWindow", "Last time"))
        self.LastInitialCount.setText(_translate("MainWindow", "Initial count"))
        self.LastDormentSeeds.setText(_translate("MainWindow", "Dorment seeds "))
        self.LastGerminatedSeeds.setText(_translate("MainWindow", "Germinated seeds"))
        self.LastTimeUpdate.setText(_translate("MainWindow", "Date"))
        # self.LastDateUpdate.setText(_translate("MainWindow", "Last date"))

        
        self.groupBox2.setTitle(_translate("MainWindow", "Current time"))
        self.CurrentInitialCount.setText(_translate("MainWindow", "Initial count"))
        self.CurrentDormentSeeds.setText(_translate("MainWindow", "Germinated seeds"))
        self.CurrentGerminatedSeeds.setText(_translate("MainWindow", "Dorment seeds"))
        # self.CurrentTimeUpdate.setText(_translate("MainWindow", "Current time"))
        # self.CurrentDateUpdate.setText(_translate("MainWindow", "Current date"))
        self.BtnGenerate.setText(_translate("MainWindow", "Generate"))
        self.BtnRefresh.setText(_translate("MainWindow", "Refresh"))


    def generateBtnClick(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        datas = self.updateData()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="seeddb"
        )
        
        mycursor = mydb.cursor()

        # INSERT QUERY
        timestamp = datetime.datetime.now()
        first_count = datas[0]
        second_count = datas[1]
        dormant = abs(int(first_count) - int(second_count))
        
        sql = "INSERT INTO `germination` (timestamp, first_count, second_count, dormant) VALUES (%s, %s, %s, %s)"
        val = (timestamp, first_count, second_count, dormant)
        # print("value",second_count)

        mycursor.execute(sql, val)
        mydb.commit()

        # self.TxtLastInitialcount.setPlainText(str(initData[0][2]))
        self.TxtCurrentInitialcount.setPlainText(str(first_count))
        self.TxtCurrentDormantSeeds.setPlainText(str(second_count))
        self.TxtCurrentGerminatedSeeds.setPlainText(str(dormant))
        # self.LastDateUpdate.setText(_translate("MainWindow", str(initData[0][1])))



        # print(datas[0])

    
    def populateFields(self):
        
        _translate = QtCore.QCoreApplication.translate

        initData = []
        
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="seeddb"
        )
        
        mycursor = mydb.cursor()

        sql = "SELECT * FROM `germination` ORDER BY `id` DESC LIMIT 1;"

        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        
        if myresult:
            for x in myresult:
                initData.append(x)

            self.TxtLastInitialcount.setPlainText(str(initData[0][2]))
            self.TxtLastGerminatedSeeds.setPlainText(str(initData[0][3]))
            self.TxtLastDormentSeeds.setPlainText(str(initData[0][4]))
            self.LastDateUpdate.setText(_translate("MainWindow", str(initData[0][1])))


    def updateData(self):

        # image = cv.imread("C:/Users/Alpha_D/PycharmProjects/untitled/img/MIXS2.jpg", 1)
        image = cv.imread("captured.jpg", 1)

        imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(imgray, 220, 255, cv.THRESH_BINARY_INV)
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        firstCount = str(len(contours))
        # print(firstCount)

        # cv.imwrite('out.jpg', thresh)

        image2 = Image.open("C:/Users/Alpha_D/PycharmProjects/untitled/img/MIXS2.jpg")
        image1 = Image.open("captured.jpg")

        different_find = ImageChops.difference(image2,image1)
        if different_find.getbbox():
            different_find.save("difference.png")
            ##########################################################
            image3 = cv.imread("C:/Users/Alpha_D/PycharmProjects/untitled/img/difference.png")
            imgray = cv.cvtColor(image3, cv.COLOR_BGR2GRAY)
            ret, thresh = cv.threshold(imgray, 35, 255, cv.THRESH_BINARY)
            kernel = np.ones((5,5),np.uint8)
            dilation = cv.dilate(thresh,kernel,iterations = 1)

            contours, hierarchy = cv.findContours(dilation,cv.RETR_CCOMP,cv.CHAIN_APPROX_NONE)

            thresh = cv.cvtColor(thresh, cv.COLOR_GRAY2BGR)

            secondCount = str(len(contours))
            # print(secondCount)

            return firstCount, secondCount


        return firstCount


    def refreshClick(self):
        self.populateFields()
        self.populateTable()
        fafa()


    def populateTable(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="seeddb"
        )
        
        mycursor = mydb.cursor()

        sql = "SELECT * FROM `germination` ORDER BY `id`;"

        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        datas = [
            ['ID', 'Time', 'Initial', 'Germinated', 'Dormant'],
        ]

        for x in myresult:
            datas.append(x)

        self.table = QtWidgets.QTableView()

        # datas = [
        #   [4, 9, 2],
        #   [1, 0, 0],
        #   [3, 5, 0],
        #   [3, 3, 2],
        #   [7, 8, 9],
        # ]

        self.model = TableModel(datas)
        self.tableView.setModel(self.model)


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        # if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
        return str(self._data[index.row()][index.column()])

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])


cap = cv.VideoCapture(0)

def fafa():
    while True:
        _, img = cap.read()
        cv.imshow('Incubator Feed', img)

        if cv.waitKey(1) & 0xff == ord('q'):
            cv.imwrite('captured.jpg', img)
            break


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    fafa()
    sys.exit(app.exec_())
    
    #this is not work without camera
