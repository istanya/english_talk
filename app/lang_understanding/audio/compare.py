from resemblyzer import VoiceEncoder
import numpy as np
import glob
import librosa

encoder = VoiceEncoder()

def compare_audio(audio1, audio2):
    wav_fpaths = glob.glob('~/aud/*.mp3', recursive=True)
    lib_a = librosa.load(wav_fpaths[0])
    lib_b = librosa.load(wav_fpaths[1])
    embeds_a = np.array([encoder.embed_utterance(lib_a[0])])
    embeds_b = np.array([encoder.embed_utterance(lib_b[0])])
    spk_sim_matrix = np.inner(embeds_a, embeds_b)[0]
    return spk_sim_matrix
