import speech_recognition as sr

def speech_to_text_azure(filepath):
    
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(str(filepath)) as source:
        audio = r.record(source)  # read the entire audio file


    # recognize speech using Microsoft Azure Speech
    AZURE_SPEECH_KEY = "b80df333b049490aa879bef385ef6bb5"  # Microsoft Speech API keys 32-character lowercase hexadecimal strings
    try:
        return r.recognize_azure(audio, key=AZURE_SPEECH_KEY, language="nl-NL", location="westeurope")[0]
    except sr.UnknownValueError:
        print("Microsoft Azure Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Azure Speech service; {0}".format(e))
