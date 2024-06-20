from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

try:
    video_url = input("Enter the URL of the video to download: ")

    video = YouTube(video_url)

    downloaded_file = video.streams.get_highest_resolution()

    download_path = '/Users/treyweldon/Desktop/editing/Downloaded Video'
    downloaded_file.download(download_path)

    print(f'"{video.title}" Download Completed')

except RegexMatchError:
    print("Invalid YouTube URL. Please check the URL and try again.")

except VideoUnavailable:
    print("Video unavailable. It may be private or deleted.")

except Exception as e:
    print(f"An error occurred: {str(e)}")