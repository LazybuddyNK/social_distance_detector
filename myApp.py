import numpy
import time
import cv2
from tkinter import *
import tkinter.messagebox
import datetime
import os
from tkinter import filedialog
from PIL import Image,ImageTk,ImageOps
from tkinter import ttk 

current_date_and_time = datetime.datetime.now()

current_date_and_time_string = str(current_date_and_time)

file_path= os.getcwd()



root=Tk()
root.geometry('500x570')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('Social Distance Detector')
frame.config(background='light blue')
label = Label(frame, text="Detector",bg='light blue',font=('Times 35 bold'))
label.pack(side=TOP)


image = Image.open(file_path + "/demo.png")
image = ImageOps.fit(image, (500, 570))
image = ImageTk.PhotoImage(image)
test = Label(frame, image = image, bg="#ffb8e1")
test.pack()






def hel():
   help(cv2)

def Contri():
   tkinter.messagebox.showinfo("Contributor","Sourav Sharma")


def anotherWin():
   tkinter.messagebox.showinfo("About",'Social Distance Detector version v1.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python 3')
                                    
   

def confo():
   #Enter configuration file here
   pass

menu = Menu(root)
root.config(menu=menu)

#Tools
subm1 = Menu(menu,tearoff=False)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Set Configuration",command=confo)

#Help
subm2 = Menu(menu,tearoff=False)
menu.add_cascade(label="Help",menu=subm2)
subm2.add_command(label="Open CV Docs",command=hel)

#About
subm3 = Menu(menu,tearoff=False)
menu.add_cascade(label="About",menu=subm3)
subm3.add_command(label="Social Distance Detection",command=anotherWin)
subm3.add_command(label="Contributors",command=Contri)



def exitt():
   exit()

def open_app():
    filename= filedialog.askopenfilename(parent=root,initialdir="/",title="Select File",filetypes=[
                    ("all video format", ".mp4"),
                    ("all video format", ".flv"),
                    ("all video format", ".avi"),
                    ("All files","*.*")
                ])
    return(filename)
    
  
def web():
   capture =cv2.VideoCapture(0)
   while True:
      ret,frame=capture.read()
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   capture.release()
   cv2.destroyAllWindows()

def webrec():
   capture =cv2.VideoCapture(0)
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter(current_date_and_time_string + '.avi',fourcc,11.0,(640,480))
   while True:
      ret,frame=capture.read()
      cv2.imshow('frame',frame)
      op.write(frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   op.release()
   capture.release()
   cv2.destroyAllWindows()   


   
def webdet():
    os.system('python social_distance_detector.py')
   


def webdetrec():
    file_name=open_app()
    root.update()
    os.system("python social_distance_detector.py -i " + str(file_name))


   
but1=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=web,text='Open Cam',font=('helvetica 15 bold'))
but1.place(x=5,y=104)

but2=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webrec,text='Open Cam & Record',font=('helvetica 15 bold'))
but2.place(x=5,y=176)

but3=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webdet,text='Open Cam & Detect',font=('helvetica 15 bold'))
but3.place(x=5,y=250)


but4=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,text='Select File to Detect',command=webdetrec,font=('helvetica 15 bold'))
but4.place(x=5,y=322)

but5=Button(frame,padx=5,pady=5,width=5,bg='white',fg='black',relief=GROOVE,text='EXIT',command=exitt,font=('helvetica 15 bold'))
but5.place(x=210,y=478)




root.mainloop()