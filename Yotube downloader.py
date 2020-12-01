from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox as msg
from pytube import YouTube



def select(event):
    data=askdirectory()
    try:
        dirV.set(f"{data}")
        pass
    except:
        print("you didn't selected compatible directory.")
        pass
    pass

def remove(event):
    enterurlentry.delete(0,END)
    root.update()

def download(event):
    global yt
    try:
        yt = YouTube(linkV.get())
        pass
    except:
        msg.showerror("Privacy issue","You can't download this video because of either low conection OR owner "
                                      "has restricted this video.")
        print("Connection error........")
        pass
    global v
    if ext.get()==1:
        v=yt.streams.filter(type="audio").first()
        pass
    else:
        v = yt.streams.filter(type="video").first()
        pass

    try:
        msg.showinfo("Downloading started","""Your file is downloading....Please click "OK" and we will notify you when downloading is completed.""")
        if dirV.get()!="Choose a folder to save file":
            v.download(dirV.get())
            pass
        else:
            v.download()
        msg.showinfo("Task completed","Successfully downloaded your file!!")
        pass
    except:
        print("Can't download.......")
        msg.showerror("Failed!","You can't download this video.")
        pass
    pass



root=Tk()
root.geometry('600x680+450+75')
root.title("Youtube Downlaoder Made By Madhavi Bisen")
root.resizable(0,0)

bgImage=PhotoImage(file='bg.png')
bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)

youtubelogoImage=PhotoImage(file='YouTube.png')
youtubelogoLabel=Label(root,image=youtubelogoImage,bg='grey4',width=80,height=45,bd=20)
youtubelogoLabel.place(x=250,y=15)

enterurlLabel=Label(root,text='URL :',font=('castellar',15,'bold'),fg='red3',bg='grey')
enterurlLabel.place(x=95,y=130)
linkV=StringVar()
linkV.set("Enter link")
enterurlentry=Entry(root,font=('calibri',12,'italic'),textvariable=linkV,width=30,bd=4,relief=GROOVE,justify=CENTER)
enterurlentry.place(x=220,y=130)
enterurlentry.bind("<Button-1>",remove)

enterurlentry.focus_set()

enterdirectoryLabel=Label(root,text='Directory :',font=('castellar', 15, 'bold'),fg='red3',bg='grey')
enterdirectoryLabel.place(x=55,y=180)
dirV=StringVar()
dirV.set("Choose a folder to save file")
enterdirectoryentry=Entry(root,font=('calibri',12,'italic'),textvariable=dirV,width=30,bd=4,relief=GROOVE,justify=CENTER,)
enterdirectoryentry.place(x=220,y=180)
enterdirectoryentry.bind("<Button-1>",select)
enterdirectoryentry.focus_set()

ext=IntVar()
ext.set(2)
entermodeLabel=Label(root,text='Mode :',font=('castellar', 15, 'bold'),fg='red3',bg='grey')
entermodeLabel.place(x=95,y=250)
audio=Radiobutton(root,text="Audio",value=1,variable=ext,bg="grey",fg="black",font=('calibri',12,'bold'))
audio.place(x=250,y=250)
video=Radiobutton(root,text="Video",value=2,variable=ext,bg="grey",fg="black",font=('calibri',12,'bold'))
video.place(x=350,y=250)


downloadButtonimage=PhotoImage(file='download.png')
downloadButton=Button(root,image=downloadButtonimage,bg='grey',bd=4)
downloadButton.place(x=250,y=300)
downloadButton.bind("<Button-1>",download)


exitButtonimage=PhotoImage(file='exit.png')
exitButton=Button(root,image=exitButtonimage,bg='grey',bd=4,command=exit)
exitButton.place(x=350,y=300)




root.mainloop()