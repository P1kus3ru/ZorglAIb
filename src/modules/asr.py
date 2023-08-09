from os import getenv
from pathlib import Path

import requests
from dotenv import load_dotenv

import time

load_dotenv()

BASE_URL = getenv('WHISPER_BASE_URL')
REQUEST_TIMEOUT = int(getenv('REQUEST_TIMEOUT'))
SAMPLE_JP_FILEPATH = Path(__file__).resolve().parent.parent / r'audio\samples\japanese_speech_sample.wav'
SAMPLE_EN_FILEPATH = Path(__file__).resolve().parent.parent / r'audio\samples\english_speech_sample.wav'

SAMPLE_NL_VLOEIEND = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_vloeiend.wav'
SAMPLE_NL_VLOEIEND2 = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_vloeiend2.wav'
SAMPLE_NL_LICHTESTOTTER = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_lichtestotter.wav'
SAMPLE_NL_ZWARESTOTTER = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_zwarestotter.wav'
SAMPLE_NL_ZWARESTOTTER2 = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_zwarestotter2.wav'


def speech_to_text(filepath, task, language):
    start_time = time.time()
    try:
        with open(filepath, 'rb') as infile:
            files = {'audio_file': infile}
            r = requests.post(f'{BASE_URL}/asr?task={task}&language={language}&output=json',
                              files=files,
                              timeout=REQUEST_TIMEOUT)

        if r.status_code == 404:
            print('Unable to reach Whisper, ensure that it is running, or the WHISPER_BASE_URL variable is set correctly')
            return None

    except requests.exceptions.Timeout:
        print('Request timeout')
        return None

    except Exception as e:
        print(f'An unknown error has occurred: {e}')
        return None

    print("ASR took %.2f seconds" % (time.time() - start_time))
    return r.json()['text'].strip()


if __name__ == '__main__':
    # test if ASR is up and running
    # print('Testing ASR on EN speech sample.')
    # print(f'Actual audio: Oh. Honestly, I could not be bothered to play this game to full completion.\n '
    #       f'The narrator is obnoxious and unfunny, with his humor and dialogue proving to be more irritating than entertaining.\n'
    #       f"Whisper audio: {speech_to_text(SAMPLE_EN_FILEPATH, 'transcribe', 'en')}\n")

    # print('Testing ASR on JA speech sample.')
    # print(f'Actual translation: How is this dress? It suits you very well.\n'
    #       f"Whisper translation: {speech_to_text(SAMPLE_JP_FILEPATH, 'translate', 'ja')}\n")
    
    # print('Testing ASR on NL speech sample.')
    # print(f"Whisper audio: {speech_to_text(SAMPLE_NL_VLOEIEND, 'transcribe', 'nl')}\n")
    
    # print('Testing ASR on NL speech sample.')
    # print(f"Whisper audio: {speech_to_text(SAMPLE_NL_VLOEIEND2, 'transcribe', 'nl')}\n")
    
    # print('Testing ASR on NL speech sample.')
    # print(f"Whisper audio: {speech_to_text(SAMPLE_NL_LICHTESTOTTER, 'transcribe', 'nl')}\n")
    
    # print('Testing ASR on NL speech sample.')
    # print(f"Whisper audio: {speech_to_text(SAMPLE_NL_ZWARESTOTTER, 'transcribe', 'nl')}\n")
    
    print('Testing ASR on NL speech sample.')
    print(f"Whisper audio: {speech_to_text(SAMPLE_NL_ZWARESTOTTER2, 'transcribe', 'nl')}\n")
