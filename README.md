# BeatsCompiler
Beat detection and cut to music video creator (python based, music beat detection and video cut/join libraries) - finds all the  beats that a music file has and cuts various videos and joins alongside the audio track to make a compilation video

## Libraries to be used
- librosa (Music information retrieval system for beat detection) [Librosa Webpage](https://librosa.github.io/librosa/)
- ffmpeg (python wrapper - for audio / video processing) [FFMPEG webpage](https://www.ffmpeg.org/)

## Setup 
- Install latest anaconda distribution on a linux machine
- Find an mp3 file (preferable EDM as it is more synthetic, precise and clear)
- Using librosa, find the times where beat occurs
- Process (input) a set of video files
- Trim videos to lengths between the beats
- Merge videos (removing their audios) into a single video
- Overlay the new video on top of audio
- Export an mp4 file

## Librosa sample and official github Account
https://github.com/librosa/librosa/blob/master/examples/LibROSA%20demo.ipynb

## FFMPEG example and how to use it:
https://github.com/kkroening/ffmpeg-python/blob/master/examples/README.md
