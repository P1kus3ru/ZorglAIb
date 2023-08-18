import speech_recognition as sr

def speech_to_text_sphinx(filepath):
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(str(filepath)) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Sphinx
    try:
        return r.recognize_sphinx(audio, language="nl")
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))