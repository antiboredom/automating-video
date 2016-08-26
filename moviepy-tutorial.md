# Moviepy Tutorial

[Moviepy](http://zulko.github.io/moviepy/index.html) is a great python library that lets you edit videos in python.

## Installation

```
pip install moviepy
```

You may also need to install the ```pillow``` library to do things like resize clips.

```
pip install pillow
```

## Basic Use

### VideoFileClips

The basic use is to create instances of a ```VideoFileClip``` class, passing in the filename of the video you want to work with.

This will combine two videos into a single clip:

```python
import moviepy.editor as mp

video1 = mp.VideoFileClip('somevideo.mp4')
video2 = mp.VideoFileClip('anothervideo.mp4')

final_video = mp.concatenate_videoclips([video1, video2])
final_video.write_videofile('composition.mp4')
```

After we load our videos in, we make a new clip with the ```concatenate_videoclips``` method, which takes an array of ```Clip``` instances. Once we have our ```final_video``` clip, we call ```write_videofile``` to save our composition.

You can also tell moviepy to use only a portion of clip, by calling ```subclip(start, end)``` on a ```VideoFileClip```. The ```subclip``` method takes two arguments, a start and an end time, in seconds.

```python
import moviepy.editor as mp

video1 = mp.VideoFileClip('somevideo.mp4').subclip(1.1, 3)
video2 = mp.VideoFileClip('anothervideo.mp4').subclip(5, 9)

final_video = mp.concatenate_videoclips([video1, video2])
final_video.write_videofile('composition.mp4')
```

In addition to ```subclip```, you can also call ```resize((width, height))``` to resize a video, and ```crossfadein(time)``` to fade videos in.

### Text and Images and Mattes

Moviepy can also insert text, images and solid colors, with the ```TextClip```, ```ImageClip```, and ```ColorClip``` classes. The only caveat is that we need to set the duration of the clips manually with the ```set_duration(time)``` method.

In this example we show a red frame for 5 seconds, and then an image for 10 seconds.

```python
import moviepy.editor as mp

clip1 = mp.ColorClip((1280, 720), col=(255, 0, 0))
clip1 = clip1.set_duration(5)

clip2 = mp.ImageClip('someimage.jpg')
clip2 = clip2.set_duration(10)

final_video = mp.concatenate_videoclips([clip1, clip2], method="compose")
final_video.write_videofile('composition.mp4', fps=24)
```

Note that we need to set the frames per second of the final video because these are not set by default for image and color clips. I've also added the ```method="compose"``` parameter to the ```concatenate_videoclips``` function. This will ensure that the image will display correctly if it's not 1280x720.







