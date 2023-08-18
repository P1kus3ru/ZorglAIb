import speech_recognition as sr

def speech_to_text_wit(filepath):
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(str(filepath)) as source:
        audio = r.record(source)  # read the entire audio file

    # # recognize speech using Wit.ai
    # WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"  # Wit.ai keys are 32-character uppercase alphanumeric strings
    # try:
    #     print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
    # except sr.UnknownValueError:
    #     print("Wit.ai could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from Wit.ai service; {0}".format(e))
