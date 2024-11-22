import cv2
from icecream import ic
from datetime import datetime
import time

ic.configureOutput(includeContext=True)

# VideoCaptureAPIs 열거형 상수	설명
# CAP_ANY	자동 선택
# CAP_V4L, CAP_V4L2	V4L/V4L2(리눅스)
# CAP_FIREWIRE, CAP_FIREWARE, CAP_IEEE1394	IEEE 1394 드라이버
# CAP_DSHOW	다이렉트쇼(DirectShow)
# CAP_PVAPI	PvAPI, Prosilica GigE SDK
# CAP_OPENNI	OpenNI
# CAP_MSMF	마이크로소프트 미디어 파운데이션
# (Microsoft Media Foundation)
# CAP_GSTREAMER	GStreamer
# CAP_FFMPEG	FFMPEG 라이브러리
# CAPIMAGES	OpenCV에서 지원하는 일련의 영상 파일 (예) img%02d.jpg
# CAP_OPENCV_MJPEG	OpenCV에 내장된 MotionJPEG 코덱

class WebCam:
    def __init__(self, portNum=None):
        self.port_num = portNum

    ###################################################################
    # Get WebCam List
    ###################################################################
    def get_valid_camera_list(self, max_port_num=3):
        camera_port_list = []

        for index in range(max_port_num):
            cap = cv2.VideoCapture(index)
            ret, frame = cap.read()

            if ret is True and frame is not None:
                camera_port_list.append(index)
            else:
                break

        return camera_port_list

    ###################################################################
    # Set Port Number
    ###################################################################
    def set_port(self, portNum):
        self.port_num = portNum

    ###################################################################
    # Capture Webcam Image
    ###################################################################
    def capture_image(self, file_name, width=1280, height=720):
        # 웹캠 객체생성
        cap = cv2.VideoCapture(self.port_num, cv2.CAP_DSHOW) # Windows Directshow 사용

        # 웹캠 옵션설정
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

        # 카메라 이미지 캡쳐
        ret, frame = cap.read()

        # 캡쳐된 이미지를 파일로 저장
        if ret is True:
            ret = cv2.imwrite(file_name, frame)

        # 객체핸들 릴리즈
        cap.release()

        return ret, file_name

    ###################################################################
    # Capture Video Stream
    ###################################################################
    def capture_video(self, width=1280, height=720, isMono=False, flip=None):






if __name__ == '__main__':
    cam = WebCam()
    # port_list = cam.get_valid_camera_list()
    # ic(port_list)

    # 사용할 웹캠선택
    port_num = 0
    cam.set_port(port_num)

    ################################################################
    # Capture Image(Snapshot)
    ################################################################
    file_name = f'{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.png'
    ret, file_name = cam.capture_image(file_name)
    if ret is True:
        ic(file_name)
    else:
        ic('Capture is fail')




























