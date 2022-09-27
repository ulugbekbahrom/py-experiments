from pytube import YouTube
import string

# function takes youtube object as arg
def vid_info(yt):
    print("title : ", yt.title)
    print("total length : ", yt.length, " seconds")
    print("total views : ", yt.views)
    print("is age restricted : ", yt.age_restricted)
    print("video description : ", yt.description)
    print("thumbnail url : ", yt.thumbnail_url)


link = "https://youtu.be/V3ZPPPKEipA"
yt = YouTube(link) # create youtube object

# call the function
vid_info(yt)

