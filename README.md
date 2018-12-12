biosignalprocessing.py
This code is used to run biosignals such as EMG and ECG
The modules that are required to be imported inlcude numpy, matplotlib.lib, ecg submodule and emg submodule. The following are the lines of code that demonstrate the same:
import numpy as np
from biosppy import storage
from biosppy.signals import ecg
import matplotlib.pyplot as plt
from biosppy.signals import emg
The final output would be the raw signal that gets filtered out along with QRS complex and provides the heart beat rate in the case of ECG and the muscle activity rate in the case of EMG. 
