import wave

from vosk import Model, KaldiRecognizer

def speech_to_text_vosk(filepath):
    wf = wave.open(filepath, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        return None

    model = Model(lang="nl")

    # You can also init model by name or with a folder path
    # model = Model(model_name="vosk-model-en-us-0.21")
    # model = Model("models/en")

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    rec.SetPartialWords(True)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            print(rec.Result())
        else:
            print(rec.PartialResult())

    return rec.FinalResult()