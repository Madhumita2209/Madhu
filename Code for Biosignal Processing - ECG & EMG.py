import numpy as np
from biosppy import storage
from biosppy.signals import ecg
import matplotlib.pyplot as plt
from biosppy.signals import emg


signal, mdata = storage.load_txt('ecgsignal.txt')
#Fs = mdata['sampling_rate']
Fs= int(input('What is the operating frequency?'))
if (Fs > 1500):
    print('Tachycardia')
elif (Fs <1000):
    print('Bradycardia')
else:
    print('Normal Heart Beat');
N = len(signal) # number of samples
T = (N - 1) / Fs # duration
ts = np.linspace(0, T, N, endpoint=False) # relative timestamps
plt.figure(1)
plt.plot(ts, signal, lw=2)
plt.xlabel('Time(s)');
plt.ylabel('Amplitude');
plt.title('Raw ECG Signal')
plt.grid()
plt.show()

signal, mdata = storage.load_txt('ecgsignal.txt')
out = ecg.ecg(signal=signal, sampling_rate=Fs, show=True)


#EMG Signal coding
signal2, mdata2 = storage.load_txt('emg.txt')
#Fs2 = mdata['sampling_rate']
Fs2= int(input('What is the operating frequency?'))
N2 = len(signal2) # number of samples
T2 = (N2 - 1) / Fs2 # duration
ts2 = np.linspace(0, T2, N2, endpoint=False) # relative timestamps
plt.figure(2)
plt.plot(ts2, signal2, lw=2)
plt.grid()
plt.xlabel('Time(s)');
plt.ylabel('Amplitude');
plt.title('Raw EMG Signal')
plt.show()

outputemg = emg.emg(signal=signal2, sampling_rate=Fs2, show=True)





