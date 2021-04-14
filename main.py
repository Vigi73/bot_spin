from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from mainForm import Ui_MainWindow
from foo import fish_tank, foods, travel, sale_fish
from random import randrange as rnd

import sys
import pyautogui as bot
import psutil as pu

app = QtWidgets.QApplication(sys.argv)


def tick(tmp, value):
    if tmp:
        bot.keyDown('g')
        tmp -= 1
    else:
        bot.keyUp('g')
        tmp = value
        bot.press('t')


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(294, 700)
        self.tmp = 0
        self.log_count = 0
        self.count_point = 0  # Количество точек заброса
        self.tmp_point = 0
        self.list_point = []
        self.fl = 0
        self.coo_location = 0
        self.coo_spinning = 0
        self.fish_count_for_sale = 0
        self.fsale = 0
        self.ui.btnStop.setVisible(False)

        self.ui.btnStart.clicked.connect(self.start_timer)
        self.ui.btnStop.clicked.connect(self.stop_timer)

        self.timer = QTimer()
        self.timer.timeout.connect(self.main_loop)

    def stop_timer(self):
        self.ui.btnStart.setVisible(True)
        self.ui.btnStop.setVisible(False)
        self.timer.stop()

    def start_timer(self):
        if "RF3.exe" in [p.name() for p in pu.process_iter()]:
            self.timer.start(500)  # Запуск оснавного таймера
            self.ui.btnStart.setVisible(False)
            self.ui.btnStop.setVisible(True)

            if self.ui.sale.isChecked():
                self.fish_count_for_sale = self.ui.saleCount.value()
                try:
                    self.coo_location = tuple(map(int, self.ui.coordLocacion.text().split(',')))
                    self.coo_spinning = tuple(map(int, self.ui.coordSpin.text().split(',')))

                except:
                    pass

            self.ui.txtLog.clear()
            self.log_count = 0
            self.tmp = self.ui.toPull.value()
            # Заполняем список точками заброса
            if self.ui.point1.text():
                self.list_point.append(tuple(map(int, self.ui.point1.text().split(','))))
            if self.ui.point2.text():
                self.list_point.append(tuple(map(int, self.ui.point2.text().split(','))))
            if self.ui.point3.text():
                self.list_point.append(tuple(map(int, self.ui.point3.text().split(','))))

            self.tmp_point = len(self.list_point)

            # Первый заброс
            bot.click(self.list_point[0])

            # Определяем сколько точек заброса использовать
            if self.ui.point1.text():
                self.count_point += 1

            if self.ui.point2.text():
                self.count_point += 1

            if self.ui.point3.text():
                self.count_point += 1

        else:
            try:
                self.timer_stop()
            except:
                pass
            bot.alert('Запустите рыбалку', 'Внимание!')

    # Основной цикл _____________________________________________________________________________
    def main_loop(self):

        self.ui.lcdNumber.display(str(self.log_count))

        # Если голод
        if foods():
            self.ui.txtLog.append(f'Перекусил')

        # Если поймали и открылся садок
        if res := fish_tank(self.ui.checkBox.isChecked()):
            bot.keyUp('g')
            bot.sleep(.1)
            bot.keyUp('ctrlright')

            if res == - 1:
                self.ui.txtLog.append('Отпустили не зачёт')
            else:
                if self.ui.sale.isChecked():
                    # if 'зачетная' in res[1].split():
                    self.fsale += 1

                if self.fsale >= self.ui.saleCount.value():
                    sale_fish(self.coo_location, self.coo_spinning)
                    self.fsale = 0

                self.ui.txtLog.append(f'{res[0]}: {res[1]}')
                self.log_count += 1
                bot.sleep(.2)
                bot.press('space')

        # Если продлить путевку
        if self.ui.travel.clicked:
            if im := bot.locateOnScreen('img/put_full.bmp', region=(454, 221, 391, 221)):
                travel()

        if im := bot.locateOnScreen('img/headr_spin.bmp', region=(454, 384, 797, 127)):
            # тянем пока не клюнуло tmp раз
            bot.keyUp('ctrlright')
            bot.sleep(.2)
            if self.tmp:
                bot.keyDown('g')
                self.tmp -= 1
            else:
                bot.keyUp('g')

                self.tmp = self.ui.toPull.value()
                if self.ui.random.isChecked():
                    bot.click(self.list_point[rnd(self.tmp_point)])
                else:
                    bot.click(self.list_point[self.fl])
                    self.fl += 1

            if self.fl >= self.tmp_point:
                self.fl = 0

                # bot.press('t')
                bot.sleep(.5)
        else:
            # вываживание рыбы
            bot.keyUp('g')
            bot.keyDown('ctrlright')
            bot.sleep(.3)
            bot.press('f')


if __name__ == '__main__':
    win = MyMainWindow()
    win.show()

    sys.exit(app.exec_())
