import sys
import moviepy.editor as mp

videos = []

for filename in sys.argv[1:]:
    video = mp.VideoFileClip(filename)

    # just get the first second
    video = video.subclip(0, 1)

    # make all videos the same size
    video = video.resize((1280, 720))
    videos.append(video)

final_video = mp.concatenate(videos)
final_video.write_videofile('composition.mp4')
