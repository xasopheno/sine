#!/usr/bin/env python
import Queue
import threading
import time

import pyaudio
import numpy as np
import math
from scipy.fftpack import fft, ifft

from matplotlib.mlab import find
import matplotlib.pyplot as plt

queue = Queue.Queue()

chunk = 1024
FORMAT = pyaudio.paInt32
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5


def Pitch(signal):
    signal = np.fromstring(signal, 'Int32');
    crossing = [math.copysign(1.0, s) for s in signal]
    index = find(np.diff(crossing));
    f0=round(len(index) *RATE /(2*np.prod(len(signal))))
    return f0;

def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return np.sin(np.arange(length) * factor)

def play_tone(stream, frequency, length, rate=44100):
    chunks = []
    chunks.append(sine(frequency, length, rate))

    chunk = np.concatenate(chunks) * 0.25

    stream.write(chunk.astype(np.float32).tostring()) 
p1 = pyaudio.PyAudio()
# p2 = pyaudio.PyAudio()

stream = p1.open(format = FORMAT,
channels = CHANNELS,
rate = RATE,
input = True,
output = True,
frames_per_buffer = chunk)
FrequencyA = 0

series = [0]

for i in range(0, RATE / chunk * RECORD_SECONDS):
    data = stream.read(chunk)
    Frequency=Pitch(data)
    if Frequency == 0:
        Frequency = 1
    FrequencyB = Frequency
    if abs(FrequencyB - FrequencyA) < 20: 
      print "%f Frequency" %Frequency
      series.append(Frequency)
    # else:
    #   print "0"
    #   series.append(0)
    #   # series.append(Frequency-(11*Frequency/8))
    #   # series.append(Frequency-(3*Frequency/2))
    #   # series.append(Frequency-(2*Frequency))
    #   test = Frequency
      # while test > 0:
      #     series.append(test)
      #     test = test - 50
    FrequencyA = FrequencyB

# N = 50
# T = 1.0 / 800.0
# series = fft(series)
# series = 2.0/N * np.abs(series[0:N/2])


outputStream = p1.open(format=pyaudio.paFloat32,
                channels=1, rate=44100, output=1)

class ThreadPitch(threading.Thread):
    """Threaded frequency grab"""
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue  

    def run(self):
        while True:
          #grabs host from queue
            host = self.queue.get()
       
          #grabs urls of hosts and prints first 1024 bytes of page
            for freq in series:
                host = freq
                print host
                play_tone(outputStream, host, 0.025) 
                # play_tone(outputStream, host * 3/2, 0.1) 

                
       
          #signals to queue job is done
            self.queue.task_done()  

def main():

#spawn a pool of threads, and pass them queue instance 
    for i in range(3):
        t = ThreadPitch(queue)
        t.setDaemon(True)
        t.start()

    
    queue.put(series)

main()
plt.plot(series)
plt.show()

p1.terminate()

# series = [0]

# for i in range(0, RATE / chunk * RECORD_SECONDS):
#     data = stream.read(chunk)
#     Frequency=Pitch(data)
#     FrequencyB = Frequency
#     if abs(FrequencyB - FrequencyA) < 10: 
#       print "%f Frequency" %Frequency
#       series.append(Frequency)
#     FrequencyA = FrequencyB

# for i in series:
#     print i

    
