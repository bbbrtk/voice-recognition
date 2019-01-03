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

length = len(spectrum)
trip = int(len(spectrum)/3)
spectrum = spectrum[trip: length-trip] #tylko 1/3 do 2/3 //środek


# basic voice plot
fig = plt.figure(figsize=(15, 6), dpi=80)   
plotnum = 811
ax = fig.add_subplot(plotnum)
ax.plot(spectrum, linestyle='-', color='red')
ax.set_ylim([min(spectrum), max(spectrum)])
# --- 

# decimate x7
signal = np.fft.rfft(spectrum)
Decimated_signal_list = []
for i in range(5):
    decimate_signal = decimate(signal, i+2)
    decimate_signal = abs(decimate_signal)
    Decimated_signal_list.append(decimate_signal)
    #signal = signal[signal>0]
    
    # show each decimiated signal on plot
    plotnum += 1
    ax = fig.add_subplot(plotnum)  
    ax.set_xlim([0, 1000])
    plt.plot(decimate_signal)


# multiply 7 signals    
sum = Decimated_signal_list[0][:1000]
for j in range(4):
    sum *= Decimated_signal_list[j][:1000]

# show mulitiplied signal on plot
plotnum += 1
ax = fig.add_subplot(plotnum)
ax.set_xlim([0, 1000])
plt.plot(sum)


j = list(sum).index(max(sum[50:300])) # get max peak from 50 to 500Hz
print(j)
print(w)

# show result
if (j < 175):
    print ("M")
else: 
    print ("K")

plt.show()


