import os
from moviepy.editor import VideoFileClip

folder_path = '' #Write the path to your folder here to input the videos
files = os.listdir(folder_path)

number = 0 #To give a unique name to each video

for file in files:
    output = str(number) + ".mp4"
    video_clip = VideoFileClip(folder_path + "\\" + file)
    video_clip.write_videofile(output, codec="libx264", audio_codec="aac")
    number += 1