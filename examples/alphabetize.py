import sys
import moviepy.editor as mp
import audiogrep

videofile = sys.argv[1]
sentences = audiogrep.convert_timestamps([videofile])
words = []

for sentence in sentences:
    words += sentence['words']

words.sort(key=lambda x: x[0])
# words = words[100:200]

original_video = mp.VideoFileClip(videofile)

clips = []

for word in words:
    if len(word[0]) < 5:
        continue

    start = float(word[1])
    end = float(word[2])
    clip = original_video.subclip(start, end)
    clips.append(clip)


final_video = mp.concatenate_videoclips(clips)
final_video.write_videofile('alphabetized.mp4')



