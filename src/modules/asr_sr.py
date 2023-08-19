import speech_recognition as sr
import time
from asr.whisper import speech_to_text_whisper
# from asr.sphinx import speech_to_text_sphinx
# from asr.vosk import speech_to_text_vosk
from asr.google import speech_to_text_google
from asr.azure import speech_to_text_azure

def speech_to_text(filepath, model):
    start_time = time.time()
    match model:
        # case 'sphinx':
        #     result = speech_to_text_sphinx(filepath)
        # case 'vosk':
        #     result = speech_to_text_vosk(filepath)
        case 'google':
            result = speech_to_text_google(filepath)
        case 'azure':
            result = speech_to_text_azure(filepath)
        case _:
            result = speech_to_text_whisper(filepath)
    print("ASR took %.2f seconds" % (time.time() - start_time))
    return result