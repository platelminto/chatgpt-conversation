#!/usr/bin/env python3
import time

import speech_recognition as sr


class SpeechRecognizer:
    def __init__(self, ambient_duration=2):
        self.recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=ambient_duration)

    def listen(self, model="base.en"):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)

        try:
            t = time.time()
            text = self.recognizer.recognize_whisper(audio, language="english", model=model)
            time_parsing = time.time() - t
            if time_parsing > 2:
                print(f"Recognized in {time.time() - t} seconds - maybe try using a small model. "
                      f"See https://github.com/openai/whisper#available-models-and-languages.")

            return text

        except sr.UnknownValueError:
            print("Whisper could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Whisper")
