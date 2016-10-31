import pyaudio
import numpy as np
import math
from matplotlib.mlab import find

chunk = 32
# CHUNK = 32
WIDTH = 2
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 30
FrequencyA = 0

p = pyaudio.PyAudio()

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

def Pitch(signal):
    signal = np.fromstring(signal, 'Int16');
    crossing = [math.copysign(1.0, s) for s in signal]
    index = find(np.diff(crossing));
    f0=round(len(index) *RATE /(2*np.prod(len(signal))))
    return f0;


stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=chunk)

print("* recording")

for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
    data = stream.read(chunk)
    Frequency=Pitch(data)
    FrequencyB = Frequency
    if abs(FrequencyB - FrequencyA) < 10: 
      print "%f Frequency" %Frequency
      # series.append(Frequency)
    FrequencyA = FrequencyB
    stream.write(data, chunk)


print("* done")

stream.stop_stream()
stream.close()

p.terminate()
