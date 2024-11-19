import serial
from icecream import ic
import time

ic.configureOutput(includeContext=True)

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


if __name__ == '__main__':
    # 포트열기
    ser = openSerial(port='com2')

    # 포트쓰기
    data = 'HelloWorld\r\n'
    # writePort(ser, data.encode()) # unicode --> bytes array
    writePortUnicode(ser, data)




















