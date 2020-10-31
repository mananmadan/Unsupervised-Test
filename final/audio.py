import sounddevice as sd
from scipy.io.wavfile import write
import time

fs = 44100  # Sample rate
seconds = 2 * 60  # time duration of the test
try:
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
except:
    write('generated-report/output.wav', fs, myrecording)  # Save as WAV file 
