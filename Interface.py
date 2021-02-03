#!/usr/bin/python3

from tkinter import *
from Downloader import Downloader


class Interface:
    def __init__(self):
        self.root = Tk()
        self.dl = Downloader()
        self.music_only = IntVar()
        self.url = StringVar()
        self.message = StringVar()

        self.root.title("YouTube Downloader")
        self.root.geometry('500x150')
        self.menu()
        self.widgets()

    # ----------------------------------------

    def menu(self):
        menubar = Menu(self.root)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Exit', command=self.root.quit)

        menubar.add_cascade(label="File", menu=filemenu)

        self.root.config(menu=menubar)

    # ----------------------------------------
    def widgets(self):
        # URL Frame
        url_frame = Frame(self.root)

        Label(url_frame, text="URL").pack(side=LEFT)

        self.url_input = Entry(url_frame, textvariable=self.url, width=50)

        self.url_input.pack(side=RIGHT)

        url_frame.pack()

        # Audio Fame
        audio_frame = Frame(self.root)

        Checkbutton(audio_frame, text="Music Only",
                    variable=self.music_only, onvalue=True, offvalue=False).pack()

        audio_frame.pack()

        # Downloading Frame
        download_frame = Frame(self.root)

        Button(download_frame, text="Download", command=self.download).pack()

        download_frame.pack()

        # Message Frame
        message_frame = Frame(self.root)

        Label(message_frame, textvariable=self.message,
              width=65).pack()

        self.update_message('Ready...')

        message_frame.pack()

    # ----------------------------------------
    def update_message(self, msg):
        self.message.set(msg)

    # ----------------------------------------
    def download(self):
        url = self.url.get()
        info = self.dl.info(url)

        msg = 'Downloading {} by {}'.format(
            str(info['title']), str(info['uploader']))

        msg.replace('\n', '')
        msg.replace('\t', '')

        self.update_message(msg)

        if self.music_only:
            self.dl.audio()
        else:
            self.dl.video()

        self.update_message('Done.  Ready for the next URL')
        self.url.set('')

    # ----------------------------------------
    def show(self):
        self.root.mainloop()
