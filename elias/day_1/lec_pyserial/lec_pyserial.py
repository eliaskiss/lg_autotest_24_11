from pickletools import read_unicodestringnl

import serial
from icecream import ic
import time

ic.configureOutput(includeContext=True)
# ic.disable()

################################################
# Open Serial
################################################
def openSerial(port, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False,
               dsrdtr=False):

    # 시리얼 포트 객체 생성
    ser = serial.Serial()

    # 시리얼 포트설정
    ser.port = port             # Port Name: com1, com2,...
    ser.stopbits = stopbits
    ser.baudrate = baudrate     # Baudrate 속도: 9600, 115200, ...
    ser.bytesize = bytesize     # Data Bit
    ser.parity = parity         # Check Parity
    ser.timeout = timeout          # Timeout None: 무한대기, n: n초 대기
    ser.xonxoff = xonxoff       # Sw Flow control
    ser.rtscts = rtscts         # RTS/CTS Flow control
    ser.dsrdtr = dsrdtr         # DSR/DTR Flow control

    # 시리얼 포트 열기
    ser.open()

    # 시리얼 포트객체 생성시, 포트설정값을 넣으면, open은 필요없음
    # ser = serial.Serial(port, baudrate, ...)

    return ser

################################################
# Write Port
################################################
def writePort(ser, data):
    ser.write(data)

def writePortUnicode(ser, data, encode='utf-8'):
    writePort(ser, data.encode(encode))

################################################
# Read Port
################################################
def read(ser, size=1, timeout=None):
    ser.timeout = timeout
    readed = ser.read(size)
    return readed

################################################
# Read EOF
# Putty에서의 EOF값 --> Ctrl + j
################################################
def readEOF(ser):
    readed = ser.readline()
    return readed[:-1]

################################################
# Read Until ExitCode
# Ctrl + C 값이 넘어올때까지 read
################################################
def readUntilExitCode(ser, code=b'\x03'):
    readed = b''
    while True:
        data = ser.read()
        ic(data)
        readed += data

        if data == code:
            return readed


if __name__ == '__main__':
    # 포트열기
    ser = openSerial(port='com2')

    # 포트쓰기
    data = 'HelloWorld\r\n'
    # writePort(ser, data.encode()) # unicode --> bytes array
    writePortUnicode(ser, data)

    # 포트읽기
    # ic(read(ser))

    # 10 byte 읽기
    # ic(read(ser, 10))

    # EOF까지 읽기
    # ic(readEOF(ser))

    # Ctrl + C가 들어올때까지 read
    ic(readUntilExitCode(ser))















