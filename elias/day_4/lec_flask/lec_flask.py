from flask import Flask, request
from flask_restx import Api, Resource, reqparse
from flask_cors import CORS # Cross Origin Resource Sharing
from datetime import datetime, timedelta
import logging
import sys

# Write log in file
today = datetime.now()
today = today.strftime('%Y_%m_%d')
file_name = f'{today}.log'

DISPLAY_LOG_IN_TERMINAL = True

logger = logging.getLogger('MyLogger')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s (%(funcName)s:%(lineno)d) [%(levelname)s]: %(message)s')

if DISPLAY_LOG_IN_TERMINAL:
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

file_handler = logging.FileHandler(file_name)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)









