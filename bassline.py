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
    loopBassline = 0
    while loopBassline < 1:
        i = 1
        frequency = 250
        length = .20
        for i in range (70):
            lenght = .25
            if i > 95:
                length = 1
            play_tone(stream, frequency, length)
            lenght = .25
            change = random.randint(-50, 20)
            print frequency         
            if frequency < 0:
                frequency = 100 
            else:
                frequency = frequency + change
                # lChange = - 0.01
                # length = length +lChange

        i = 100
        while i < 500:
            play_tone(stream, i, 0.01)
            print i
            i +=1

        loopBassline += 1       

    # coffee is ready
    # Perfect! Save this! 350!
    j = 1
    while j < 5000:
        i = 100
        
        while i < 5000:
            play_tone(stream, i, .1)   
            print i
            i = math.tan(i) * 350
        j += 1


    # # makes a high pitch
    # size = 1000
    # while size < 1500:
    #     j = 1
    #     while j < 5:
    #         i = 100
    #         for i in range(-2000, 2000, 45):
    #             play_tone(stream, i, 0.005)   
    #             print i
    #             i = math.sin(i) * size
    #         j += 1
    #     size += 5

    # stream.close()
    # p.terminate()    

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=44100, output=1)


doit()



#     

# import numpy as np
# from scipy.io.wavfile import write

# data = np.random.uniform(-100,100,444100) # 44100 random samples between -1 and 1
# scaled = np.int16(data/np.max(np.abs(data)) * 32767)
# write('test.wav', 44100, scaled)

