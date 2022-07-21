import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq

import wave, sys

def visualise (path):
    raw = wave.open(path)

    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype="int16")

    f_rate = raw.getframerate()

    time = np.linspace(0, len(signal) / f_rate, num = len(signal))

    print(len(signal))

    N = f_rate * len(signal)
    yf = fft(signal)
    xf = fftfreq(len(signal), 1 / f_rate)

    plt.figure(1)
    plt.title("Amplitude")
    plt.xlabel("Frequency")
    plt.xlim(0, 1000)
    plt.plot(xf, yf)
    plt.show()

visualise("rec.wav")
