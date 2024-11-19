from lec_pyserial_class import MySerial
from icecream import ic

ic.configureOutput(includeContext=True)

# Echo Server
# 입력받다가 Enter키가 입력되는 순간 그동안의 데이터를 출력하는 에코서버
# Exit, exit, EXIT, eXit, EXit lower() 들어오면 프로그램 종료`
# b'\x0d'

def main():
    ser = MySerial()
    ser.openSerial('com2')

    # ....

if __name__ == '__main__':
    main()