import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ma Fenêtre")
        self.__nb = 0
        # Create the LineEdit
        self.__l = QLineEdit(self)
        self.__mettre_pub()
        self.__l.setGeometry(0, 0, 400, 200)
        self.__l.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        # Create a button
        self.__b1 = QPushButton("0", self)
        self.__b1.setGeometry(0, 200, 100, 50)
        self.__b1.clicked.connect(self.__cpt)
        self.__b2 = QPushButton("Effacer pub", self)
        self.__b2.setGeometry(300, 200, 100, 50)
        self.__b2.clicked.connect(self.__l.clear)
        self.__b3 = QPushButton("Remettre pub", self)
        self.__b3.setGeometry(300, 200, 100, 50)
        self.__b3.clicked.connect(self.__mettre_pub)
        self.__b3.hide()
        self.__b2.clicked.connect(self.__b3.show)
        self.__b2.clicked.connect(self.__b2.hide)
        self.__b3.clicked.connect(self.__b2.show)
        self.__b3.clicked.connect(self.__b3.hide)

    # Slot du bouton 1
    def __cpt(self):
        self.__nb += 1
        self.__b1.setText(str(self.__nb))

    def __mettre_pub(self):
        self.__l.setText("Achetez des pommes !\nC'est bon pour vous.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
