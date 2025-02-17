import sys
import time
import os


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QRadioButton, QButtonGroup
from PyQt5.QtWidgets import QMainWindow, QLabel, QFileDialog, QLineEdit, QComboBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from functools import partial


class Cats(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self._1_ = 0
        self.pussy_cats = ('персидская', 'мэйн-кун', 'рэгдолл', 'сиамская', 'абиссинская', 'британская короткошерстная',
        'шотландская вислоухая', 'сфинкс', 'бенгальская', 'сибирская', 'русская голубая',
                     'американская короткошерстная', 'бирманская', 'ориентальная', 'бурманская', 'беспородная',
                         'персидский', 'мэйн-кун', 'рэгдолл', 'сиамский', 'абиссинский', 'британский короткошерстный',
        'шотландский вислоухий', 'сфинкс', 'бенгальский', 'сибирский', 'русский голубой',
                     'американский короткошерстный', 'бирманский', 'ориентальный', 'бурманский', 'беспородный')
        self._2_ = 0
        self._3_ = 0
        self._35_ = -1
        self._4_ = 0
        self.i = 0
        self.path = ''
        self._2_check = False
        self._3_check = False
        self._35_check = False
        self._4_check = False

    def initUI(self):
        self.setGeometry((QApplication.desktop().width() - 1200) // 2,
                         (QApplication.desktop().height() - 440) // 2, 1200, 440)
        self.setWindowTitle(
            'КОТОБОТ'
        )

        self.setWindowIcon(QIcon('cat.png'))

        self.btn = QPushButton('НАЧАТЬ', self)
        self.btn.resize(1000, 120)
        self.btn.move(100, 300)
        self.btn.clicked.connect(partial(self.next_form, self.first_question))
        self.btn.setStyleSheet("font-size: 20px")

        self.btn1 = QPushButton('Далее', self)
        self.btn1.move(700, 480)
        self.btn1.hide()
        self.btn1.setStyleSheet("font-size: 20px")

        self.btn2 = QPushButton('Назад', self)
        self.btn2.resize(1000, 120)
        self.btn2.move(100, 480)
        self.btn2.hide()
        self.btn2.setStyleSheet("font-size: 20px")

        self.linedit = QLineEdit(self)
        self.linedit.resize(400, 120)
        self.linedit.move(700, 320)
        self.linedit.hide()
        self.linedit.editingFinished.connect(self.third)

        self.label3 = QLabel(self)
        self.label3.move(700, 400)
        self.label3.resize(1000, 900)

        self.box7 = QRadioButton('Меньше трех месяцев', self)
        self.box7.resize(800, 200)
        self.box7.move(40, 140)
        self.box7.clicked.connect(partial(self.second, 0))
        self.box7.hide()
        self.box7.setStyleSheet("font-size: 20px")

        self.box = QRadioButton('Три месяца - год', self)
        self.box.resize(800, 200)
        self.box.move(40, 240)
        self.box.clicked.connect(partial(self.second, 1))
        self.box.hide()
        self.box.setStyleSheet("font-size: 20px")

        self.box1 = QRadioButton('Год -  семь лет', self)
        self.box1.resize(800, 200)
        self.box1.move(440, 140)
        self.box1.hide()
        self.box1.clicked.connect(partial(self.second, 2))
        self.box1.setStyleSheet("font-size: 20px")

        self.box2 = QRadioButton('Больше семи лет', self)
        self.box2.resize(800, 200)
        self.box2.move(440, 240)
        self.box2.hide()
        self.box2.clicked.connect(partial(self.second, 3))
        self.box2.setStyleSheet("font-size: 20px")

        self.box3 = QRadioButton('Мужской', self)
        self.box3.resize(800, 200)
        self.box3.move(40, 100)
        self.box3.clicked.connect(partial(self.first, 1))
        self.box3.hide()
        self.box3.setStyleSheet("font-size: 20px")

        self.box4 = QRadioButton('Женский', self)
        self.box4.resize(800, 200)
        self.box4.move(40, 200)
        self.box4.hide()
        self.box4.clicked.connect(partial(self.first, 2))
        self.box4.setStyleSheet("font-size: 20px")

        self.box5 = QRadioButton('Нашёл на улице', self)
        self.box5.resize(800, 200)
        self.box5.move(40, 100)
        self.box5.clicked.connect(partial(self.thourth, 0))
        self.box5.hide()
        self.box5.setStyleSheet("font-size: 20px")

        self.box6 = QRadioButton('Купил (отдали)', self)
        self.box6.resize(800, 200)
        self.box6.move(40, 200)
        self.box6.hide()
        self.box6.clicked.connect(partial(self.thourth, 1))
        self.box6.setStyleSheet("font-size: 20px")

        self.combo = QComboBox(self)
        self.combo.resize(400, 120)
        self.combo.move(700, 320)
        self.combo.addItems(["Лишай",
                             "Проблемы с желудком", "Травма мозга", "Нету"])
        self.combo.activated.connect(self.fourth)
        self.combo.hide()
        self.combo.setStyleSheet("font-size: 20px")

        self.group = QButtonGroup()
        self.group.addButton(self.box3)
        self.group.addButton(self.box4)

        self.group1 = QButtonGroup()
        self.group1.addButton(self.box5)
        self.group1.addButton(self.box6)

        self.label = QLabel(self)
        self.label.resize(800, 200)
        self.label.setText(
            "ВАС ПРИВЕТСТВУЕТ КОТОБОТ"
        )
        self.label.move(440, 0)
        self.label.setStyleSheet("font-size: 20px")

        self.label1 = QLabel(self)
        self.label1.resize(800, 200)
        self.label1.setText(
            "Поздравляем с пополнением"
        )
        self.label1.move(444, 80)
        self.label1.setStyleSheet("font-size: 20px")

        self.label2 = QLabel(self)
        self.label2.resize(800, 200)
        self.label2.setText(
            "Для начала работы ответьте на пару вопросов"
        )
        self.label2.move(352, 120)
        self.label2.setStyleSheet("font-size: 20px")

        self.error = QLabel(self)
        self.error.resize(800, 200)
        self.error.hide()
        self.error.setStyleSheet("font-size: 20px")

    def first_question(self):
        self.btn1.move(100, 480)
        self.btn1.resize(1000, 120)
        self.btn1.disconnect()
        self.btn1.clicked.connect(partial(self.fecond_question, self.second_question))
        self.btn.move(100, 480)
        self.box3.show()
        self.box4.show()
        self.setGeometry((QApplication.desktop().width() - 1200) // 2,
                         (QApplication.desktop().height() - 640) // 2, 1200, 640)
        self.label.setText(
            "1. Какого пола ваше котообразное?"
        )
        self.label.move(440, 0)

    def second_question(self):
        self.btn1.move(700, 480)
        self.btn1.resize(400, 120)
        self.btn1.disconnect()
        self.btn1.clicked.connect(partial(self.fecond_question, self.third_question))
        if self._2_check is True:
            self.btn1.show()
        self.box.show()
        self.box1.show()
        self.box2.show()
        self.box7.show()
        self.setGeometry((QApplication.desktop().width() - 1200) // 2,
                         (QApplication.desktop().height() - 640) // 2, 1200, 640)
        self.label.setText(
            "2. Какого возраста ваш кот?"
        )
        self.label.move(440, 0)
        self.btn2.show()
        self.btn2.move(100, 480)
        self.btn2.resize(400, 120)
        self.btn2.disconnect()
        self.btn2.clicked.connect(partial(self.sirst_question, self.first_question))

    def third_question(self, cat=-1):
        self.setGeometry((QApplication.desktop().width() - 1200) // 2,
                         (QApplication.desktop().height() - 640) // 2, 1200, 640)
        self.linedit.show()
        if cat != -1:
            if self._1_ == 1:
                self.linedit.setText(self.pussy_cats[self.i + 16])
                self._3_ = self.pussy_cats[self.i + 16]
            elif self._1_ == 2:
                self.linedit.setText(self.pussy_cats[self.i])
                self._3_ = self.pussy_cats[self.i]
        self.label.setText(
            "3. Какой породы ваш кот?"
        )
        self.label.move(440, 0)
        if self._2_ != 0:
            self.btn.show()
            self.btn.move(100, 320)
            self.btn.setText('Я не знаю')
            self.btn.setStyleSheet("font-size: 20px")
            self.btn.resize(400, 120)
            self.btn.disconnect()
            self.btn.clicked.connect(partial(self.fecond_question, self.i_dont_know_3))
        if self._2_ != 0:
            self.btn1.move(700, 480)
            self.btn1.resize(400, 120)
            self.btn1.setStyleSheet("font-size: 20px")
        else:
            self.btn1.move(100, 480)
            self.btn1.resize(1000, 120)
        self.btn1.setText('Далее')
        if self._3_check is True:
            self.btn1.show()
        self.btn1.disconnect()
        self.btn1.clicked.connect(self.wrong_text)
        self.btn2.show()
        self.btn2.resize(400, 120)
        if self._2_ != 0:
            self.btn2.move(100, 480)
        else:
            self.btn2.move(100, 320)
        self.btn2.disconnect()
        self.btn2.setText('Назад')
        self.btn2.clicked.connect(partial(self.sirst_question, self.second_question))

    def thourth_question(self):
        self.btn1.hide()
        if self._3_ == 'беспородный':
            self.label.setText(
                "4. Откуда у вас кот?"
            )
        else:
            self.label.setText(
                "4. Откуда у вас кошка?"
            )
        self.label.show()
        self.box5.show()
        self.box6.show()
        self.btn1.move(100, 500)
        self.btn1.resize(1000, 80)
        self.btn1.setText('Далее')
        self.btn1.disconnect()
        self.btn1.clicked.connect(partial(self.fecond_question, self.fourth_question))
        if self._35_check is True:
            self.btn1.show()
        self.btn2.show()
        self.btn2.resize(1000, 80)
        self.btn2.move(100, 400)
        self.btn2.setText('Назад')
        self.btn2.disconnect()
        self.btn2.clicked.connect(partial(self.sirst_question, self.third_question))

    def fourth_question(self):
        self.btn1.hide()
        self.btn1.move(100, 480)
        self.btn1.resize(1000, 120)
        self.btn1.setText('Готово')
        self.btn1.disconnect()
        self.btn1.clicked.connect(partial(self.next_form, self.mainwindow))
        if self._4_check is True:
            self.btn1.show()
        self.btn.move(100, 480)
        self.combo.show()
        self.setGeometry((QApplication.desktop().width() - 1200) // 2,
                         (QApplication.desktop().height() - 640) // 2, 1200, 640)
        if self._35_ == -1:
            self.label.setText(
                "4. Есть ли у вашего питомца какие-либо недуги?"
            )
        else:
            self.label.setText(
                "5. Есть ли у вашего питомца какие-либо недуги?"
            )
        self.label.move(330, 0)
        self.btn2.show()
        self.btn2.resize(400, 120)
        self.btn2.move(100, 320)
        self.btn2.disconnect()
        self.btn2.setText('Назад')
        if self._35_ == -1:
            self.btn2.clicked.connect(partial(self.sirst_question, self.third_question))
        else:
            self.btn2.clicked.connect(partial(self.sirst_question, self.thourth_question))

    def i_dont_know_3(self):
        self.i = 0
        self.label.setText(
            "Какой из этих красавцев похож на вашего?"
        )
        self.label.setStyleSheet("font-size: 20px")
        self.label.move(450, -30)
        self.setGeometry((QApplication.desktop().width() - 1300) // 2,
                         (QApplication.desktop().height() - 1000) // 2, 1300, 1000)
        self.btn.show()
        self.btn.setText('>')
        self.btn.setStyleSheet("font-size: 16px")
        self.btn.resize(20, 50)
        self.btn.move(1250, 450)
        self.btn.disconnect()
        self.btn.clicked.connect(partial(self.straight_ahead, 1))
        self.btn1.setText('<')
        self.btn1.setStyleSheet("font-size: 16px")
        self.btn1.resize(20, 50)
        self.btn1.move(50, 450)
        self.btn1.disconnect()
        self.btn1.clicked.connect(partial(self.straight_ahead, 0))
        self.btn2.show()
        self.btn2.setText('Этот')
        self.btn2.move(470, 900)
        self.btn2.disconnect()
        self.btn2.clicked.connect(partial(self.sirst_question, partial(self.third_question, 0)))
        for i in os.listdir(self.path):
            if self.pussy_cats[self.i] in i:
                self.label3.setPixmap(QPixmap(os.path.join(self.path, i)))
        self.label3.show()
        self.label3.move(150, 50)

    def straight_ahead(self, direction):
        self.label3.show()
        self.label1.hide()
        self.label2.hide()
        self.label.show()
        self.btn.show()
        self.btn1.show()
        if direction == 1:
            self.i += 1
        if direction == 0:
            self.i -= 1
        if self.i == 15:
            self.btn.hide()
            self.label.hide()
            self.label3.hide()
            self.label2.show()
            self.label2.setText('НЕ НАШЛИ СВОЕГО?')
            self.label2.move(550, 300)
            self.label1.setText('НАЖМИТЕ КНОПКУ И МЫ ЗАПИШЕМ ЕГО КАК ДВОРНЯГУ')
            self.label1.move(400, 400)
            self.label1.show()
            return
        print(self.i)
        if self.i == 0:
            self.btn1.hide()
        for j in os.listdir(self.path):
            print(j)
            if self.pussy_cats[self.i] in j:
                self.label3.setPixmap(QPixmap(os.path.join(self.path, j)))
                return
        return

    def mainwindow(self):
        self.setGeometry(0, 30, 1920, 1130)
        self.btn1.resize(601, 120)
        self.btn1.setText('Первые дни')
        self.btn1.move(49, 428)
        self.btn1.disconnect()
        self.btn1.clicked.connect(partial(self.to_info_window, 0))
        self.btn2.show()
        self.btn2.resize(608, 120)
        self.btn2.setText('Питание и туалет')
        self.btn2.move(650, 428)
        self.btn2.disconnect()
        self.btn2.clicked.connect(partial(self.to_info_window, 1))
        self.btn.show()
        self.btn.resize(608, 120)
        self.btn.setText('Досуг')
        self.btn.move(1258, 428)
        self.btn.disconnect()
        self.btn.clicked.connect(partial(self.to_info_window, 2))
        self.label.show()
        self.label.resize(600, 408)
        self.label.move(50, 20)
        self.label.setPixmap(QPixmap(os.path.join('data', '4230252.jpg')))
        self.label1.show()
        self.label1.resize(608, 408)
        self.label1.move(650, 20)
        self.label1.setPixmap(QPixmap(os.path.join('data', 'кошка_ест.jpg')))
        self.label2.show()
        self.label2.resize(608, 408)
        self.label2.move(1258, 20)
        self.label2.setPixmap(QPixmap(os.path.join('data', 'кошка_играет.jpg')))

    def to_info_window(self, button):
        if button == 0:
            pictures = [2, 3, 6, 8]
            if self._35_ == 0:
                pictures += [1, 5]
            if self._2_ == 3:
                pictures.append(4)
            if self._2_ == 0 or self._2_ == 1:
                pictures.append(7)
        if button == 1:
            pictures = [19, 20]
            if self._2_ == 0:
                pictures += [9, 10, 11]
            if self._2_ == 1:
                pictures.append(12)
            if self._2_ == 3:
                pictures.append(13)
            if self._4_ == 'Проблемы с желудком':
                pictures.append(14)
            i = self.pussy_cats.index(self._3_)
            if i == 5 or i == 6 or i == 21 or i == 22:
                pictures.append(15)
            if self._3_ == 7:
                pictures.append(16)
            if self._3_ == 1:
                pictures.append(17)
            if self._3_ == 0 or self._3_ == 16:
                pictures.append(18)
        if button == 2:
            pictures = [25, 26, 27]
            i = self.pussy_cats.index(self._3_)
            if i in (4, 11, 8, 5, 14, 13, 10, 6, 20, 27, 24, 21, 30, 29, 26, 22):
                pictures.append(21)
            elif i == 7:
                pictures.append(24)
            else:
                pictures.append(22)
            if i != 7:
                pictures.append(23)
            if self._2_ == 3:
                pictures.append(28)
        pictures.sort()
        self.next_class = InfoWindow(pictures)
        self.next_class.show()

    def first(self, number):
        self.btn1.show()
        self._1_ = number

    def second(self, number):
        self.btn1.show()
        self._2_ = number
        if number == 1:
            self.path = 'MELKII'
        if number == 2:
            self.path = 'POBOLSHE'
        if number == 3:
            self.path = 'BOLSHOY'
        self._2_check = True

    def third(self):
        self.btn1.show()
        self._3_ = self.linedit.text().lower()
        self._3_check = True

    def thourth(self, number):
        self.btn1.show()
        self._35_ = number
        self._35_check = True

    def fourth(self):
        self.btn1.show()
        self._4_check = True
        self._4_ = self.combo.currentText()

    def wrong_text(self):
        if self._3_ in self.pussy_cats:
            if self._3_ == 'беспородная' or self._3_ == 'беспородный':
                return self.fecond_question(self.thourth_question)
            self._35_ = -1
            return self.fecond_question(self.fourth_question)
        if self._3_[-1] == 'й':
            r = range(16, 32)
        else:
            r = range(32)
        for i in r:
            if -2 <= len(set([j for j in self.pussy_cats[i] + self._3_])) - len(set([j for j in self.pussy_cats[i]])) <= 1\
                    and -1 <= len(self._3_) - len(self.pussy_cats[i]) <= 1:
                if self.pussy_cats[i] == 'бирманский' or self.pussy_cats[i] == 'бирманская' \
                or self.pussy_cats[i] == 'бурманский' or self.pussy_cats[i] == 'бурманский':
                    self.error.setText(
                        'Возможно, вы имели ввиду "' + 'бурманск' + self.pussy_cats[i][-2::] + '" или ' \
                        + '"бирманск' + self.pussy_cats[i][-2::] + '"'
                    )
                else:
                    self.error.setText(
                        'Возможно, вы имели ввиду "' + self.pussy_cats[i] + '"'
                    )
                self.error.show()
                self.error.move(200, 80)
                return
        self.error.setText(
            'Таких не знаем'
        )
        self.error.show()
        return

    def fecond_question(self, function):
        self.btn1.hide()
        self.next_form(function)

    def sirst_question(self, function):
        self.btn1.show()
        self.next_form(function)

    def next_form(self, function):
        self.label3.hide()
        self.label2.hide()
        self.label1.hide()
        self.btn2.hide()
        self.linedit.hide()
        self.btn.hide()
        self.box.hide()
        self.box1.hide()
        self.box2.hide()
        self.box3.hide()
        self.box4.hide()
        self.box5.hide()
        self.box6.hide()
        self.box7.hide()
        self.error.hide()
        self.combo.hide()
        return function()


class InfoWindow(QWidget):
    def __init__(self, pictures):
        super().__init__()
        self.i = 0
        self.pictures = pictures
        self.initUi()

    def initUi(self):
        self.setGeometry(600, 220, 740, 350)

        self.label = QLabel(self)
        self.label.resize(600, 311)
        self.label.move(70, 20)

        self.btn = QPushButton(self)
        self.btn.setText('>')
        self.btn.resize(20, 50)
        self.btn.move(690, 150)
        self.btn.clicked.connect(partial(self.last_form, 1))

        self.btn1 = QPushButton(self)
        self.btn1.setText('<')
        self.btn1.resize(20, 50)
        self.btn1.move(30, 150)
        self.btn1.hide()
        self.btn1.clicked.connect(partial(self.last_form, -1))

        self.last_form(0)

    def last_form(self, arg):
        print(self.pictures)
        self.i += arg
        self.label.setPixmap(QPixmap(os.path.join('data', str(self.pictures[self.i]) + '.png')))
        if self.i == 0:
            self.btn1.hide()
            self.btn.show()
        elif self.i == len(self.pictures) - 1:
            self.btn.hide()
            self.btn1.show()
        else:
            self.btn1.show()
            self.btn.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Cats()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())