from __future__ import print_function
from similarity import *
import RPi.GPIO as GPIO
from ctypes import *
from audio_input_speech_recognition import speechRecognitionByGoogle
import audioop
import MicrophoneStream as MS
from audio_output import ttsByGoogle


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(31, GPIO.OUT)
btn_status = False

def callback(channel):
    print("falling edge detected from pin {}".format(channel))
    global btn_status
    btn_status = True
    print(btn_status)

GPIO.add_event_detect(29, GPIO.FALLING, callback=callback, bouncetime=10)
ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def runAISpeaker():
    global btn_status
    if btn_status == True:
        input_txt = speechRecognitionByGoogle()
        query_list = []
        if input_txt == '000':
            ttsByGoogle('죄송해요, 다시 물어봐주세요.')

        else:
            res_txt = func()
            ttsByGoogle(res_txt)
        btn_status = False

def main():
    runAISpeaker()

if __name__ == '__main__':
    main()