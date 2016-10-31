#!/usr/bin/python
import math
import numpy
import pyaudio
from os import system
import random


def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)


def play_tone(stream, frequency, length, rate=44100):
    chunks = []
    chunks.append(sine(frequency, length, rate))

    chunk = numpy.concatenate(chunks) * 0.25

    stream.write(chunk.astype(numpy.float32).tostring()) 

def doit():  
    i = 1
    frequency = 100
    length = .25
    for i in range (100):
        play_tone(stream, frequency, length)
        change = random.randint(-50, 20)
        print frequency         
        if frequency < 0:
            frequency = 100 
        else:
            frequency = frequency + change
            # lChange = - 0.01
            # length = length +lChange

    stream.close()
    p.terminate()    

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=44100, output=1)


doit()
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1, rate=44100, output=1)



#     

# import numpy as np
# from scipy.io.wavfile import write

# data = np.random.uniform(-100,100,444100) # 44100 random samples between -1 and 1
# scaled = np.int16(data/np.max(np.abs(data)) * 32767)
# write('test.wav', 44100, scaled)

