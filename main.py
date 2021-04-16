from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from mainForm import Ui_MainWindow
from foo import fish_tank, foods, travel, sale_fish
from random import randrange as rnd
from fishes import fish_name
from PyQt5.QtWidgets import QFileDialog

import configparser
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
file = ''

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
        self.file_ini = ''

        self.config = configparser.ConfigParser()

        self.ui.btnStart.clicked.connect(self.start_timer)
        self.ui.btnStop.clicked.connect(self.stop_timer)

        self.ui.btnSave.clicked.connect(self.save_config)
        self.ui.btnOpen.clicked.connect(self.open_config)

        self.ui.btnOpenDialog.clicked.connect(self.open_file)

        self.timer = QTimer()
        self.timer.timeout.connect(self.main_loop)

    def open_file(self):
        global file
        file, _ = QFileDialog.getOpenFileName(None, 'Open File', './', "Ini (*.ini)")
        self.ui.lineEdit.setText(file)
        self.config.read(file, encoding='utf-8')

    def save_config(self):
        '''Сохраняем конфигурацию'''
        self.config.set('Options', 'pulling', str(self.ui.toPull.value()))
        self.config.set('Options', 'point1', self.ui.point1.text())
        self.config.set('Options', 'point2', self.ui.point2.text())
        self.config.set('Options', 'point3', self.ui.point3.text())
        self.config.set('Options', 'reset_min', str(int(self.ui.checkBox.isChecked())))
        self.config.set('Options', 'rnd', str(int(self.ui.random.isChecked())))
        self.config.set('Options', 'travel', str(int(self.ui.travel.isChecked())))
        self.config.set('Options', 'sale', str(int(self.ui.sale.isChecked())))
        self.config.set('Options', 'sale_count', str(self.ui.saleCount.value()))
        self.config.set('Options', 'coo_location', self.ui.coordLocacion.text())
        self.config.set('Options', 'coo_spinning', self.ui.coordSpin.text())
        self.config.set('Options', 'selected_fish', str(int(self.ui.selestedFish.isChecked())))
        self.config.set('Options', 'fish_name', self.ui.FishName.currentText())

        with open(file, 'w', encoding='utf-8') as configfile:  # save
            self.config.write(configfile)
        bot.alert('Настройки сохранены...')

    def open_config(self):
        '''Читаем кофигурацию'''
        self.ui.toPull.setValue(int(self.config['Options']['pulling']))
        self.ui.point1.setText(self.config['Options']['point1'])
        self.ui.point2.setText(self.config['Options']['point2'])
        self.ui.point3.setText(self.config['Options']['point3'])
        self.ui.checkBox.setChecked(int(self.config['Options']['reset_min']))
        self.ui.random.setChecked(int(self.config['Options']['rnd']))
        self.ui.travel.setChecked(int(self.config['Options']['travel']))
        self.ui.sale.setChecked(int(self.config['Options']['sale']))
        self.ui.saleCount.setValue(int(self.config['Options']['sale_count']))
        self.ui.coordLocacion.setText(self.config['Options']['coo_location'])
        self.ui.coordSpin.setText(self.config['Options']['coo_spinning'])
        self.ui.selestedFish.setChecked(int(self.config['Options']['selected_fish']))
        self.ui.FishName.setCurrentText((self.config['Options']['fish_name']).strip())

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
                self.ui.txtLog.append('Выкинули малька...')
            else:
                if self.ui.sale.isChecked():
                    # if 'зачетная' in res[1].split():
                    self.fsale += 1

                if self.fsale >= self.ui.saleCount.value():
                    sale_fish(self.coo_location, self.coo_spinning)
                    self.fsale = 0
                    self.ui.txtLog.clear()
                    self.log_count = 0

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

            if self.fl >= self.tmp_point:
                self.fl = 0

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

                bot.sleep(.5)
        else:
            # вываживание рыбы
            bot.keyUp('g')
            bot.keyDown('ctrlright')
            bot.sleep(.3)
            bot.press('f')

    def add_fish(self):
        '''Добавляем список рыб'''
        for i in fish_name.split('\n'):
            self.ui.FishName.addItem(i.strip())


if __name__ == '__main__':
    win = MyMainWindow()
    win.add_fish()
    win.show()

    sys.exit(app.exec_())
