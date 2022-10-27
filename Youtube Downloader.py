from pytube import YouTube
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD
from tkinter import ttk
from pytube import Playlist
#Form Settings

form=tk.Tk()
form.geometry("500x500")
form.title("Youtube Downloader v0.5")
form.configure(bg="#303030")
#-----------------------
#Functions
def video_info():
            link = link_entry.get()
            yt = YouTube(link)
            video_link.config(text=yt.title)

        # İndirilecek Konumu Seçtiren Fonksiyon
def select_directory():
            path_select = filedialog.askdirectory()
            location_label.config(text=path_select)
        
        # İndirme İşlemini Yapan Fonksiyon
def download_video():
    link = link_entry.get()
            
    try:
         yt = YouTube(link)
    except:
        download_status.config(text="Geçersiz Link")

    folder =location_label.cget("text")

    uzanti = listitem.get()
    if uzanti == ".mp3":
        mp3 = yt.streams.filter(only_audio=True).first().download(folder)
       
        download_status.config(text="Başarıyla İndirildi!")
    elif uzanti ==".mp4":
        mp4 = YouTube(link).streams.get_highest_resolution().download(folder)
        download_status.config(text="Başarıyla İndirildi!")

#Video Find Section


link_entry=Entry(form,width=50)
link_entry.place(x=250,y=150,anchor=CENTER)

linklabel=Label(form,text="Enter Video Link",fg="RED",bg="#303030")
linklabel.place(x=250,y=125,anchor=CENTER)

location_label=Label(form,text="You didn't select location",fg="RED",bg="#303030")
location_label.place(x=250,y=220,anchor=CENTER)

download_status=Label(form,text="DOWNLOAD STATUS",fg="RED",bg="#303030")
download_status.place(x=250,y=450,anchor=CENTER)


check_button= Button(form,text="Check Link",fg="RED",bg="#1e1e1e",command=video_info)
check_button.place(x=250,y=190,anchor=CENTER)

download_button= Button(form,text="Start Download",fg="RED",bg="#1e1e1e",command=download_video)
download_button.place(x=350,y=190,anchor=CENTER)

fileSelect_button= Button(form,text="Select Location",fg="RED",bg="#1e1e1e",command=select_directory)
fileSelect_button.place(x=150,y=190,anchor=CENTER)
#Video info Section
video_tittle=Label(form,text="Video Tittle: ",fg="RED",bg="#303030")
video_tittle.place(x=10,y=325)
video_link=Label(form,text="",fg="white",bg="#303030")
video_link.place(x=85,y=325)

#video_length=Label(form,text="Video Length: ",fg="RED",bg="#303030")
#video_length.place(x=10,y=350)

#video_lenghtLabel=Label(form,text="---",fg="white",bg="#303030")
#video_lenghtLabel.place(x=90,y=350)

#Download Type
ayarlar = [
            ".mp3",
            ".mp4"
        ]

listitem = ttk.Combobox(form,value = ayarlar,width=10)
listitem.place(x=250,y=275,anchor=CENTER)

list_label=Label(form,text="Select Type",fg="RED",bg='#303030')
list_label.place(x=250,y=250,anchor=CENTER)
form.mainloop()