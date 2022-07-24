import speech_recognition as s_r
import pyaudio


def record():
    r = s_r.Recognizer()
    with s_r.Microphone(device_index = 1) as source:
        print("say something")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.7)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language = "ru-RU")
        print(f"you say: {query}")
    except:
        pass

while True:
    record()


