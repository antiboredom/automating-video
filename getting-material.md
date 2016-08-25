## youtube-dl
[youtube-dl](https://rg3.github.io/youtube-dl/) is a great command line program that you can use to download video from a bunch of different sources (YouTube, Vimeo, Facebook, and many more).

If you're on a Mac, first install homebrew if you don't already have it:
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Then just run
```
brew install youtube-dl
```

To download a video, just type youtube-dl and the url of the video you want
```
youtube-dl http://youtube.com.com/somevideo
```

## Savefrom.net
Another easy option for YouTube Videos is [savefrom.net](http://en.savefrom.net/). Just go to any YouTube video, and then change the domain name from www.youtube.com to www.ssyoutube.com.

## Subtitles
You can download subtitles for YouTube videos from [downsub.com](http://downsub.com)

You can also use youtube-dl's download subtitles option
```
youtube-dl http://somevideowebsite.com/somevideo --write-sub
```