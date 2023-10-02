"""
Copyright 2023 jack0wack0 (https://github.com/Jack0wack0)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the “Software”), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
"""





import pytube
from pytube import YouTube
from pytube import streams
from pytube import Stream
from pytube import extract
from pytube import exceptions
import time
from tqdm import tqdm
import ssl
import os
import math
ssl._create_default_https_context = ssl._create_stdlib_context



#clear the screen
os.system("clear")

#grab the input and turn it into a readable link
link = input("paste the link you want to download now: \n")
ytlink = YouTube(f"{link}") #loophole to add quotation marks to the link. I dont know if its nessecary but im scared to take it out

#non-working function
#check if age restricted?
"""
if pytube.extract.is_age_restricted(ytlink) == True:
    print("content is age restricted")
    time.sleep(2)
elif pytube.extract.is_age_restricted(ytlink) == False:
    print("content is not age resticted")
    time.sleep(2)
"""

#set all of our variables to print and do things with
title = ytlink.title
views = ytlink.views
author = ytlink.author

#grab the highest resolution and grab its filesize
stream = ytlink.streams.get_highest_resolution()
filesize = ytlink.streams.get_highest_resolution().filesize

#divide the filesize to make it more readable
filemb = filesize * 0.000001

#truncate the number to make it prettier.
filetrunc = math.trunc(filemb)

#if the video is age restricted, reject the video
if pytube.exceptions.AgeRestrictedError(ytlink) == True:
    raise Exception("The video is age restricted. Unable to download.")
    exit

#clear the screen again and provide details about the video
os.system("clear")
print()
print(f"filezize = {filetrunc} MB")
time.sleep(1)
print(f"title: {title}")
time.sleep(1)
print(f"Views: {views}")
time.sleep(1)
print(f"Creator: {author}")
print()

time.sleep(1)
print("downloading stream. ")
print()

#download the stream
stream.download()

#show a progress bar. it isnt actually linked to the download process, but it provides a reasonable 10 second buffer.
for i in tqdm(range(0,10), desc = "Progress: "):
    time.sleep(1)

print("Stream Downloaded. Enjoy!")