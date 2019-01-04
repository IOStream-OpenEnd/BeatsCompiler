import librosa                                  # Updated for making program short and understandable
def beat_dect(audio):
    x, sr = librosa.load(audio)
    tempo, beat_times = librosa.beat.beat_track(x, sr=sr, start_bpm=120, units='time')
    lst = beat_times.tolist()                   # Converts the array into a simple list
    rnd_lst = [round(items ,3) for items in lst]# For rounding off float upto 3 digits
    
    
    return(rnd_lst)
    
