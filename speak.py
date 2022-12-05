import pyttsx3


class Speak:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 160)
        self.engine.setProperty('volume', 0.8)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
