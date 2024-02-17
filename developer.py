from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        
        
        # img_top=Image.open("C:\\Users\\HP\\Downloads\\attend-me-master\\attend-me-master\\images\\bg2.jpg")
        # img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        # self.photoimg_top=ImageTk.PhotoImage(img_top)

        # f_lbl=Label(self.root,image=self.photoimg_top)
        # f_lbl.place(x=0,y=55,width=1530,height=720)

        # main_frame=Frame(bd=2,bg="white")
        # main_frame.place(x=200,y=0,width=500,height=900)

        img_top1=Image.open("C:\\Users\\HP\\Downloads\\attend-me-master\\attend-me-master\\images\\bg2.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(image=self.photoimg_top1)
        f_lbl.place(x=200,y=0,width=200,height=600)

        
        img_top2=Image.open("C:\\Users\\HP\\Downloads\\attend-me-master\\attend-me-master\\images\\bg2.jpg")
        img_top2=img_top2.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(image=self.photoimg_top2)
        f_lbl.place(x=650,y=0,width=200,height=600)

        img_top3=Image.open("C:\\Users\\HP\\Downloads\\attend-me-master\\attend-me-master\\images\\bg2.jpg")
        img_top3=img_top3.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top3=ImageTk.PhotoImage(img_top3)

        f_lbl=Label(image=self.photoimg_top3)
        f_lbl.place(x=1100,y=0,width=200,height=600)

        title_lbl=Label(self.root,text="OUR TEAM",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)




        dev_label=Label(text="Hello my name is Ajinkya Shama",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=145,y=450)

        dev_label=Label(text="I am full software developer",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=160,y=500)
        

        dev_label=Label(text="Hello my name is Ajinkya Shama",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=605,y=450)

        dev_label=Label(text="I am full software developer",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=620,y=500)

        dev_label=Label(text="Hello my name is Ajinkya Shama",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=1055,y=450)

        dev_label=Label(text="I am full software developer",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=1070,y=500)



        


if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()