from pydub import AudioSegment
from pydub.silence import detect_nonsilent

#adjust target amplitude
def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

#Convert wav to audio_segment
audio_segment = AudioSegment.from_wav("sample_long.wav")

#normalize audio_segment to -20dBFS 
normalized_sound = match_target_amplitude(audio_segment, -20.0)
print("length of audio_segment={} seconds".format(len(normalized_sound)/1000))

#Print detected non-silent chunks, which in our case would be spoken words.
nonsilent_data = detect_nonsilent(normalized_sound, min_silence_len=500, silence_thresh=-20, seek_step=1)

#convert ms to seconds
print("start,Stop")
for chunks in nonsilent_data:
    print( [chunk/1000 for chunk in chunks])
