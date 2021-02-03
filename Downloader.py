#!/usr/bin/python3

from youtube_dl import YoutubeDL

class Downloader:
  def __init__(self, url=None):
    self.url = None
    self.meta = None

    self.info(url)

  #----------------------------------------
  def set_url(self, url=None):
    if url is not None:
      self.url = url

    return self.url is not None

  #----------------------------------------
  def info(self, url=None):
    if self.set_url(url) is False:
      return False
      
    with YoutubeDL() as ytl:
      self.meta = ytl.extract_info(self.url, download=False)

    return self.meta

  #----------------------------------------
  def video(self, url=None):
    if self.set_url(url) is False:
      return False

    with YoutubeDL() as ytl:
      ytl.download([self.url])
      return True

  #----------------------------------------
  def audio(self, url=None):
    if self.set_url(url) is False:
      return False

    opts = {
      'format': 'bestaudio/best',
      'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
      }]
    }

    with YoutubeDL(opts) as ytl:
      ytl.download([self.url])
      return True
