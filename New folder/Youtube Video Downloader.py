from tkinter import *
from tkinter import messagebox
from pytube import YouTube
window=Tk()
window.title('Youtube Downloader')
window.geometry("499x300")
window.resizable(0,0)
window.configure(bg="#869890")

def Download():
    if CallmeNow.get()=='':
        messagebox.showerror("Error","Please Enter Link")
    else:
        CallmeNow1 = YouTube(CallmeNow.get())
        video =CallmeNow1.streams.first()
        video.download()
        Label(window,text='Downloaded',font='arial 15').place(x=80,y=100)
    
Label(window,text='Youtube Video Downloader',font='arial 26 bold', bg="#869890" ,fg="#0a030c").place(x=19,y=20)
Label(window,text='Insta: Sushant.exe_',font='arial 13 bold', bg="#869890" ,fg="#0a030c").pack()
CallmeNow = StringVar()
Label(window,text="Enter Your Video's Url",font='arial 15 bold', bg="#869890" ,fg="#0a030c").place(x=100,y=80)
Label(window,text="The Small youtube Downloader Is Made Only For Educational Purpose",font='arial 7 bold', bg="#869890" ,fg="#0a030c").place(x=0,y=210)
EnteryPoint = Entry(window,width=50,textvariable=CallmeNow).place(x=70,y=110)



Button(window,
       text='DOWNLOAD',
       font='arial 15 bold',
       bg='#a08df4',
       padx=2,
       command=Download,
       fg="black").place(x=150, y=150)
    
    
window.mainloop()