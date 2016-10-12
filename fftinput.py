from matplotlib.mlab import find
import pyaudio
import numpy as np
import math


chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
RECORD_SECONDS = 5


def Pitch(signal):
    signal = np.fromstring(signal, 'Int16');
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
    FrequencyB = Frequency
    if abs(FrequencyB - FrequencyA) < 10: 
      print "%f Frequency" %Frequency
      series.append(Frequency)
    FrequencyA = FrequencyB

outputStream = p1.open(format=pyaudio.paFloat32,
                channels=1, rate=44100, output=1)
for i in series:
    play_tone(outputStream, i, 0.05)

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

    
