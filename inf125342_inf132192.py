from scipy.io.wavfile import read as scipy_read
from scipy.signal import decimate
import sys
import numpy as np
from scipy import *
from ipywidgets import *
import matplotlib.pyplot as plt
import warnings
import soundfile as sf 

if not sys.warnoptions:
    warnings.simplefilter("ignore")


def reco():
    try:
        signal, w = sf.read(sys.argv[1])

        if len(signal.shape) > 1:
            signal = [s[0] for s in signal]

        spectrum = signal
        length = len(spectrum)
        trip = int(len(spectrum)/3)
        spectrum = spectrum[trip: length-trip]

        # # basic voice plot
        # fig = plt.figure(figsize=(15, 6), dpi=80)   
        # plotnum = 811
        # ax = fig.add_subplot(plotnum)
        # ax.plot(spectrum, linestyle='-', color='red')
        # ax.set_ylim([min(spectrum), max(spectrum)])

        signal = np.fft.rfft(spectrum)
        signal = abs(signal)

        Decimated_signal_list = []
        for i in range(6):
            decimate_signal = decimate(signal, i+2)
            Decimated_signal_list.append(decimate_signal)
        
            # # show each signal on plot
            # plotnum += 1
            # ax = fig.add_subplot(plotnum)  
            # ax.set_xlim([0, 1000])
            # plt.plot(decimate_signal)

        sum = Decimated_signal_list[0][:300]
        for j in range(5):
            sum *= Decimated_signal_list[j][:300]

        # # show mulitiplied signal on plot
        # plotnum += 1
        # ax = fig.add_subplot(plotnum)
        # ax.set_xlim([0, 1000])
        # plt.plot(sum)
        # plt.show()

        j = list(sum).index(max(sum[50:]))
        # print(j)

        if (j < 195):
            return "M"
        else: 
            return "K"

    except ValueError:
        return "M"


print(reco())
