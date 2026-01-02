import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

def speak(text):
    engine = pyttsx3.init()   # re-initialize every time (IMPORTANT)
    engine.setProperty('rate', 170)
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=2)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            return ""

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""

# Greeting
speak("Hello, I am your voice assistant")

# Main loop
while True:
    command = listen()

    if command == "":
        continue

    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {date}")

    elif "open notepad" in command:
        speak("Opening notepad")
        os.system("notepad")

    elif "open calculator" in command:
        speak("Opening calculator")
        os.system("calc")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        break

