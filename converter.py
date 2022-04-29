import moviepy.editor as moviepy
from PyQt5.QtWidgets import QFileDialog
file_name = QFileDialog.getOpenFileName()
print(file_name)
clip=moviepy.VideoFileClip(file_name)
new_clip=clip.write_videofile("myvideo.mp4")