#!/usr/bin/env python3

import os
import requests
import re
import stat

# Function to get the newest video URL of a YouTuber
def get_newest_video_url():
    # Construct the URL of the YouTuber's channel page
    channel_url = "https://www.youtube.com/@TheLibraryofLetourneau/videos"

    try:
        # Send a GET request to the channel URL
        response = requests.get(channel_url)

        # Extract the video ID from the HTML content using regular expressions
        video_id_match = re.search(r"watch\?v=([a-zA-Z0-9_-]+)", response.text)

        # If a video ID is found, construct the video URL
        if video_id_match:
            video_id = video_id_match.group(1)
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            return video_url
        else:
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def main():
    # Get the newest video URL
    newest_video_url = get_newest_video_url()

    if newest_video_url:
        # Format the command to run
        s = f"yt-dlp --config-locations conf.conf {newest_video_url}"

        # Specify the file path
        file_path = "download-latest.sh"

        # Open the file in write mode
        with open(file_path, 'w') as file:
            # Write the string into the file
            file.write(s)

        # chmod +x
        st = os.stat(file_path)
        os.chmod(file_path, st.st_mode | stat.S_IEXEC)

        print("Download script updated successfully.")
    else:
        print("No videos found.")

if __name__ == "__main__":
    main()

