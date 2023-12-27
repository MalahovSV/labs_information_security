import numpy as np


class Playfair:
    matrix_playfair = []
    alphabet = []
    message = []
    encrypted_word = ''
    insert_litter = 'я'

    def __init__(self, key, message):
        self.create_ru_alphabet()  # русский алфавит по порядку
        self.generate_matrix(str(key).lower())  # формирование матрицы с ключом
        self.message = str(message).lower().replace(" ", "")
        self.create_bigram_word()
        self.encrypt()

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

    def create_bigram_word(self):
        temp = []
        count_chrs = len(self.message)
        index = 0
        print(len(self.message), self.message)
        while index < (count_chrs - 1 if count_chrs % 2 < 1 else count_chrs - 2):
            if self.message[index] == self.message[index+1]:
                temp.append([self.message[index], 'я'])
                index += 1
            else:
                temp.append([self.message[index], self.message[index + 1]])
                index += 2
        if len(temp) % 2 > 0:
            temp.append([self.message[len(self.message)-1], 'я'])
        self.message = temp

    def encrypt(self):
        print("Квадрат Плейфеера: \n", self.matrix_playfair)
        for letter in self.message:
            first_indexes = np.where(self.matrix_playfair == letter[0])
            second_indexes = np.where(self.matrix_playfair == letter[1])

            if first_indexes[0] == second_indexes[0]:
                if first_indexes[1] == 5:
                    self.encrypted_word += self.matrix_playfair[int(second_indexes[0]), int(second_indexes[1])+1]
                    self.encrypted_word += self.matrix_playfair[first_indexes[0], 0]
                elif second_indexes[1] == 5:
                    self.encrypted_word += self.matrix_playfair[int(first_indexes[0]), int(first_indexes[1])+1]
                    self.encrypted_word += self.matrix_playfair[second_indexes[0], 0]
                else:
                    self.encrypted_word += self.matrix_playfair[int(first_indexes[0]), int(first_indexes[1]) + 1]
                    self.encrypted_word += self.matrix_playfair[int(second_indexes[0]), int(second_indexes[1]) + 1]
            elif first_indexes[1] == second_indexes[1]:
                if first_indexes[1] == 5:
                    self.encrypted_word += self.matrix_playfair[int(second_indexes[0])+1, int(second_indexes[1])]
                    self.encrypted_word += self.matrix_playfair[0, first_indexes[1]]
                elif second_indexes[1] == 5:
                    self.encrypted_word += self.matrix_playfair[int(first_indexes[0])+1, int(first_indexes[1])]
                    self.encrypted_word += self.matrix_playfair[0, second_indexes[0]]
                else:
                    self.encrypted_word += self.matrix_playfair[int(first_indexes[0]) + 1, int(first_indexes[1])]
                    self.encrypted_word += self.matrix_playfair[int(second_indexes[0]) + 1, int(second_indexes[1])]
            else:
                self.encrypted_word += self.matrix_playfair[int(first_indexes[0]), int(second_indexes[1])]
                self.encrypted_word += self.matrix_playfair[int(second_indexes[0]), int(first_indexes[1])]
        print("Зашифрованное сообщение: ", self.encrypted_word)



