from PyQt5.QtWidgets import *
from urllib.request import urlopen
import html2text

class Okno_do_podania_tekstu(QMainWindow):
    def __init__(self):
        super().__init__()
        ja = QVBoxLayout()
        przycisk = QPushButton("Enter URL")
        przycisk.clicked.connect(self.click)
        ja.addWidget(przycisk)
        self.url = QLineEdit()
        ja.addWidget(self.url)
        widget = QWidget()
        self.setWindowTitle("WWW Browser")
        widget.setLayout(ja)
        self.setCentralWidget(widget)
    def click(self, checked):
        url2 = self.url.text()
        html2 = urlopen(url2).read().decode('utf-8')
        self.strona = html2text.html2text(html2)
        self.okno = Okno(self.strona,url2)
        self.okno.show()
class Okno(QWidget):
    def __init__(self,strona,url_do_wczytania):
        super().__init__()
        ja = QVBoxLayout()
        self.label = QLabel(strona, self)
        ja.addWidget(self.label)
        self.setWindowTitle("Web page {}".format(url_do_wczytania))
        self.setLayout(ja)



app = QApplication([])
aplikacja = Okno_do_podania_tekstu()
aplikacja.show()
app.exec()



