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

signal, w = sf.read(sys.argv[1])

# get first canal if more than 1
if len(signal.shape) > 1:
    signal = [s[0] for s in signal]

spectrum = signal 

# basic voice plot
fig = plt.figure(figsize=(15, 6), dpi=80)   
plotnum = 811
ax = fig.add_subplot(plotnum)
ax.plot(spectrum, linestyle='-', color='red')
ax.set_ylim([min(spectrum), max(spectrum)])
# --- 

# decimate x7
signal = np.fft.fft(spectrum)
ffts = []
for i in range (6):
    decimate_signal = decimate(signal, i+2)
    decimate_signal = abs(decimate_signal)
    ffts.append(decimate_signal)
    #signal = signal[signal>0]
    
    # show each decimiated signal on plot
    plotnum += 1
    ax = fig.add_subplot(plotnum)  
    ax.set_xlim([0, 1000])
    plt.plot(decimate_signal)


# multiply 7 signals    
sum = ffts[0][:1000]
for j in range(5):
    sum  *= ffts[j+1][:1000]

# show mulitiplied signal on plot
plotnum += 1
ax = fig.add_subplot(plotnum)
ax.set_xlim([0, 1000])
plt.plot(sum)


j = list(sum).index(max(sum[50:500])) # get max peak from 50 to 500Hz
print(j)

# show result
if (j < 200): 
    print ("M")
else: 
    print ("K")

plt.show()


