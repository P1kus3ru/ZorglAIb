import speech_recognition as sr
import time
from asr.whisper import speech_to_text_whisper
from asr.sphinx import speech_to_text_sphinx
from asr.google import speech_to_text_google
from asr.wit import speech_to_text_wit

def speech_to_text(filepath, model):
    start_time = time.time()
    match model:
        case 'sphinx':
            result = speech_to_text_sphinx(filepath)
        case 'google':
            result = speech_to_text_google(filepath)
        case 'wit':
            result = speech_to_text_wit(filepath)
        # case 'azure':
        #     result = speech_to_text_azure(filepath)
        # case 'bing':
        #     result = speech_to_text_bing(filepath)
        # case 'houndify':
        #     result = speech_to_text_houndify(filepath)
        # case 'ibm':
        #     result = speech_to_text_ibm(filepath)
        case _:
            result = speech_to_text_whisper(filepath)
    print("ASR took %.2f seconds" % (time.time() - start_time))
    return result
        
def speech_to_text_azure(filepath):
    
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(str(filepath)) as source:
        audio = r.record(source)  # read the entire audio file


    # recognize speech using Microsoft Azure Speech
    AZURE_SPEECH_KEY = "INSERT AZURE SPEECH API KEY HERE"  # Microsoft Speech API keys 32-character lowercase hexadecimal strings
    try:
        print("Microsoft Azure Speech thinks you said " + r.recognize_azure(audio, key=AZURE_SPEECH_KEY))
    except sr.UnknownValueError:
        print("Microsoft Azure Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Azure Speech service; {0}".format(e))

def speech_to_text_bing(filepath):
    
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(str(filepath)) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Microsoft Bing Voice Recognition
    BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
    try:
        print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

def speech_to_text_houndify(filepath):
    
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(str(filepath)) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Houndify
    HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"  # Houndify client IDs are Base64-encoded strings
    HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"  # Houndify client keys are Base64-encoded strings
    try:
        print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
    except sr.UnknownValueError:
        print("Houndify could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Houndify service; {0}".format(e))

def speech_to_text_ibm(filepath):
    
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(str(filepath)) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using IBM Speech to Text
    IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
    try:
        print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
    except sr.UnknownValueError:
        print("IBM Speech to Text could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from IBM Speech to Text service; {0}".format(e))