import inspect
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
import logging
from datetime import datetime
import os
import sys
import time

from main_ui import Ui_Dialog as Main_Ui

DISPLAY_LOG_IN_TERMINAL = True

logger = logging.getLogger('MyLogger')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s (%(funcName)20s:%(lineno)4d) [%(levelname)s]: %(message)s')

# Print log in terminal
if DISPLAY_LOG_IN_TERMINAL is True:
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

# Write log in file
today = datetime.now().strftime('%Y_%m_%d')
filename = f'{today}.log'

# If file exist, remove it
if os.path.isfile(filename):
    os.remove(filename)

file_handler = logging.FileHandler(filename)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class MainDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, True)

        self.main_ui = Main_Ui()
        self.main_ui.setupUi(self)
        self.setWindowTitle('QT Sample Dialog')

        # Line Edit
        self.main_ui.btn_get_le.clicked.connect(self.get_le)
        self.main_ui.btn_set_le.clicked.connect(self.set_le)

        # Exit
        self.main_ui.btn_exit.clicked.connect(self.close_dialog)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            pass

    def close_dialog(self):
        self.close()
        # self.exit(0)

    def get_le(self):
        value = self.main_ui.lineEdit.text()
        self.add_log(f'LineEdit: {value}')

    def set_le(self):
        self.main_ui.lineEdit.setText('World')

    def add_log(self, message):
        now = datetime.now()
        now = now.strftime('%H:%M:%S')

        # 호출된 함수와 라인번호 가져오기
        curframe = inspect.currentframe()
        callframe = inspect.getouterframes(curframe, 2)
        func_name = callframe[1].function
        line_no = callframe[1].lineno

        log_message = f'[{now}]: {message} <{func_name}:{line_no}>'
        file_message = f'{message} <{func_name}:{line_no}>'
        self.main_ui.tb_log.append(log_message)
        logger.info(file_message)

class ProcessThread(QThread):
    logSignal = pyqtSignal(str)
    countSignal = pyqtSignal(int)
    stopSignal = pyqtSignal()

    def __init__(self, param, interval=0.5, max_count=100):
        super(self.__class__, self).__init__()
        # super().__init__()
        self.param = param
        self.isRunning = True
        self.interval = interval
        self.max_count = max_count

    def run(self):
        self.logSignal.emit('Thread is started')
        count = 1

        while self.isRunning:
            time.sleep(self.interval)
            self.countSignal.emit(count)
            count += 1

            if count > self.max_count:
                break

        self.logSignal.emit('Thread is dead')
        self.stopSignal.emit()

    def stop(self):
        self.isRunning = False
        self.logSignal.emit('Thread is stopping...')
















if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainDialog()
    myWindow.show()
    app.exec()

























