import os
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable
import subprocess

try:
    video = input("Enter the URL of the video to download: ")

    yt = YouTube(video)

    stream = yt.streams.filter(only_audio=True).first()

    output_path = '/Users/treyweldon/Desktop/editing/Downloaded Audio'

    downloaded_file = stream.download(output_path=output_path)

    input_file = downloaded_file
    output_file = os.path.splitext(input_file)[0] + '.mp3'

    ffmpeg_cmd = f'ffmpeg -i "{input_file}" -vn -ar 44100 -ac 2 -b:a 192k "{output_file}"'
    subprocess.run(ffmpeg_cmd, shell=True, check=True)

    os.remove(input_file)

    print(f'"{yt.title}" downloaded and converted to MP3 successfully.')

except RegexMatchError:
    print("Invalid YouTube URL. Please check the URL and try again.")

except VideoUnavailable:
    print("Video unavailable. It may be private or deleted.")

except subprocess.CalledProcessError as e:
    print(f"ffmpeg command failed: {e}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
