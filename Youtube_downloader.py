#Make sure yt_dlp is installed 
# use: pip install yt-dlp

#Importing yt_dlp
import os
import yt_dlp

try:
    # Ask for YouTube link
    link = input("Enter the link of YouTube video to download: ")

    # Where the video will be downloaded can change wherever you want
    download_folder = r'C:\Users\jbpop\Desktop'

    # Controls video quality
    quality = {
        'format': 'best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
    }

    # Actual dowloader
    with yt_dlp.YoutubeDL(quality) as vid:
        vid_info = vid.extract_info(link, download=False)
        print("Name of Video: ", vid_info.get('title', 'N/A'))
        print("Number of Views: ", vid_info.get('view_count', 'N/A'))

        vid.download([link])

    #confirms downloard was complete
    print("Downloaded!")

#Helps Troubleshooting
except Exception as error:
    print("Error! ", str(error))