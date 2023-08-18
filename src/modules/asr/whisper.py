from os import getenv


import requests
from dotenv import load_dotenv


load_dotenv()

BASE_URL = getenv('WHISPER_BASE_URL')
REQUEST_TIMEOUT = int(getenv('REQUEST_TIMEOUT'))
WHISPER_TASK = 'transcribe'
TARGET_LANGUAGE = getenv('TARGET_LANGUAGE')


def speech_to_text_whisper(filepath):
    try:
        with open(filepath, 'rb') as infile:
            files = {'audio_file': infile}
            r = requests.post(f'{BASE_URL}/asr?task={WHISPER_TASK}&language={TARGET_LANGUAGE}&output=json',
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

    return r.json()['text'].strip()