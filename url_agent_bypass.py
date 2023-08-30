#!/usr/bin/python

#I wrote this - and it was done randomly without knowing doing so was so easy. The success of this script depends on successfully spoofing the header for a user agent.
#Per line 19, the header here matches up with an iPad and chances are, you are now downloaidng Kali Linux images on an iPad. No, sir or ma'am... But, who's to say whether or not the good folks at 
#Offensive security care whether or not you are spoofing one to obtain their open source products efficiently. Hence, I am glad I finally circumvented the frustrating obstacles I faced leading up to this 
#code

# Test URL: https://cdimage.kali.org/kali-2023.3/kali-linux-2023.3-virtualbox-amd64.7z

import os
import time
import urllib.request
import requests
from tqdm import tqdm  # Import the tqdm library

def download_progress_bar(block_num, block_size, total_size):
    downloaded = block_num * block_size
    progress = (downloaded / total_size) * 100
    print(f"Downloaded: {downloaded} bytes | Progress: {progress:.2f}%", end='\r')

# Header hack: mimic the user agent header of an iPad
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

urlf = input("Enter the URL for the file you need to download: ")
print('Attempting to download files')
#time.sleep(3)

# Get the filename from the URL
filename = urlf.split("/")[-1]

# Download the file and show progress using requests library
response = requests.get(urlf, headers=HEADERS, stream=True)
total_size = int(response.headers.get('content-length', 0))

with open(filename, 'wb') as file, tqdm(
        desc=filename,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
    for data in response.iter_content(chunk_size=1024):
        size = file.write(data)
        bar.update(size)

print("\nDownload completed")

# Check if the file was downloaded
if os.path.exists(filename):
    print("File successfully downloaded")
else:
    print("Failed to download file - review the URL and network connection")
