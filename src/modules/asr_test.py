from pathlib import Path

from asr_sr import speech_to_text

SAMPLE_JP_FILEPATH = Path(__file__).resolve().parent.parent / r'audio\samples\japanese_speech_sample.wav'
SAMPLE_EN_FILEPATH = Path(__file__).resolve().parent.parent / r'audio\samples\english_speech_sample.wav'

SAMPLE_NL_VLOEIEND = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_vloeiend.wav'
SAMPLE_NL_VLOEIEND2 = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_vloeiend2.wav'
SAMPLE_NL_LICHTESTOTTER = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_lichtestotter.wav'
SAMPLE_NL_ZWARESTOTTER = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_zwarestotter.wav'
SAMPLE_NL_ZWARESTOTTER2 = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_zwarestotter2.wav'

MODEL = 'sphinx'

if __name__ == '__main__':
    # test if ASR is up and running
    # print('Testing ASR on EN speech sample.')
    # print(f'Actual audio: Oh. Honestly, I could not be bothered to play this game to full completion.\n '
    #       f'The narrator is obnoxious and unfunny, with his humor and dialogue proving to be more irritating than entertaining.\n'
    #       f"Transcription: {speech_to_text(SAMPLE_EN_FILEPATH)}\n")

    # print('Testing ASR on JA speech sample.')
    # print(f'Actual translation: How is this dress? It suits you very well.\n'
    #       f"Transcription: {speech_to_text(SAMPLE_JP_FILEPATH, 'translate', 'ja')}\n")
    
    print('Testing ASR on NL speech sample.')
    print(f"Transcription: {speech_to_text(SAMPLE_NL_VLOEIEND, MODEL)}\n")
    
    print('Testing ASR on NL speech sample.')
    print(f"Transcription: {speech_to_text(SAMPLE_NL_VLOEIEND2, MODEL)}\n")
    
    # print('Testing ASR on NL speech sample.')
    # print(f"Transcription: {speech_to_text(SAMPLE_NL_LICHTESTOTTER)}\n")
    
    # print('Testing ASR on NL speech sample.')
    # print(f"Transcription: {speech_to_text(SAMPLE_NL_ZWARESTOTTER)}\n")
    
    # print('Testing ASR on NL speech sample.')
    # print(f"Transcription: {speech_to_text(SAMPLE_NL_ZWARESTOTTER2)}\n")
