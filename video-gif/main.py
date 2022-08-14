import ffmpeg
from ffmpeg import Error as FFmpegError
import os

def video_to_gif():
    # stream = ffmpeg.input("video_0.mp4")
    # stream = ffmpeg.filter(stream , "fps", fps=2)
    # stream = ffmpeg.output(stream, "video_0.gif")
    # ffmpeg.run(stream)

    for file in os.listdir("video"):
        if file.endswith((".mp4", ".MP4")):
            file_name = file.split(".")[0]
            print(file_name)
            try:
                gif_file = file_name + ".gif"
                stream = ffmpeg.input(f"video/{file_name}")
                stream = ffmpeg.filter(stream , "fps", fps=2)
                stream = ffmpeg.output(stream, f"gif/{gif_file}" )
                ffmpeg.run(stream)
            except ffmpeg.Error as e:
                print(e.stderr)


def main():
    video_to_gif()

if __name__ == "__main__":
    main()



