import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
  
fs = 44100
duration = 30
  
sd.default.samplerate = fs
sd.default.channels = 2
 
# start recording 
myrecording = sd.rec(int(duration * fs))

# wait for the recording to finish 
sd.wait()
 
# save recording
write("recording.wav", fs, myrecording)