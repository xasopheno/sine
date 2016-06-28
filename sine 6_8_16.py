#! /usr/bin/python

import math
import numpy
import pyaudio


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
    length = .04
    length2 = .08
    while i < 40:
        while frequency < 2800:
            play_tone(stream, frequency, length)
            frequency = float(frequency) * (math.pi * 2) /4.5
            length += .0005
            print length
            print frequency
        while frequency > 250:
            play_tone(stream, frequency, length2) 
            frequency = float(frequency) * (math.pi * 2) /8.5
            length2 -= .0005
            print frequency
        i += 1
        print i
    play_tone(stream, 2200, .5)
    play_tone(stream, 1500, .5)
    play_tone(stream, 888, 1)
    play_tone(stream, 2000, .5)
    play_tone(stream, 1200, .5)
    play_tone(stream, 488, 1)
    play_tone(stream, 200, 8)

    stream.close()
    p.terminate()

def doit2():    
    i = 1
    frequency = 100
    length = .04
    length2 = .08
    while i < 3:
        frequency = 100
        length = .04
        while frequency < 1.18804829839e+40:
            play_tone(stream, frequency, length)
            frequency = float(frequency) * (math.pi * 2) /3.5
            length += .0005
            # print length
            print frequency         
        print i     
        # while frequency > 1.18804829839e+30:
        #     play_tone(stream, frequency, length2) 
        #     frequency = float(frequency) * (math.pi * -2) /3.5
        #     length2 -= .0005
        #     print frequency  
        play_tone(stream, 200, 5)  
        i += 1

    stream.close()
    p.terminate()    

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=44100, output=1)


doit2()
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1, rate=44100, output=1)

doit()
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1, rate=44100, output=1)

doit2()

    