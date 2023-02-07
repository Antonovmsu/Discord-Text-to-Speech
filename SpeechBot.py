import gtts  
from pydub import AudioSegment
import sounddevice as sd
import soundfile as sf

def say(text: str, lang = 'ru'):
    # make a request to google to get synthesis 
    t1 = gtts.gTTS(text = text ,lang = lang, slow = False)
    t1.save("tmp.mp3")

    sound = AudioSegment.from_mp3("tmp.mp3")
    sound.export("tmp.wav", format="wav")

    # Extract data and sampling rate from file
    data, fs = sf.read('tmp.wav')  
    sd.play(data, fs)
    sd.wait()  #Wait until file is done playing

def specify_id():
    #do while
    while True:
        device_id = input("Enter the device id:")
        try:
            sd.default.device = int(device_id)
            break
        except ValueError:
            print("Your id is not an integer!")
        except:
            print("Somthing went wrong, try again")

def main():
    print("Choose your virtual output:")
    print(sd.query_devices(),"\n")

    specify_id()

    print('''\nType "exit" to stop program\n''')
    while True:
        text = input('Say: ')
        if text != 'exit':
            try:
                say(text)
            except sd.PortAudioError:
                print("\nYou've choosed the wrong device!")
                specify_id()
            except:
                print("Somthing went wrong, try again")
        else:
            break

if __name__ == "__main__":
    main()