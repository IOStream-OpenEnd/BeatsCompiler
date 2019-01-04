from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("1234.mp4", 9, 25, targetname="test.mp4")