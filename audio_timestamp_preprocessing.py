from time import time
import wave
obj= wave.open("sample_long.wav","rb")
print(obj)
print("number of channels",obj.getnchannels())
print("width",obj.getsampwidth())
print("frame rate",obj.getframerate())
print("number of frames",obj.getnframes())
print("parameters",obj.getparams())

t_audio= obj.getnframes()/ obj.getframerate()
print("Time of the audio is :",t_audio)
frames=obj.readframes(-1)
print(type(frames),type(frames[0]))
print(len(frames))

obj_new=wave.open("smaple_new.wav","wb")
obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(44100)
obj_new.writeframes(frames)

obj_new.close(
