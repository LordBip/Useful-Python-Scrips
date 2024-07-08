'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QFileDialog, QTableWidget, QTableWidgetItem, QInputDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import pandas as pd
from io import StringIO

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSV Previewer")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.button1 = QPushButton("Select and Preview CSV File 1")
        self.button1.clicked.connect(self.open_and_preview1)

        self.webView1 = QWebEngineView()

        self.button2 = QPushButton("Select and Preview CSV File 2")
        self.button2.clicked.connect(self.open_and_preview2)

        self.webView2 = QWebEngineView()

        self.button3 = QPushButton("Merge CSV Files")
        self.button3.clicked.connect(self.merge_csv_files)

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.webView1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.webView2)
        self.layout.addWidget(self.button3)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.layout)

    def open_and_preview1(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select CSV File 1", "", "CSV Files (*.csv)")
        if filename:
            try:
                df = pd.read_csv(filename)
                self.webView1.setHtml(df.to_html())
            except pd.errors.EmptyDataError:
                self.webView1.setHtml("The file is empty.")
            except pd.errors.ParserError:
                self.webView1.setHtml("The file is not a valid CSV file.")

    def open_and_preview2(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select CSV File 2", "", "CSV Files (*.csv)")
        if filename:
            try:
                df = pd.read_csv(filename)
                self.webView2.setHtml(df.to_html())
            except pd.errors.EmptyDataError:
                self.webView2.setHtml("The file is empty.")
            except pd.errors.ParserError:
                self.webView2.setHtml("The file is not a valid CSV file.")

    def merge_csv_files(self):
        try:
            df1 = pd.read_html(self.webView1.toPlainText())[0]
            df2 = pd.read_html(self.webView2.toPlainText())[0]

            df1_headers = df1.columns.tolist()
            df2_headers = df2.columns.tolist()

            for header in df1_headers:
                if header in df2_headers:
                    df2[header] = df2[header].fillna(df1[header])

            df2.to_csv('merged.csv', index=False)
        except:
            print("An error occurred.")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
'''