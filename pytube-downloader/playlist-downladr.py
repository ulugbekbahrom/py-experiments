from pytube import Playlist

def download_playlist(pl):

    print(pl.title)
    for video in pl.videos:
        try:
            video.streams.first().download("pytube-downloader/shorts")
        except Exception as e:
            print(e, type(e))
    print("Playlist is downloaded")


link = input("Youtube Playlist URL : ")
pl = Playlist(link)
download_playlist(pl)