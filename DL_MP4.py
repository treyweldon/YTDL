from pytube import YouTube

video = YouTube(
    str(input("Enter the URL of the video to download: "))
)

yd = video.streams.get_highest_resolution()

yd.download('/Users/treyweldon/Desktop/editing/Downloaded Video')

print( '"' + video.title + '" Download Completed')