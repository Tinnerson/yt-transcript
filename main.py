import speech_recognition as sr
from pydub import AudioSegment
import os

video = AudioSegment.from_file("video.mp4", format="mp4")
audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2)
audio.export("audio.wav", format="wav")

r = sr.Recognizer()

with sr.AudioFile("audio.wav") as source:
    audio_text = r.record(source)

text = r.recognize_google(audio_text, language='en-US')

file_name = "transcription.txt"

with open(file_name, "w") as file:
    file.write(text)
os.system(f"start {file_name}")
