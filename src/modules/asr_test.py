from pathlib import Path

from asr_sr import speech_to_text

SAMPLE_JP_FILEPATH = Path(__file__).resolve().parent.parent / r'audio\samples\japanese_speech_sample.wav'
SAMPLE_EN_FILEPATH = Path(__file__).resolve().parent.parent / r'audio\samples\english_speech_sample.wav'

SAMPLE_NL_VLOEIEND = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_vloeiend.wav'
SAMPLE_NL_VLOEIEND2 = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_vloeiend2.wav'
SAMPLE_NL_LICHTESTOTTER = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_lichtestotter.wav'
SAMPLE_NL_ZWARESTOTTER = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_zwarestotter.wav'
SAMPLE_NL_ZWARESTOTTER2 = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_zwarestotter2.wav'
SAMPLE_NL_HEELZWARESTOTTER  = Path(__file__).resolve().parent.parent / r'audio\samples\nederlands_sample_heelzwarestotter.wav'

MODEL = ''

if __name__ == '__main__':
    # test if ASR is up and running
    
    # print('Testing ASR on NL speech sample.')
    # print(f"Transcription: {speech_to_text(SAMPLE_NL_VLOEIEND, MODEL)}\n")
    
    # print('Testing ASR on NL speech sample.')
    # print(f"Transcription: {speech_to_text(SAMPLE_NL_VLOEIEND2, MODEL)}\n")
    
    # print('Testing ASR on NL speech sample.')
    # print(f"Transcription: {speech_to_text(SAMPLE_NL_LICHTESTOTTER, MODEL)}\n")
    
    # print('Testing ASR on NL speech sample.')
    # print(f"Transcription: {speech_to_text(SAMPLE_NL_ZWARESTOTTER, MODEL)}\n")
    
    # print('Testing ASR on NL speech sample.')
    # print(f"Transcription: {speech_to_text(SAMPLE_NL_ZWARESTOTTER2, MODEL)}\n")
    
    print('Testing ASR on NL speech sample.')
    print(f"Transcription: {speech_to_text(SAMPLE_NL_HEELZWARESTOTTER, MODEL)}\n")
