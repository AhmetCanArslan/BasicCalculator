from PyQt6 import QtWidgets
from calcForm import Ui_Main
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.ui.btn_bol.clicked.connect(self.hesapla)
        self.ui.btn_carp.clicked.connect(self.hesapla)
        self.ui.btn_cikar.clicked.connect(self.hesapla)
        self.ui.btn_topla.clicked.connect(self.hesapla)


    def hesapla(self):
        sender = self.sender()#hangi butona basıldığını anlamak için

        if(sender.text() == "Topla"):
            result = int(self.ui.lbl_sayi1.text()) + int(self.ui.lbl_sayi2.text())
        elif(sender.text() == "Çıkar"):
            result = int(self.ui.lbl_sayi1.text()) - int(self.ui.lbl_sayi2.text())
        elif(sender.text()=="Böl"):
            if(int(self.ui.lbl_sayi2.text()) != 0):
                result = int(self.ui.lbl_sayi1.text()) / int(self.ui.lbl_sayi2.text())
            else:
                result = "Division By Zero Error!"
        else:
            result = int(self.ui.lbl_sayi1.text())*int(self.ui.lbl_sayi2.text())
        self.ui.lbl_sonuc.setText(str(result))


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())




app()