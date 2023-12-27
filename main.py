import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit, QComboBox, QPushButton
import numpy as np


class EncryptionPlayfair:
    matrix_playfair = []
    alphabet = []

    def __init__(self, key):
        self.create_ru_alphabet()                   #русский алфавит по порядку
        self.generate_matrix(str(key).lower())      #формирование матрицы с ключом


    def create_ru_alphabet(self):
        get_letters = lambda start, end: [chr(code_char) for code_char in range(start, end)]
        self.alphabet = get_letters(1072, 1078)
        self.alphabet.append(get_letters(1105, 1106)[0])
        self.alphabet = self.alphabet + get_letters(1078, 1104)

    def generate_matrix(self, key):
        for letter in key:
            if not (letter in self.matrix_playfair) and ord(letter) != 32:
                self.matrix_playfair.append(letter)
        for character in self.alphabet:
            self.matrix_playfair.append(character) if character not in self.matrix_playfair else ''
        self.matrix_playfair.append('-')
        self.matrix_playfair.append('1')
        self.matrix_playfair.append('2')
        self.matrix_playfair = np.array(self.matrix_playfair).reshape(6, 6)


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
    # app = QApplication(sys.argv)
    # ex = Example()
    # sys.exit(app.exec_())
    EncryptionPlayfair("Ехал грека через реку видит грека в реке рак")
