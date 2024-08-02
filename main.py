import yt_dlp
import whisper

youtube_video_url = "https://www.youtube.com/watch?v=L9XJVgpUUzg"
model = whisper.load_model('small')

# yt-dlp configuration for downloading only the audio
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'tmp.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# Downloads the audio using yt-dlp
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([youtube_video_url])

# Transforms audio into text
result = model.transcribe('tmp.mp3')

# Prints text
print("---------------------------------")
print(result["text"])




file_path = "transcription.txt"

# Saves text into a .txt file
with open(file_path, "w+") as txt_file:
    txt_file.write(result['text'])
