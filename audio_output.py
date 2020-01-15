from gtts import gTTS
import playsound

def ttsByGoogle(text):
    output_text = text

    tts = gTTS(text = output_text, lang = 'ko')
    tts.save("output_kr.mp3")

    playsound.playsound('output_kr.mp3', True)    #for Windows

if __name__ == '__main__':
    ttsByGoogle('')