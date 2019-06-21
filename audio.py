import math        #import needed modules
import pyaudio     #sudo apt-get install python-pyaudio
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

#PARAMETROS 

# ESTE PROGRAMA NOS MUESTRA LOS SONIDOS QUE CREAMOS EN UNA GRAFICA EN TIEMPO REAL CON PYTHON 
#PRIMER PARAMETRO ES LA FRECUENCIA 
# SEGUNDO PARAMETRO EL BITRATE



# programa para poder sintetizar sonidos 
#desarrollado en python 2.7
# instalar 
  # apt install python-dev
  #apt install python-tk
  #





#pass for parameter the frecuency value



frecuency = str(sys.argv)

print "Frecuencia pasada es ",sys.argv[1]


PyAudio = pyaudio.PyAudio     #initialize pyaudio

#See https://en.wikipedia.org/wiki/Bit_rate#Audio
# BITRATE = 16000     #number of frames per second/frameset.      

BITRATE = int(sys.argv[2])


# FREQUENCY = 900     #Hz, waves per second, 261.63=C4-note.


FREQUENCY = int(sys.argv[1])

LENGTH = 1     #seconds to play sound

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"


if FREQUENCY > BITRATE:
    BITRATE = FREQUENCY+100

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''    

#generating wawes
for x in xrange(NUMBEROFFRAMES):
 WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

for x in xrange(RESTFRAMES): 
 WAVEDATA = WAVEDATA+chr(128)


fragmentos = []	

p = PyAudio()
stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = BITRATE, 
                output = True)

stream.write(WAVEDATA)
fragmentos.append(WAVEDATA)
stream.stop_stream()
stream.close()


waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(p.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(fragmentos))
waveFile.close()


#show something with the plot 



#plot de grafica radio


spf = wave.open('file.wav','r')

signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')


#If Stereo
# if spf.getnchannels() == 2:
#     print 'Just mono files'
#     sys.exit(0)

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(signal)
plt.show()

#Extract Raw Audio from Wav File



#plot de grafica sinoideal 

# Data for plotting












