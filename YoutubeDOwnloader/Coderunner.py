from email import message
from platform import python_branch
from pytube import YouTube
from tkinter import messagebox
link = 'https://www.youtube.com/watch?v=8mYeTuzBQr4'
YoutubeLink = YouTube(str(link))
YoutubeTitle = YoutubeLink.title

messagebox.showinfo(f"{YoutubeTitle}",f"{YoutubeTitle}")
messagebox.showwarning("Error","Unable To Download the File")
LovePrastap = messagebox.askquestion("Question","DO You Love Me")
if LovePrastap =='yes':
    print("WoW Miracle ")
else:
    print("Bichara Lastai Dukhad Ghatana Sunyo Yrr")
messagebox.showerror("Error","Erroe Message is seen")
messagebox.askokcancel("Why","Give any Reason To me")
messagebox.askyesno("Tell ME","Vande AAja Ja xa Man ma")
messagebox.askretrycancel("AskRetryCancelBox","SOme Dummmy Data By the user")

# Creating the Radio Button in python_branch
# gender = tk.IntVar()
# radiobutton_1 = tk.Radiobutton(window_main, text='Male', variable=gender, value=1)
# radiobutton_1.pack()
# radiobutton_2 = tk.Radiobutton(window_main, text='Female', variable=gender, value=2)
# radiobutton_2.pack()
# radiobutton_3 = tk.Radiobutton(window_main, text='Other', variable=gender, value=3)
# radiobutton_3.pack()
 