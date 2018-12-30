from scipy.io.wavfile import read as scipy_read
from scipy.signal import decimate
import sys
import numpy as np
from scipy import *
from ipywidgets import *
import math as mt 
import matplotlib.pyplot as plt
import warnings

import soundfile as sf 

# show signal on 2 plots
# make n copies of fft signal
# decimate each signal: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.decimate.html
# multiply each decimation
# find x for y=argmax
# decide if male or female


if not sys.warnoptions:
    warnings.simplefilter("ignore")


# w, signal = scipy_read(sys.argv[1])
signal, w = sf.read(sys.argv[1])

if len(signal.shape) > 1:
    signal = [s[0] for s in signal]

#spectrum = signal[::10]
spectrum = signal 

fig = plt.figure(figsize=(15, 6), dpi=80)   
plotnum = 811
ax = fig.add_subplot(plotnum)

ax.plot(spectrum, linestyle='-', color='red')
ax.set_ylim([min(spectrum), max(spectrum)])
# --- 

signal = np.fft.fft(spectrum)
ffts = []
for i in range (5):
    signal = decimate(signal, 2, zero_phase=False)
    ffts.append(signal)
    #signal = signal[signal>0]
    #signal = abs(signal)

    
    plotnum += 1
    ax = fig.add_subplot(plotnum)  
    ax.set_xlim([0, 1000])

    plt.plot(signal)

    #multiply_signal *= signal
    #np.multiply(multiply_signal, signal)
sum = ffts[0][:1000]
for j in range(4):
    sum  *= ffts[j+1][:1000]

 
plotnum += 1
ax = fig.add_subplot(plotnum)
ax.set_xlim([0, 1000])
plt.plot(sum)

j = list(sum).index(max(sum))
print(j)
plt.show()


