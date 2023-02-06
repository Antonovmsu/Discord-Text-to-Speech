import gtts  
from pydub import AudioSegment
import sounddevice as sd
import soundfile as sf

def say(text):
    # make a request to google to get synthesis 
    txt = text
    t1 = gtts.gTTS(text = txt ,lang = 'ru', slow = False)
    t1.save("tmp.mp3")

    sound = AudioSegment.from_mp3("tmp.mp3")
    sound.export("tmp.wav", format="wav")

    #5 с наушниками
    sd.default.device = 5

    filename = 'tmp.wav'
    # Extract data and sampling rate from file
    data, fs = sf.read(filename)  
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing

while True:
    text = input('Сказать:')
    say(text)