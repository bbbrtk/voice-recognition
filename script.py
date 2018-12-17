from scipy.io.wavfile import read as scipy_read
from scipy.signal import decimate
import sys
import numpy as np
from scipy import *
from ipywidgets import *
import math as mt 
import matplotlib.pyplot as plt

def myFunction(A=1, LP=1, w=50, f=2.0):
    
#   w = 2678400
    T = 1.0/f        
    # Okres sygnaku [s] (jak dkugo trwa jeden przebieg sinusa)

#     TW = 1.0/w 
    TW = 2678400
    w = 1.0/TW
    # Okres probkowania [s] (co ile sekund pobieramy

    t = np.arange(0, LP*T, TW)
    # generujemy momenty, w ktorych pobieramy proki

    #signal = array=[float(x) for x in open('spots.txt').read().split()] 
    w, signal = scipy_read(sys.argv[1])
    signal = [s[0] for s in signal]            
    # funkcja sprobkowana
    
    n = len(signal)
    
    
    fig = plt.figure(figsize=(15, 6), dpi=80)   
    ax = fig.add_subplot(121)
    ## --- POMOCNICZY SYGNAL
    base_t = np.arange(0, n, 1)
    base_signal = signal
    ax.plot(base_t, base_signal, linestyle='-', color='red')
    ax.set_ylim([min(base_signal), max(base_signal)])
    ## --- 
#     ax.plot(t, signal, 'o')

    signal1 = fft(signal)
    # sygnal w dziedzinie czestotliwosci 
    signal1 = abs(signal1)        
    # modul sygnalu

    freqs = np.arange(0,w,w/n)


    ax = fig.add_subplot(122)
    ymax = max(signal1)
    if (ymax > 3.0):
        ax.set_ylim([0.0,ymax])
    plt.stem(freqs, signal1, '-*')
    ax.set_xlabel('[Hz]')
    plt.show()
    
    tempx = (argmax(signal1[1:])+1) * w/n
    tempx = 1.0/tempx / 2678400.0 / 12.0
    print(tempx)
    
myFunction()


print("_start")
w, signal = scipy_read(sys.argv[1])
signal = [s[0] for s in signal]

# show signal on 2 plots
# make n copies of fft signal
# decimate each signal: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.decimate.html
# multiply each decimation
# find x for y=argmax
# decide if male or female


answer = "K"
print(answer)