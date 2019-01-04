## Sample code which can cut video files according to video length given in list l
## CAN BE UTILISED IN OUR PROJECT TO CUT VIDEO ACCORDING TO BEAT TIMELENGTH
##
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip  
l = [23, 46, 68, 90, 112, 135]      ##TESTING LIST
vid = ['1234.mp4' , 'abcd.mp4']     ##TESTING VIDEOS
tup = zip(l,vid)
#for num in range(0,55):
for tim,vids in tup:
    s = ("{a!r}.mp4".format(a = tim))
    ffmpeg_extract_subclip(vids, 0, tim , targetname=s)
