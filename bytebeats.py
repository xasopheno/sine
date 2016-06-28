#!/usr/bin/python3
#   ByteBeats.py
 
import matplotlib.pyplot as pl
import pyaudio
from math import sin, pi
 
#   Initialise PyAudio
PyAudio = pyaudio.PyAudio       # error msgs are usually safe to ignore
pa = PyAudio()
audio = pa.open(format=pa.get_format_from_width(1),channels=1,rate=8000,output=True)
 
funcs = [
    't*2',
    't*5&t>>7|t*3&t>>10|t>>4',
    '127.5*sin(pi*t/50)+127.5',
    't*(t+(t>>9|t>>13))%40&120',
    '(t&t%255)-(t*3&t>>13&t>>6)',
    't*((t>>3|t>>13)&t>>6|t>>8)',
    't*4&(t>>10)|t*4&(t*6>>8)&t|64',
    '(t>>6|t|t>>(16))*10+((t>>11)&7)',
    't*(((t>>12)|(t>>8))&(63&(t>>4)))',
    't*(4|t*t&4<<t)*(t&(t>>9|t>>13)+1)',
    't*3&(t>>10)|t*12&(t>>10)|t*10&((t>>8)*55)&128',
        '(((t*5&t>>6)^(t>>4|t>>2&t%255|t*3&t>>8)-10)/4)',
    '(t*((15&t>>11)%12)&55-(t>>5|t>>12)|t*(t>>10)*32)-1'
          ]
stop = len(funcs)                       # number of functions
start = stop - 1                        # only playing the last one
start = 0                               # playing all
pls = 10000                             # number of samples to plot
aus = 100000                            # number of audio samples
#   Note that in this loop, we calculate the samples in 2 parts -
#   first those we want to plot, then the rest - so the plot is shown sooner
 
for i in range(start,stop):             # for a range of functions:
    f = funcs[i]                            # select a function
    x = [x for x in range(aus)]             # compute x range
    y = [int(eval(f)%256) for t in x[:pls]]   # only what's needed for plot
 
    pl.figure(figsize=(15,10))                  # set the plot size
    pl.title(f)
    pl.plot(x[:pls],y)
    pl.show(block=False)
 
    y[pls:] = [int(eval(f)%256) for t in x[pls:]]   # now the rest...
    for v in y:                                 # for all y
        # replace with print(...,end='') if no pyaudio
        audio.write(chr(v))                     # convert to 8-bit
 
input("Press Enter")