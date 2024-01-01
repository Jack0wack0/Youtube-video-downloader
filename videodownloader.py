"""
Copyright 2023 jack0wack0 (https://github.com/Jack0wack0)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the “Software”), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THIS SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THIS SOFTWARE OR THE USE OR OTHER DEALINGS
IN THIS SOFTWARE.
"""

# Imports
import pytube
from pytube import YouTube
import time
import ssl
import os
import math
import re
import urllib.request

# YouTube link regex 
youtube_regex = r'(https?://)?(www\.)?' r'((youtube\.com)|((m|music)\.youtube\.com))/' r'[^\s]+$'

# Checking if the link is from youtube
def validate_link(url):
  if re.match(youtube_regex, url):
    return True
  return False 

# Check any and every exception for links. If the link is not from youtube, its not getting downloaded
def check_valid_link(link):
  if not link:
    raise ValueError('No link provided')
  if not validate_link(link):
    raise ValueError('That link is not a valid YouTube link')
  try:
    response = urllib.request.urlopen(link)
    if response.getcode() == 200:
      print("Link is valid")
      return True
  except Exception as e:
    print("Invalid link")
    raise TypeError("Invalid Link")

# Ask the user if the video is correct
def checkCorrectVideo(stream):
    linkcheck = input("Is this the correct video? (y/n): ")
    if linkcheck == "y":
        time.sleep(1)
        print("downloading video.")
        stream.download()
        print("Downloaded!")
    elif linkcheck == "n":
        print("No was selected. Exiting the program with exception on line 54.")
        raise Exception("Incorrect video. Rerun the program")

# Obtain and print information about the video.
def printVideoData(ytlink):
    title = ytlink.title
    views = ytlink.views
    author = ytlink.author
    os.system("clear")
    print()
    print(f"title: {title}")
    print(f"Views: {views}")
    print(f"Creator: {author}")
    obtainFileSize(ytlink)
    print()

# Obtain the filesize and display it.
def obtainFileSize(ytlink):
    filesize = ytlink.streams.get_highest_resolution().filesize
    filemb = filesize * 0.000001
    filetrunc = math.trunc(filemb)
    print(f"filezize = {filetrunc} MB")

# Check if the video is age restricted
def checkAgeRestriction(ytlink):
    if pytube.exceptions.AgeRestrictedError(ytlink) == True:
        os.system("clear")
        print("Video is age restricted. Exiting the program with exception on line 80.")
        raise Exception("This video is age restricted. Unable to download")
    
# This is the main function for the program.
def linkinput(link):
    ytlink = YouTube(link)
    checkAgeRestriction(ytlink)
    printVideoData(ytlink)
    stream = ytlink.streams.get_highest_resolution()
    checkCorrectVideo(stream)

# commands outside of the functions
ssl._create_default_https_context = ssl._create_stdlib_context
os.system("clear")
link = input("paste the youtube video link below\n")
check_valid_link(link)
linkinput(link)
