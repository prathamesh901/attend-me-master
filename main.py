from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime

from click import command
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1530x790+0+0")
      
        # #first img
        # img=Image.open("images\\bg.jpg")
        # img=img.resize((1700,3330),Image.LANCZOS)
        # self.photoimg=ImageTk.PhotoImage(img)
        
        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=0,y=0,width=1530,height=710)
        # #second img
        # img1=Image.open("images\\bg.jpg")
        # img1=img1.resize((500,130),Image.LANCZOS)
        # self.photoimg1=ImageTk.PhotoImage(img1)

        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=500,y=0,width=500,height=130)
        # #third img
        # img2=Image.open("images\\bg.jpg")
        # img2=img2.resize((500,130),Image.LANCZOS)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # f_lbl=Label(self.root,image=self.photoimg2)
        # f_lbl.place(x=1000,y=0,width=500,height=130)
        #baground img
        img3=Image.open("images\\bg2.jpg")
        img3=img3.resize((1500,800),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=800)

        # title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM",font=("times new roman",35,"bold"),bg="cyan",fg="red")
        # title_lbl.place(x=0,y=0,width=1530,height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(bg_img,font=('times new roman',14,'bold'),background='black',foreground='blue')
        lbl.place(x=20,y=0,width=110,height=50)
        time()
        
        # img_chat=Image.open("images\\face2.jpg")
        # img_chat=img_chat.resize((110,50),Image.LANCZOS)
        # self.photoimg_chat=ImageTk.PhotoImage(img_chat)
        # bchat=Button(title_lbl,image=self.photoimg_chat,cursor="hand2",command=self.cahatbot)
        # bchat.place(x=1250,y=0,width=120,height=40)
        

        #student button
        img4=Image.open("images\\sd1.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.student_details)
        b1.place(x=300,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",command=self.student_details,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=300,y=400,width=220,height=40)
        #detect face
        img5=Image.open("images\\traindata1.png")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=600,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=600,y=400,width=220,height=40)

        #Attendance
        img6=Image.open("images\\at1.png")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=900,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=900,y=400,width=220,height=40)
        
        #Help Desk
        img7=Image.open("images\\help1.jpg")
        img7=img7.resize((200,200),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1200,y=200,width=220,height=220) #box size changed

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1200,y=400,width=220,height=40)
        #Train Data
        img8=Image.open("images\\attendance.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=300,y=480,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=300,y=700,width=220,height=40)
 
        #Photos
        img9=Image.open("images\\photo1.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=600,y=480,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=600,y=700,width=220,height=40)

        #Devloper
        img10=Image.open("images\\dev3.png")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=900,y=480,width=220,height=220)

        b1_1=Button(bg_img,text="Developers",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=900,y=700,width=220,height=40)

        #Exit
        img11=Image.open("images\\exit1.png")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit)
        b1.place(x=1200,y=480,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1200,y=700,width=220,height=40)

    def open_img(self):
        os.startfile("data")   

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("face recognition","Are you sure to exit ",parent=self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return




        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student( self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train( self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition( self.new_window)

    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer( self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help( self.new_window)


    


    




if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
