import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something:")
    r.adjust_for_ambient_noise(source, duration=2)
    try:
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    except sr.WaitTimeoutError:
        print("Listening timed out, try again")
        exit()

try:
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError:
    print("Could not request results; check internet")
