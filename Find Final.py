import librosa
import numpy as np
import IPython.display as ipd
from scipy.io.wavfile import write

#help(librosa.beat)
print(format('.............This is a program used for beat detection................','^40'))
#reding the audio
y, sr = librosa.load('C:\\Users\\ayush\\Downloads\\sample.wav')
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
l = len(beats)
librosa.frames_to_time(beats, sr=sr)
onset_env = librosa.onset.onset_strength(y , sr=sr , aggregate=np.median)
tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env,sr=sr)
tempo
#creating the graph
import matplotlib.pyplot as plt
hop_length = 512
plt.figure(figsize=(8, 4))
times = librosa.frames_to_time(np.arange(len(onset_env)),sr=sr, hop_length=hop_length)
plt.plot(times, librosa.util.normalize(onset_env),label='Onset strength')
plt.vlines(times[beats], 0, 1, alpha=0.5, color='r',linestyle='--', label='Beats')
plt.legend(frameon=True, framealpha=0.75)
# Limit the plot to a 15-second window
plt.xlim(15, 30)
plt.gca().xaxis.set_major_formatter(librosa.display.TimeFormatter())
plt.tight_layout()

#output
scaled = np.int16(beats/np.max(np.abs(beats)) * 32767)
write('test.wav', l, scaled)