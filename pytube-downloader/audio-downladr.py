from pytube import YouTube

def download_audio(yt):
    
    my_streams = yt.streams.filter(only_audio=True)
    for streams in my_streams:
        print(f"Audio itag :  {streams.itag} Quality : {streams.abr} ")

    input_itag = input("Enter itag value : ")
    audio = yt.streams.get_by_itag(input_itag)

    audio.download("pytube-downloader/audios")
    print("Audio is downloading as ", yt.title + ".mp3")


link = input("Enter your link : ")
yt = YouTube(link)
download_audio(yt)