import speech_recognition as sr
from os import path


AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "sample_long.wav")
#print(AUDIO_FILE)
r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.listen(source)
    print("")
    try:
        print("Sphinx thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
#Accuracy Very Baaaaaaaad
