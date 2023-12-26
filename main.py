import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit, QComboBox, QPushButton

class EncryptionPlayfair:
    def __init__(self, key):
        matrix_playfair = []
        for letter in key:
            matrix_playfair.append(letter)
        print(matrix_playfair)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        encryption_combo = QComboBox(self)
        encryption_combo.addItems(['Шифр Плейфеера',
                                   'Шифр Цезаря'])
        encryption_combo.move(15, 10)

        txt_key_message = QLabel('Ключ: ', self)
        txt_key_message.move(15, 40)

        edit_start_message = QLineEdit(self)
        edit_start_message.move(15, 70)

        txt_start_message = QLabel('Исходное сообщение: ', self)
        txt_start_message.move(15, 100)

        edit_start_message = QLineEdit(self)
        edit_start_message.move(15, 130)

        btn = QPushButton("Зашифровать", self)
        btn.move(15, 160)



        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('Absolute')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    EncryptionPlayfair("Hello")

    sys.exit(app.exec_())