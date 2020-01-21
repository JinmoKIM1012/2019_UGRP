import speech_recognition as sr
import playsound

def speechRecognitionByGoogle():
    speechRecognition = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print('Recording...')
        playsound.playsound('turnon.mp3')
        audio = speechRecognition.listen(source, 8.0)
        print('Stop Recording')
    try:
        res = speechRecognition.recognize_google(audio, language='ko-KR')
        print(res)
        return res
    except sr.UnknownValueError as e:
        print('Error Occured!\n')
        return '000'


if __name__ == '__main__':
    speechRecognitionByGoogle()