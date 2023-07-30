import speech_recognition as sr
import moviepy.editor as mp
import os
import ffmpy
r = sr.Recognizer()

inputdir = 'C:\\Users\\inhor\\Downloads\\Python_Projects\\yt-transcript\\video'
outputdir = 'C:\\Users\\inhor\\Downloads\\Python_Projects\\yt-transcript'
for filename in os.listdir(inputdir):
    actual_filename = filename[:-4]
    if(filename.endswith(".mp4")):
        os.system('ffmpeg -i {}/{} -acodec pcm_s16le -ar 16000 {}/{}.wav'.format(inputdir, filename, outputdir, actual_filename))
    else:
        continue


for filenmae in os.listdir(outputdir):
    hellow=sr.AudioFile(filename)
    with hellow as source:
        audio = r.record(source)
    try:
        s = r.recognize_google(audio)
        print("Text: "+s)
    except Exception as e:
        print("Exception: "+str(e))