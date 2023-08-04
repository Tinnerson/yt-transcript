import speech_recognition as sr
import moviepy.editor as mp
import os
import ffmpy
import time
from io import BufferedReader

import soundfile
data, samplerate = soundfile.read('ENG_M.wav')
soundfile.write('new.wav', data, samplerate, subtype='PCM_16')

def convert_audio(path: str = None,
                  convert: str = 'wav',
                  stream: BufferedReader = None) -> dict:
    error_message = None

    try:
        _audio = AudioSegment.from_file_using_temporary_files(stream) \
            if stream else AudioSegment.from_file(path)
    except FileNotFoundError as error:
        error_message = 'Audio file was not found (convert audio)'

        logging.exception(error_message)

        return dict(error=error_message)
    except Exception as error:
        error_message = 'Unexpected error when open audio file (convert audio)'

        logging.exception(error_message)

        return dict(error=error_message)

    audio_converted = _audio.export(format=convert)

    audio_converted.seek(0)

    return dict(
        audio=_audio,
        audio_converted=audio_converted,
        error=error_message
    )


def audio(path: str = None,
          stream: BufferedReader = None) -> dict:
    recognizer = speech_recognition.Recognizer()

    error_message = None

    try:
        _ = convert_audio(
            stream=stream) if stream else convert_audio(path=path)

        if _.get('error'):
            error_message = _.get('error')

            logging.exception(error_message)

            return dict(error=error_message)

        _audio = _.get('audio_converted')

        with speech_recognition.AudioFile(_audio) as file:
            _audio = recognizer.record(file)
    except FileNotFoundError as error:
        error_message = 'Audio file was not found (audio)'

        logging.exception(error_message)

        return dict(error=error_message)
    except Exception as error:
        error_message = 'Unexpected error when open audio file (audio)'

        logging.exception(error_message)

        return dict(error=error_message)

    text_sphinx = recognizer.recognize_sphinx(_audio)

    return dict(
        text=text_sphinx,
        error=error_message
    )
