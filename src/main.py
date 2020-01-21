from __future__ import print_function
from similarity import *
# import RPi.GPIO as GPIO
# from ctypes import *
from audio_input_speech_recognition import speechRecognitionByGoogle
# import audioop
# import MicrophoneStream as MS
from audio_output import ttsByGoogle
from mysql_ReadQuery import mysqlQuery
from answers import *
from functionsToFind import *


# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
# GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(31, GPIO.OUT)
# btn_status = False
#
#
# def callback(channel):
#     print("falling edge detected from pin {}".format(channel))
#     global btn_status
#     btn_status = True
#     print(btn_status)
#
#
# GPIO.add_event_detect(29, GPIO.FALLING, callback=callback, bouncetime=10)
# ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)


def checkQueryNum(input_text):
    query_data = mysqlQuery()
    if query_data is None:
        return None
    elif input_text == '000':
        return None
    else:
        max_sim = 0
        max_query_num = 0
        max_query = ''
        for query_num, query in query_data:
            if max_sim < sim(input_text, query):
                max_sim = sim(input_text, query)
                max_query_num = query_num
                max_query = query
        print(max_query_num, max_query)
        if max_sim > 0.5:
            return max_query_num
        else:
            return None


def runAISpeaker():
    #global btn_status
    if True:
        input_txt = speechRecognitionByGoogle()
        query_num = checkQueryNum(input_txt)
        if query_num is None:
            ttsByGoogle('죄송해요, 다시 물어봐주세요.')
            return
        else:
            noun_list = get_noun(input_txt)
            dpt, new_nouns = get_department(noun_list)
            name = get_name_only(new_nouns)
            if name is None:
                ttsByGoogle('죄송해요, 잘 못 알아들었어요.')
                return
            if query_num == 10001:
                result = ANS_10001(name)
            elif query_num == 10002:
                result = ANS_10002(name)
            elif query_num == 10003:
                result = ANS_10003(name)
            elif query_num == 10004:
                result = ANS_10004(name)
            elif query_num == 10005:
                result = ANS_10005(name, dpt)
            elif query_num == 20001:
                result = ANS_20001()
            else:
                result = '아직 지원하지 않는 기능입니다.'
            ttsByGoogle(result)
        #btn_status = False


def main():
    while True:
        runAISpeaker()


if __name__ == '__main__':
    main()
