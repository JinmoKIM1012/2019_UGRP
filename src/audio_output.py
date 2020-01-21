# -*- coding: utf-8 -*-
from gtts import gTTS
import playsound
import os


def ttsByGoogle(text):
    output_text = text

    tts = gTTS(text=output_text, lang='ko')
    tts.save("output_kr.mp3")

    playsound.playsound('output_kr.mp3', True)  # for Windows
    os.remove('output_kr.mp3')


if __name__ == '__main__':
    ttsByGoogle('죄송해요, 알아듣지 못했어요.')
