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
#
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























