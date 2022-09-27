from pytube import YouTube

def download_vid(yt):
    # filter mp4 streams from object
    my_streams = yt.streams.filter(file_extension='mp4', only_video=True)

    for streams in my_streams:
        print(f"Video itag : {streams.itag} Resolution : {streams.resolution}")

    
    input_itag = input("Enter itag value : ")
    video = yt.streams.get_by_itag(input_itag)

    video.download("pytube-downloader/vids")
    print("Vid is downloading as \"", yt.title + ".mp4\"")


link = input("Enter your link here : ")
yt = YouTube(link)
download_vid(yt)